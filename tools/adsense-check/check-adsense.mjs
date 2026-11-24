#!/usr/bin/env node
/**
 * AdSense readiness audit.
 *
 * Crawls the site (sitemap first, then internal links) and reports the
 * problems AdSense reviewers commonly reject sites for. Read-only: it only
 * sends GET requests.
 *
 *   npm run check:adsense                          # audits the live site
 *   npm run check:adsense -- http://127.0.0.1:8000 # audits a local server
 *   npm run check:adsense -- --max-pages 100
 *
 * Exit code 1 if any ERROR is found, 0 if only warnings or nothing.
 */

const args = process.argv.slice(2);
const opt = (name, dflt) => {
  const i = args.indexOf(name);
  return i >= 0 ? args[i + 1] : dflt;
};
const BASE = (args.find(a => /^https?:\/\//.test(a)) || process.env.SITE_URL || 'https://www.sarkarinaukriresult.online').replace(/\/$/, '');
const MAX_PAGES = Number(opt('--max-pages', 400));
const MIN_WORDS = Number(opt('--min-words', 150));
const CONCURRENCY = 4;
const TIMEOUT_MS = 20000;
const SLOW_MS = 3000;

const base = new URL(BASE);
const IS_LOCAL = /^(localhost|127\.|0\.0\.0\.0)/.test(base.hostname);
const BARE_HOST = base.hostname.replace(/^www\./, '');

const findings = [];
const add = (level, check, where, detail) => findings.push({ level, check, where, detail });
const err = (...a) => add('ERROR', ...a);
const warn = (...a) => add('WARN', ...a);

// ---------- fetching ----------
const cache = new Map();
async function get(url, { follow = true } = {}) {
  const key = `${follow}|${url}`;
  if (cache.has(key)) return cache.get(key);
  const p = (async () => {
    const t0 = Date.now();
    try {
      const res = await fetch(url, {
        redirect: follow ? 'follow' : 'manual',
        signal: AbortSignal.timeout(TIMEOUT_MS),
        headers: { 'User-Agent': 'adsense-readiness-check/1.0' },
      });
      const type = res.headers.get('content-type') || '';
      const body = /text|xml|json|javascript/.test(type) ? await res.text() : (await res.arrayBuffer(), '');
      return { url, status: res.status, location: res.headers.get('location'), finalUrl: res.url, type, body, ms: Date.now() - t0 };
    } catch (e) {
      return { url, status: 0, error: e.message, body: '', ms: Date.now() - t0 };
    }
  })();
  cache.set(key, p);
  return p;
}

async function pool(items, fn) {
  const out = [];
  let i = 0;
  await Promise.all(Array.from({ length: CONCURRENCY }, async () => {
    while (i < items.length) {
      const idx = i++;
      out[idx] = await fn(items[idx]);
    }
  }));
  return out;
}

// ---------- HTML helpers (no dependencies) ----------
const decode = s => s
  .replace(/&nbsp;/g, ' ').replace(/&amp;/g, '&').replace(/&lt;/g, '<').replace(/&gt;/g, '>')
  .replace(/&quot;/g, '"').replace(/&#0?39;|&apos;/g, "'").replace(/&rsaquo;|&raquo;|&ndash;|&mdash;/g, ' ')
  .replace(/&#(\d+);/g, (_, n) => String.fromCodePoint(Number(n)));
const strip = html => decode(html
  .replace(/<!--[\s\S]*?-->/g, ' ')
  .replace(/<(script|style|noscript|svg|template)\b[\s\S]*?<\/\1>/gi, ' ')
  .replace(/<[^>]+>/g, ' ')).replace(/\s+/g, ' ').trim();
const attr = (tag, name) => {
  const m = tag.match(new RegExp(`\\b${name}\\s*=\\s*("([^"]*)"|'([^']*)'|([^\\s>]+))`, 'i'));
  return m ? decode(m[2] ?? m[3] ?? m[4] ?? '') : null;
};
const metaContent = (html, name) => {
  for (const tag of html.match(/<meta\b[^>]*>/gi) || []) {
    if ((attr(tag, 'name') || attr(tag, 'property') || '').toLowerCase() === name) return attr(tag, 'content');
  }
  return null;
};
const title = html => { const m = html.match(/<title[^>]*>([\s\S]*?)<\/title>/i); return m ? strip(m[1]) : null; };
const h1s = html => (html.match(/<h1\b[^>]*>[\s\S]*?<\/h1>/gi) || []).map(strip).filter(Boolean);

/** Page content without the site header, menus and footer, which repeat on every page. */
function mainContent(html) {
  let body = html;
  const main = html.match(/<main\b[^>]*>([\s\S]*?)<\/main>/i);
  if (main) body = main[1];
  else {
    const endHeader = body.search(/<\/header>/i);
    if (endHeader >= 0) body = body.slice(endHeader);
    const footer = body.search(/<footer\b/i);
    if (footer >= 0) body = body.slice(0, footer);
  }
  return body.replace(/<(nav|aside)\b[\s\S]*?<\/\1>/gi, ' ').replace(/<form\b[\s\S]*?<\/form>/gi, ' ');
}
const footerHtml = html => { const m = html.match(/<footer\b[\s\S]*?<\/footer>/i); return m ? m[0] : ''; };

function links(html, pageUrl) {
  const out = [];
  for (const tag of html.match(/<a\b[^>]*>/gi) || []) {
    const href = attr(tag, 'href');
    if (!href || /^(#|mailto:|tel:|javascript:)/i.test(href)) continue;
    try { out.push(new URL(href, pageUrl)); } catch { /* ignore malformed */ }
  }
  return out;
}
const isInternal = u => u.hostname === base.hostname || u.hostname === BARE_HOST;
const pathKey = u => u.pathname + u.search;
const STATIC_EXT = /\.(pdf|jpe?g|png|gif|webp|svg|ico|css|js|xml|txt|zip|docx?|xlsx?)$/i;

// ---------- site-level checks ----------
async function siteChecks(home) {
  // HTTPS and canonical host
  if (!IS_LOCAL) {
    if (base.protocol !== 'https:') err('HTTPS', BASE, 'Site is not served over HTTPS.');
    const http = await get(`http://${base.hostname}/`, { follow: false });
    if (![301, 308].includes(http.status) || !/^https:/.test(http.location || ''))
      err('HTTPS redirect', `http://${base.hostname}/`, `Expected a permanent redirect to https, got ${http.status} ${http.location || ''}`);
    if (base.hostname !== BARE_HOST) {
      const bare = await get(`https://${BARE_HOST}/`, { follow: false });
      if (bare.status === 0) err('Canonical host', BARE_HOST, `Bare domain does not respond: ${bare.error}`);
      else if (![301, 308].includes(bare.status) || !(bare.location || '').includes(base.hostname))
        err('Canonical host', `https://${BARE_HOST}/`, `Bare domain should 301 to ${base.hostname}, got ${bare.status} ${bare.location || ''}. Two copies of the site look like duplicate content.`);
    }
  }

  // AdSense code and ads.txt
  const client = (home.body.match(/ca-pub-\d{10,}/) || [])[0];
  if (!client) err('AdSense code', '/', 'No AdSense script (ca-pub-...) on the homepage; AdSense cannot verify the site.');
  if (/adsbygoogle\.js\?client=(?:&|"|')/.test(home.body)) err('AdSense code', '/', 'AdSense script has an empty client id.');
  const hosts = IS_LOCAL ? [BASE] : [BASE, `https://${BARE_HOST}`];
  for (const h of hosts) {
    const ads = await get(`${h}/ads.txt`, { follow: false });
    if (ads.status !== 200) { err('ads.txt', `${h}/ads.txt`, `Expected 200 without a redirect, got ${ads.status}.`); continue; }
    const line = ads.body.split(/\r?\n/).find(l => /^\s*google\.com\s*,/i.test(l));
    if (!line) err('ads.txt', `${h}/ads.txt`, 'No google.com line.');
    else {
      const [, pub, rel, tag] = line.split(',').map(s => s.trim());
      if (client && pub !== client.replace('ca-', '')) err('ads.txt', `${h}/ads.txt`, `Publisher id ${pub} does not match the site code ${client}.`);
      if ((rel || '').toUpperCase() !== 'DIRECT') err('ads.txt', `${h}/ads.txt`, 'Relationship should be DIRECT.');
      if (tag !== 'f08c47fec0942fa0') warn('ads.txt', `${h}/ads.txt`, 'Google certification id should be f08c47fec0942fa0.');
    }
  }

  // robots.txt and sitemap
  const robots = await get(`${BASE}/robots.txt`);
  let sitemapUrls = [];
  if (robots.status !== 200) err('robots.txt', '/robots.txt', `Status ${robots.status}.`);
  else {
    let agent = null; const blockedFor = new Set();
    for (const raw of robots.body.split(/\r?\n/)) {
      const l = raw.replace(/#.*/, '').trim();
      const [k, ...v] = l.split(':'); const val = v.join(':').trim();
      if (/^user-agent$/i.test(k)) agent = val.toLowerCase();
      else if (/^disallow$/i.test(k) && val === '/') blockedFor.add(agent);
      else if (/^sitemap$/i.test(k)) sitemapUrls.push(val);
    }
    for (const a of ['*', 'googlebot', 'mediapartners-google', 'adsbot-google'])
      if (blockedFor.has(a)) err('robots.txt', '/robots.txt', `"Disallow: /" for ${a} blocks the whole site.`);
    if (!sitemapUrls.length) warn('robots.txt', '/robots.txt', 'No Sitemap: line.');
    for (const s of sitemapUrls) if (!IS_LOCAL && !s.startsWith(BASE)) warn('robots.txt', '/robots.txt', `Sitemap URL ${s} is not on ${BASE}.`);
  }
  if (!sitemapUrls.length) sitemapUrls = [`${BASE}/sitemap.xml`];

  const pageUrls = [];
  const queue = [...sitemapUrls];
  while (queue.length) {
    const s = queue.shift();
    const fetchUrl = IS_LOCAL ? s.replace(/^https?:\/\/[^/]+/, BASE) : s;
    const sm = await get(fetchUrl);
    if (sm.status !== 200) { err('Sitemap', s, `Status ${sm.status}.`); continue; }
    const locs = [...sm.body.matchAll(/<loc>\s*([^<]+?)\s*<\/loc>/g)].map(m => decode(m[1]));
    if (/<sitemapindex/i.test(sm.body)) queue.push(...locs);
    else pageUrls.push(...locs);
  }
  if (!pageUrls.length) err('Sitemap', '/sitemap.xml', 'Sitemap lists no pages.');
  for (const u of pageUrls) if (!IS_LOCAL && !u.startsWith(BASE + '/')) err('Sitemap', u, `Sitemap URL is not on ${BASE} (wrong host or protocol).`);
  return { client, sitemap: new Set(pageUrls.map(u => new URL(u).pathname)) };
}

// ---------- required trust pages ----------
const TRUST = [
  { name: 'Privacy Policy', re: /privacy/i },
  { name: 'About', re: /about/i },
  { name: 'Contact', re: /contact/i },
  { name: 'Terms', re: /terms|conditions/i },
];

async function trustChecks(home) {
  const found = {};
  const foot = footerHtml(home.body) || home.body;
  for (const u of links(foot, BASE).filter(isInternal)) {
    for (const t of TRUST) if (!found[t.name] && t.re.test(u.pathname)) found[t.name] = u;
  }
  for (const t of TRUST) {
    if (!found[t.name]) { err('Required pages', '/', `No ${t.name} page linked from the homepage footer.`); continue; }
    const page = await get(found[t.name].href);
    if (page.status !== 200) { err('Required pages', found[t.name].pathname, `${t.name} page returns ${page.status}.`); continue; }
    const text = strip(mainContent(page.body));
    if (t.name === 'Privacy Policy') {
      const need = [
        [/cookie/i, 'cookies'],
        [/google/i, 'Google as an ad vendor'],
        [/third[- ]party (vendors|advertis)/i, 'third-party vendors use cookies to serve ads'],
        [/ads settings|adssettings\.google|myadcenter\.google/i, 'how to opt out (Google Ads Settings link)'],
      ];
      for (const [re, what] of need) if (!re.test(page.body)) err('Privacy policy', found[t.name].pathname, `Does not mention ${what}; AdSense requires this disclosure.`);
    }
    if (t.name === 'Contact' && !/@[a-z0-9-]+\.[a-z]{2,}|<form\b/i.test(mainContent(page.body)))
      err('Contact page', found[t.name].pathname, 'No email address or contact form.');
    if (text.split(/\s+/).length < 80) warn('Required pages', found[t.name].pathname, `${t.name} page is very short (${text.split(/\s+/).length} words).`);
  }
  return found;
}

// ---------- per-page checks ----------
const PLACEHOLDER = [
  [/lorem ipsum/i, 'lorem ipsum'],
  [/under construction|coming soon/i, '"coming soon"/"under construction"'],
  [/\{\{|\{%|%\}/, 'unrendered template tags'],
  [/\bTODO\b|\bFIXME\b/, 'TODO/FIXME'],
  [/\b(?:None|undefined|NaN|null)\b(?=\s*(?:<|$))/, 'empty value shown as None/undefined/NaN'],
  [/\btest (?:post|page|job)\b|\bsample (?:post|text)\b|\bdummy (?:text|data)\b/i, 'test or dummy content'],
];
const EMPTY_LIST = /no (?:jobs|results|posts|items|admit cards|answer keys|records|guides) (?:found|available|yet)/i;

async function auditPage(url, ctx) {
  const res = await get(url);
  const path = new URL(url).pathname + new URL(url).search;
  if (res.status !== 200) { err('Broken page', path, `Status ${res.status || res.error}.`); return null; }
  if (!/html/.test(res.type)) return null;
  const finalPath = new URL(res.finalUrl || url).pathname;
  if (finalPath !== new URL(url).pathname && ctx.sitemap.has(new URL(url).pathname))
    err('Sitemap', path, `Sitemap URL redirects to ${finalPath}; list the final URL instead.`);
  if (res.ms > SLOW_MS) warn('Slow page', path, `Took ${(res.ms / 1000).toFixed(1)}s to load.`);

  const html = res.body;
  const robots = (metaContent(html, 'robots') || '').toLowerCase();
  const indexable = !/noindex/.test(robots);
  const t = title(html);
  const desc = metaContent(html, 'description');
  const h = h1s(html);
  const content = mainContent(html);
  const text = strip(content);
  const words = text ? text.split(/\s+/).filter(w => /[\p{L}\p{N}]/u.test(w)).length : 0;
  const canonical = (html.match(/<link\b[^>]*rel=["']canonical["'][^>]*>/i) || [])[0];

  if (!/<meta\b[^>]*name=["']viewport["']/i.test(html)) err('Mobile', path, 'No viewport meta tag.');
  if (!/<html\b[^>]*\blang=/i.test(html)) warn('HTML', path, 'No lang attribute on <html>.');
  if (!t) err('Title', path, 'Missing <title>.');
  else if (t.length > 70) warn('Title', path, `Title is ${t.length} characters (over ~70 gets cut off).`);
  if (indexable) {
    if (!desc) warn('Meta description', path, 'Missing meta description.');
    else if (desc.length > 160) warn('Meta description', path, `Meta description is ${desc.length} characters.`);
    if (!h.length) err('Headings', path, 'No visible <h1>.');
    else if (h.length > 1) warn('Headings', path, `${h.length} <h1> tags.`);
    if (!canonical) warn('Canonical', path, 'No rel=canonical link.');
    else if (!IS_LOCAL && attr(canonical, 'href') !== `${BASE}${new URL(res.finalUrl).pathname}`)
      warn('Canonical', path, `Canonical points to ${attr(canonical, 'href')}.`);
    if (words < MIN_WORDS) err('Thin content', path, `Indexable page has only ${words} words of its own content (min ${MIN_WORDS}). Add content or mark it noindex.`);
    if (EMPTY_LIST.test(text)) err('Empty page', path, 'Indexable page says nothing was found. Mark empty listings noindex.');
    if (!ctx.sitemap.has(new URL(res.finalUrl).pathname) && !new URL(url).search)
      warn('Sitemap', path, 'Indexable page is missing from the sitemap.');
  } else if (ctx.sitemap.has(new URL(url).pathname)) {
    err('Sitemap', path, 'Page is noindex but listed in the sitemap.');
  }
  for (const [re, what] of PLACEHOLDER) {
    const m = text.match(re) || (what === 'unrendered template tags' ? null : null);
    if (m) err('Placeholder content', path, `Contains ${what}: "…${text.slice(Math.max(0, m.index - 40), m.index + 40)}…"`);
  }
  for (const m of html.matchAll(/<(?:script|img|iframe|link|source|video|audio)\b[^>]*\b(?:src|href)=["'](http:\/\/[^"']+)/gi))
    if (!IS_LOCAL) err('Mixed content', path, `Loads ${m[1]} over plain HTTP.`);

  // Footer must link trust pages on every page
  const foot = footerHtml(html);
  for (const [name, u] of Object.entries(ctx.trust))
    if (foot && !foot.includes(`href="${u.pathname}"`) && !foot.includes(u.href)) warn('Required pages', path, `Footer has no link to ${name}.`);

  const out = links(html, res.finalUrl || url);
  for (const u of out) if (isInternal(u) && u.protocol === 'http:' && !IS_LOCAL) warn('Links', path, `Internal link uses http: ${u.href}`);
  const imgs = [...html.matchAll(/<img\b[^>]*>/gi)].map(m => m[0]);
  for (const tag of imgs) if (attr(tag, 'alt') === null) warn('Images', path, `Image without alt text: ${attr(tag, 'src')}`);
  const imgUrls = imgs.map(tag => { try { return new URL(attr(tag, 'src') || '', res.finalUrl); } catch { return null; } }).filter(u => u && isInternal(u));

  return { path: new URL(res.finalUrl).pathname, indexable, title: t, desc, links: out.filter(isInternal), imgUrls };
}

// ---------- main ----------
(async () => {
  console.log(`AdSense readiness check for ${BASE}\n`);
  const home = await get(`${BASE}/`);
  if (home.status !== 200) { console.error(`Homepage returned ${home.status || home.error}. Is the site running?`); process.exit(2); }

  const { sitemap } = await siteChecks(home);
  const trust = await trustChecks(home);
  const ctx = { sitemap, trust };

  // Crawl: sitemap pages first, then internal links they point to
  const toUrl = p => `${BASE}${p}`;
  const seen = new Set();
  const linkedFrom = new Map(); // target path -> a page linking to it
  let frontier = [...sitemap].map(toUrl);
  const pages = [];
  while (frontier.length && pages.length < MAX_PAGES) {
    const batch = frontier.filter(u => !seen.has(u)).slice(0, MAX_PAGES - pages.length);
    batch.forEach(u => seen.add(u));
    const results = await pool(batch, u => auditPage(u, ctx));
    const next = [];
    for (const r of results.filter(Boolean)) {
      pages.push(r);
      for (const u of r.links) {
        const key = pathKey(u);
        if (!linkedFrom.has(key)) linkedFrom.set(key, r.path);
        if (!u.search && !STATIC_EXT.test(u.pathname) && !/^\/(admin|cms|django-admin|static|media)\//.test(u.pathname)) next.push(toUrl(u.pathname));
      }
    }
    frontier = [...new Set(next)];
  }

  // Every internal link, including filtered listings and files, must resolve
  const toCheck = [...linkedFrom.keys()].filter(k => !seen.has(toUrl(k.split('?')[0])) || k.includes('?'))
    .filter(k => !/^\/(admin|cms|django-admin)\//.test(k));
  const statuses = await pool(toCheck, k => get(toUrl(k)));
  statuses.forEach((r, i) => {
    if (r.status >= 400 || r.status === 0) err('Broken link', toCheck[i], `Returns ${r.status || r.error}; linked from ${linkedFrom.get(toCheck[i])}.`);
  });
  const imgKeys = [...new Set(pages.flatMap(p => p.imgUrls.map(pathKey)))];
  const imgRes = await pool(imgKeys, k => get(toUrl(k)));
  imgRes.forEach((r, i) => { if (r.status >= 400 || r.status === 0) err('Broken image', imgKeys[i], `Returns ${r.status || r.error}.`); });

  // Duplicates across indexable pages
  const dup = (field, label) => {
    const by = new Map();
    for (const p of pages.filter(p => p.indexable && p[field])) by.set(p[field], [...(by.get(p[field]) || []), p.path]);
    for (const [v, ps] of by) if (ps.length > 1) warn(label, ps.slice(0, 5).join(', ') + (ps.length > 5 ? ` (+${ps.length - 5})` : ''), `${ps.length} indexable pages share: "${v.slice(0, 80)}"`);
  };
  dup('title', 'Duplicate title');
  dup('desc', 'Duplicate description');

  const indexable = pages.filter(p => p.indexable).length;
  if (indexable < 30) warn('Site size', BASE, `Only ${indexable} indexable pages found; AdSense tends to want a substantial amount of original content.`);

  // ---------- report ----------
  const errors = findings.filter(f => f.level === 'ERROR');
  const warns = findings.filter(f => f.level === 'WARN');
  const print = (list, label) => {
    if (!list.length) return;
    console.log(`${label} (${list.length})`);
    const byCheck = new Map();
    for (const f of list) byCheck.set(f.check, [...(byCheck.get(f.check) || []), f]);
    for (const [check, fs] of byCheck) {
      console.log(`  ${check}`);
      for (const f of fs.slice(0, 25)) console.log(`    ${f.where}  ${f.detail}`);
      if (fs.length > 25) console.log(`    ... and ${fs.length - 25} more`);
    }
    console.log('');
  };
  print(errors, 'ERRORS');
  print(warns, 'WARNINGS');
  console.log(`Crawled ${pages.length} pages (${indexable} indexable), checked ${toCheck.length} extra links and ${imgKeys.length} images.`);
  console.log(errors.length ? `FAIL: ${errors.length} error(s), ${warns.length} warning(s).` : `PASS: no errors, ${warns.length} warning(s).`);
  // exitCode instead of process.exit(): exiting while fetch sockets are still
  // open crashes Node on Windows (libuv assertion) and loses the exit code
  process.exitCode = errors.length ? 1 : 0;
})();
