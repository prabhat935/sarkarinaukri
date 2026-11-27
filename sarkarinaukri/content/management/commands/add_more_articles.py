import datetime
from django.core.management.base import BaseCommand
from content.models import Article
from content.seeding import upsert


ADDITIONAL_ARTICLES = [
    {
        'title': 'Government Exam Study Strategy: How to Prepare for Prelims While Studying for Mains',
        'slug': 'exam-study-strategy-prelims-mains',
        'category': 'preparation',
        'published_date': datetime.date(2026, 5, 11),
        'excerpt': 'Learn the effective strategy to balance preparing for prelims and mains simultaneously in government exams — time allocation, subject prioritization, and mock test scheduling.',
        'meta_description': 'Government exam preparation strategy: balance prelims and mains study with effective time management and subject prioritization for SSC and UPSC.',
        'content': """<p>Government exam candidates often struggle with a fundamental question: should they focus on mains after clearing prelims, or should they prepare for both simultaneously? The answer for competitive exams like SSC CGL and UPSC is clear — you must prepare for both at the same time, but with a strategic approach.</p>

<h2>Why Simultaneous Preparation is Necessary</h2>
<p>In SSC CGL, the gap between Tier I (prelims) and Tier II (mains) is typically 3–4 months. Starting mains preparation only after clearing Tier I leaves you with insufficient time to cover the vastly expanded syllabus of Tier II. Similarly, for UPSC, the gap between Prelims and Mains is 4–5 months — a tight window if you start from scratch.</p>

<p>Moreover, the knowledge required for mains is a superset of what you need for prelims. Preparing for mains simultaneously strengthens your prelims foundation without wasting time on redundant study phases.</p>

<h2>Time Allocation Strategy</h2>
<p><strong>Phase 1: First 2–3 months (60% Prelims, 40% Mains)</strong><br>
Focus primarily on clearing the prelims cutoff. Spend 6 hours daily on prelims strategy: mock tests, speed practice, and accuracy building. The remaining 2–3 hours should go into reading sources for mains GS (The Hindu newspaper, NCERT basics, policy documents).</p>

<p><strong>Phase 2: Last 1 month before prelims (80% Prelims, 20% Mains)</strong><br>
Increase prelims focus to 8 hours daily. Do mock tests every second day. Use the remaining 1–2 hours to read mains-relevant news and continue slow reading of standard references.</p>

<p><strong>After Prelims: Transition to Mains</strong><br>
Once you clear prelims, shift to 70% mains preparation and 30% revision of prelims-level current affairs and GS. Mains requires detailed answer writing practice that cannot be rushed.</p>

<h2>Subject-Wise Prioritization</h2>
<p><strong>Overlap Subjects (Study for Both Simultaneously):</strong></p>
<ul>
<li>General Studies: Mains GS syllabus includes prelims topics with added depth (e.g., Polity, Economics, History)</li>
<li>Current Affairs: Equally important for both stages</li>
<li>Reasoning: Prelims tests basic reasoning; mains requires no reasoning but answer writing skills based on reasoning foundation</li>
</ul>

<p><strong>Mains-Only Subjects (Study after clearing prelims):</strong></p>
<ul>
<li>Optional subject (for UPSC Mains) — 500 marks, requires deep knowledge of 1–2 subjects</li>
<li>Mains descriptive sections requiring extended essay writing</li>
<li>English descriptive paper (500 words essays, précis, letter writing)</li>
</ul>

<p><strong>Quick Win: GS Revision for Mains During Prelims Prep</strong><br>
Instead of formal study sessions, use travel time (30 min commute) or meal time (15 min) to read one section of a mains GS reference book daily. By the time you clear prelims, you will have read through 60–70% of mains content in thin layer, requiring only deeper revision later.</p>

<h2>Mock Test Strategy</h2>
<p><strong>For Prelims (3–4 weeks before exam):</strong><br>
Take full-length prelims mock tests every 2–3 days. Review mistakes immediately. These are your primary practice ground for speed and accuracy.</p>

<p><strong>For Mains (after clearing prelims):</strong><br>
Answer writing practice becomes paramount. Write full-length answers (150–250 words) for 2–3 mains questions daily. Take sectional and full mains mock tests (4–5 hour papers) twice per week.</p>

<p><strong>Integration Mock (1 month before mains):</strong><br>
Attempt mock tests where you write answers in real exam conditions — no breaks except those allowed in the actual exam. Time yourself strictly.</p>

<h2>What NOT to Do</h2>
<ul>
<li>Do not ignore mains completely during prelims prep and expect to catch up after prelims — it's humanly impossible in the available timeframe</li>
<li>Do not study mains topics in the exact same depth as prelims during the initial phase — that's inefficient. Use a thin-layer approach to cover breadth, then add depth after prelims</li>
<li>Do not neglect current affairs at any stage — it features in both prelims and mains</li>
<li>Do not spend 10+ hours daily thinking you will clear both in one go — 8 hours of focused study beats 12 hours of scattered effort</li>
</ul>

<p>The key to success is understanding that mains preparation is not a separate phase that starts after prelims — it's a continuous process where you build knowledge layers. By the time you sit for prelims, you should already have a thin understanding of mains topics, allowing you to deepen that knowledge in the post-prelims period without starting from zero.</p>
""",
    },
    {
        'title': 'Current Affairs for Government Exams: Best Sources and How to Take Notes',
        'slug': 'current-affairs-government-exams-best-sources',
        'category': 'preparation',
        'published_date': datetime.date(2026, 5, 12),
        'excerpt': 'The definitive guide to mastering current affairs for competitive exams — which newspapers to read, how to take notes, important news categories, and revision strategy.',
        'meta_description': 'Current affairs for competitive exams: best sources, note-taking techniques, important news categories for SSC, UPSC, banking exams.',
        'content': """<p>Current affairs is often the make-or-break section in government exams. Unlike static GK, which remains constant, current affairs changes daily with new policies, appointments, international events, and economic developments. This guide explains how to consume current affairs efficiently for maximum exam impact.</p>

<h2>Best Sources for Current Affairs</h2>
<p><strong>Tier 1: Official Government Sources (Most Important)</strong><br>
These carry absolute credibility and often provide wording that matches exam questions:</p>
<ul>
<li>PIB (Press Information Bureau) — official government press releases. Visit pib.gov.in daily.</li>
<li>Ministry websites — check your ministry of interest (e.g., Ministry of Education, Ministry of Finance)</li>
<li>RBI website — important for policy announcements affecting the economy</li>
<li>NITI Aayog — policy documents and development initiatives</li>
</ul>

<p><strong>Tier 2: Newspapers and News Aggregators</strong></p>
<ul>
<li><strong>The Hindu editorial:</strong> Read 1 editorial daily. Editorials provide expert analysis on policy issues. Not for facts, but for understanding policy rationale.</li>
<li><strong>Indian Express:</strong> Similar to The Hindu. Read the Explained series for in-depth issue analysis.</li>
<li><strong>News aggregator apps (Inshorts, DailyHunt):</strong> 10-minute daily browse for headline updates</li>
</ul>

<p><strong>Tier 3: Specialized Sources</strong></p>
<ul>
<li>Environment: Mongabay India, Down to Earth magazine</li>
<li>Defense & Security: Indian Defense Review, strategic studies publications</li>
<li>Economy: MOODY's reports, WEF (World Economic Forum) publications</li>
</ul>

<h2>What to Read vs. What to Skip</h2>
<p><strong>Read (Exam-Relevant):</strong></p>
<ul>
<li>Government schemes and policy announcements</li>
<li>Appointments of key officials (President, PM, RBI Governor, election commissioners)</li>
<li>International summits and their outcomes</li>
<li>Budget announcements and policy decisions</li>
<li>Major awards and recognitions to Indians (e.g., Nobel Prize, Padma awards)</li>
<li>Major infrastructure projects and their milestones</li>
<li>Constitutional amendments and court judgments on important issues</li>
<li>Environment and climate news (climate summits, new environmental policies)</li>
<li>Defense and security developments</li>
</ul>

<p><strong>Skip (Generally Low Exam Value):</strong></p>
<ul>
<li>Celebrity gossip and sports controversies</li>
<li>Accident/disaster news without policy implications</li>
<li>Hyperlocal city news unrelated to governance</li>
<li>Repetitive updates on the same story</li>
</ul>

<h2>Note-Taking System for Current Affairs</h2>
<p><strong>The Categorized Approach:</strong><br>
Organize notes under fixed categories so revision is targeted:</p>
<ul>
<li><strong>National Affairs:</strong> Government policies, constitutional issues, governance</li>
<li><strong>International Affairs:</strong> Bilateral relations, international organizations, global issues</li>
<li><strong>Economy & Finance:</strong> Budget, RBI policy, taxation, inflation</li>
<li><strong>Environment & Science:</strong> Climate summits, IPCC reports, new scientific discoveries</li>
<li><strong>People & Places:</strong> Appointments, awards, heritage sites, new states/unions</li>
</ul>

<p><strong>The 3-Line Rule:</strong><br>
For each news item, write exactly 3 lines in your notes:</p>
<ol>
<li>What happened (the event)</li>
<li>Why it matters (the implication for policy or governance)</li>
<li>Expected exam angle (what question could be asked)</li>
</ol>

<p>Example:</p>
<p>Event: PM inaugurated National Hydrogen Mission 2026<br>
Why: India transitioning from coal to green energy; target of net-zero by 2070<br>
Exam angle: Probable question about India's renewable energy targets, hydrogen production capacity</p>

<h2>Revision Strategy</h2>
<p><strong>Weekly Revision:</strong> Every Sunday, spend 30 minutes reviewing notes from the previous week. This ensures facts stay fresh.</p>

<p><strong>Monthly Review:</strong> On the last Sunday of each month, spend 1–2 hours reviewing the entire month's notes. Create a summary of top 10 headlines from the month.</p>

<p><strong>3 Months Before Exam:</strong> Create a condensed "current affairs booklet" with the most important news from the last 6 months. Revise this booklet once per week.</p>

<p><strong>1 Month Before Exam:</strong> Focus only on the condensed booklet. Do not read new news actively — just stay updated via headlines.</p>

<h2>How Much Current Affairs to Expect</h2>
<p>In SSC CGL Tier I, General Awareness has 25 questions, of which 8–10 are typically current affairs. In UPSC Prelims, 15–20 questions from current affairs across both GS Paper I and CSAT. Current affairs is roughly 15–25% of total marks across government exams.</p>

<p>Consistent daily reading for 20–30 minutes is far superior to cramming everything in the last month before the exam. Start your current affairs habit from Day 1 of your preparation and maintain it religiously.</p>
""",
    },
    {
        'title': 'Age Relaxation in Government Jobs: Complete Category-Wise Guidelines 2026',
        'slug': 'age-relaxation-government-jobs-2026',
        'category': 'career',
        'published_date': datetime.date(2026, 5, 13),
        'excerpt': 'How much age relaxation SC, ST, OBC, PwBD and ex-servicemen candidates get in central government jobs, why EWS gets none, how relaxations combine, and which date your age is counted on.',
        'meta_description': 'Age relaxation in central government jobs: SC/ST 5 years, OBC 3, PwBD 10 to 15, ex-servicemen rules, why EWS gets none, and how relaxations combine.',
        'content': """<p>Every government job notification sets a minimum and maximum age, and then lets some groups of candidates go above the maximum. Getting this right matters: an application from a candidate who is over age is rejected at document verification, often after they have cleared the exam. This guide explains the relaxations used in central government recruitment such as SSC, UPSC, RRB and the public sector banks, and how to work out your own limit.</p>

<h2>The Standard Central Government Relaxations</h2>
<p>These are the usual figures. Each notification has an age relaxation table, and that table is what counts for that recruitment.</p>
<ul>
<li><strong>SC and ST: 5 years</strong> above the upper age limit.</li>
<li><strong>OBC (non-creamy layer): 3 years.</strong> You need an OBC certificate in the central government format showing that you are not in the creamy layer; a creamy-layer OBC candidate applies as unreserved.</li>
<li><strong>EWS: no age relaxation.</strong> EWS candidates get reserved vacancies, but they follow the same age limit as unreserved candidates. For example, UPSC's Advertisement 13/2026 sets 35 years for both UR and EWS.</li>
<li><strong>Persons with benchmark disabilities (40% or more): 10 years</strong>, added on top of the category relaxation. That gives 10 years for an unreserved or EWS candidate, 13 years for OBC and 15 years for SC or ST.</li>
<li><strong>Ex-servicemen:</strong> for most Group C and non-gazetted Group B posts, the period of military service is deducted from your actual age, and the result may be up to 3 years above the limit. Our <a href="/content/guides/ex-servicemen-age-relaxation-calculation/">ex-servicemen age guide</a> works through examples. Gazetted posts filled through UPSC have their own ex-servicemen rules, given in each notice.</li>
</ul>
<p>Many notices add further relaxations for particular groups, such as central government civilian employees with a set period of regular service, widows and divorced or judicially separated women who have not remarried, and the children of personnel killed in action. The amounts differ between exams, so look them up in the notice rather than assuming a figure.</p>

<h2>A Worked Example</h2>
<p>Suppose a post has an age limit of 18 to 27 years on 1 January 2027.</p>
<ul>
<li>Unreserved or EWS candidate: must be born on or after 2 January 1999 and on or before 1 January 2009.</li>
<li>OBC candidate: upper limit 27 + 3 = 30 years.</li>
<li>SC or ST candidate: upper limit 27 + 5 = 32 years.</li>
<li>OBC candidate with a benchmark disability: 27 + 13 = 40 years.</li>
<li>SC candidate with a benchmark disability: 27 + 15 = 42 years.</li>
</ul>
<p>Relaxation only raises the upper limit. The minimum age stays the same for everyone.</p>

<h2>How Relaxations Combine</h2>
<p>The disability relaxation is designed to be added to the category relaxation, which is why an SC candidate with a benchmark disability gets 15 years rather than 10. Ex-servicemen who are also SC, ST or OBC usually have their own rows in the relaxation table. Most other relaxations do not add up: if you qualify for two of them, you take the one that gives you the higher limit. When in doubt, the notice's table decides, not a rule of thumb.</p>

<h2>The Date Your Age Is Counted On</h2>
<p>Your age is not counted on the day you apply. Each notice names a "crucial date" or "as on" date, and you must be within the limits on that date. SSC usually fixes a specific date such as 1 January or 1 August of the exam year. UPSC recruitment advertisements generally use the closing date for applications. State commissions set their own dates. Read this line of the notice first; a single day either way can decide whether you are eligible.</p>

<h2>State Government Jobs Are Different</h2>
<p>State recruitment follows the state's own rules, and these often differ from central ones. For example, Rajasthan's RSSB gives 5 years to general category women and 10 years to reserved category women of Rajasthan, which central rules do not. State reservation and relaxation are usually only for that state's residents; candidates from other states apply as unreserved.</p>

<h2>How to Claim It</h2>
<ul>
<li><strong>Get the right certificate in time.</strong> OBC certificates for central jobs must be in the central format and show non-creamy layer status for the year the notice asks for. Disability certificates must be issued by the competent medical authority. Ex-servicemen need their discharge book or release order.</li>
<li><strong>Choose your category correctly in the form.</strong> The relaxation is applied from what you declare, and changing it later is usually not allowed.</li>
<li><strong>Keep the originals for document verification.</strong> If a certificate does not match your claim, the candidature is cancelled even after selection.</li>
</ul>

<h2>Common Mistakes</h2>
<ul>
<li>Assuming EWS gives extra age. It does not in central recruitment.</li>
<li>Counting age on the application date instead of the notice's crucial date.</li>
<li>Using a state-format OBC certificate for a central job.</li>
<li>Applying the same relaxation in a state exam as in a central one.</li>
</ul>
<p>Our <a href="/content/guides/how-to-read-government-job-notification/">guide to reading a notification</a> shows where to find the age table in a typical notice.</p>
""",
    },
    {
        'title': 'Document Verification Stage in Government Exams: Complete Checklist and Common Mistakes',
        'slug': 'document-verification-government-exams-checklist',
        'category': 'preparation',
        'published_date': datetime.date(2026, 5, 14),
        'excerpt': 'Complete checklist of documents required for document verification in government exams, common rejection reasons, and how to prepare beforehand.',
        'meta_description': 'Document verification checklist for government exams: required documents, common mistakes, what to bring to verify credentials.',
        'content': """<p>Document verification is the final gateway before you can join your government job. Hundreds of candidates clear written exams with flying colors but face rejection at the document verification stage due to missing or incorrect documents. This guide ensures you are fully prepared.</p>

<h2>Universal Documents Required (Nearly All Exams)</h2>
<ol>
<li><strong>Admit Card:</strong> Original printout from exam board</li>
<li><strong>Photo Identity Proof:</strong> Original and 1 photocopy. Acceptable: Aadhaar, PAN, Voter ID, Driving License, Passport</li>
<li><strong>Educational Qualification Certificates:</strong> 10th, 12th, Graduation (as per exam requirements). Original + 1 photocopy each</li>
<li><strong>Birth Certificate:</strong> To verify date of birth. 1 photocopy</li>
<li><strong>Category Certificate (if applicable):</strong> SC/ST/OBC/EWS certificate issued within 1 year. Original + 1 photocopy</li>
<li><strong>Character Certificate:</strong> Issued by previous employer or principal. Some exams waive this</li>
<li><strong>Medical Certificate:</strong> If you claimed disability relaxation. Original copy of medical certificate from authorized medical board</li>
</ol>

<h2>Exam-Specific Documents</h2>
<p><strong>For Teaching Posts (KVS, NVS, State Teacher Recruitment):</strong></p>
<ul>
<li>B.Ed degree with passing certificate</li>
<li>CTET/TET qualifying certificate</li>
<li>Subject specialization proof (transcript showing the subject studied)</li>
</ul>

<p><strong>For Banking Posts (IBPS PO, SBI PO, RRB Officer):</strong></p>
<ul>
<li>Graduation or Post-graduation certificate</li>
<li>BBA/B.Com certificate if relevant</li>
<li>Scorecard showing aggregate marks</li>
</ul>

<p><strong>For Defense Forces (SSC, NDA, CDS):</strong></p>
<ul>
<li>Medical examination report (after initial medical)</li>
<li>Police verification report</li>
<li>Domicile certificate (for some posts)</li>
</ul>

<p><strong>For UPSC and State PSC exams:</strong></p>
<ul>
<li>Caste certificate (if claiming OBC/SC/ST)</li>
<li>EWS certificate (if applicable)</li>
<li>Non-Creamy Layer (NCL) certificate (mandatory for OBC candidates)</li>
<li>Proof of domicile (for state-specific recruitment)</li>
</ul>

<h2>Important: Certificate Validity Rules</h2>
<p><strong>OBC-NCL Certificate:</strong> Valid for 1 year from date of issue. Do not use expired certificates.</p>
<p><strong>EWS Certificate:</strong> Valid for one financial year. Get renewed if necessary.</p>
<p><strong>SC/ST Certificate:</strong> Permanent, but ensure it clearly mentions caste and state.</p>
<p><strong>Disability Certificate:</strong> Valid as per medical board's recommendation (usually 2–5 years). Check expiry before document verification.</p>

<h2>Common Mistakes Leading to Rejection</h2>
<ul>
<li><strong>Name mismatch:</strong> If your name in 10th certificate differs from 12th, or from PAN, it creates confusion. Ensure consistent spelling across all documents. If there is a genuine change (marriage, corrections), get an affidavit from a notary.</li>
<li><strong>Date of birth discrepancy:</strong> If your birth certificate shows different DOB than your 10th certificate, it's a major red flag. Get this corrected through official channels before document verification.</li>
<li><strong>Missing marks sheet:</strong> Many candidates bring certificates but not the original marks sheet from their graduation. Marks sheet is essential proof of qualification.</li>
<li><strong>Expired category certificates:</strong> OBC and EWS certificates expire. Always check validity dates.</li>
<li><strong>Incomplete educational records:</strong> Bring all degrees in the right order (10th → 12th → Graduation → Post-graduation). Do not skip any qualification.</li>
<li><strong>Wrong photo ID:</strong> Do not bring a PAN card with an old photo that looks nothing like you. Bring ID with a recent photo or bring multiple ID proofs.</li>
<li><strong>Sloppy photocopies:</strong> Photocopies should be clear and on white paper. Faded or colored photocopies are rejected. Make fresh photocopies 2–3 days before DV.</li>
<li><strong>Missing character certificate:</strong> If exam requires character certificate and you come without one, you face immediate rejection.</li>
</ul>

<h2>Pre-Document Verification Checklist (1 Month Before)</h2>
<ul>
<li>Arrange all required certificates in the specified order</li>
<li>Verify that your name, DOB, and category match across all documents</li>
<li>Get notarized affidavits if there are discrepancies</li>
<li>Check expiry dates of temporary certificates (OBC, EWS, disability)</li>
<li>Get fresh photocopies made on the day before or morning of DV (to avoid paper age issues)</li>
<li>Prepare a file folder with all documents organized and labeled</li>
<li>Take a final photo (for identification at center) matching how you look now</li>
<li>Check the official notification one last time for any exam-specific documents</li>
</ul>

<h2>On the Day of Document Verification</h2>
<ul>
<li>Arrive 30 minutes early — bring your admit card and photo ID</li>
<li>Carry ONE set of original documents and ONE set of photocopies per document</li>
<li>Do not hand over all originals at once — hand them document by document for verification</li>
<li>Keep a written list of what you submitted (as backup if anything is misplaced)</li>
<li>Ask for a receipt or acknowledgment of documents submitted</li>
<li>If rejected for any document, immediately ask for clarification in writing</li>
<li>Do not argue if a document is rejected — file an appeal as instructed</li>
</ul>

<p>Document verification determines whether your success in written exams translates into a job offer. Meticulous preparation weeks in advance prevents last-minute panic and rejections.</p>
""",
    },
    {
        'title': '7th Pay Commission In-Hand Salary for Pay Level 4 to Level 7: Full Breakdown with Deductions',
        'slug': '7th-pay-commission-in-hand-salary-level-4-to-7',
        'category': 'career',
        'published_date': datetime.date(2026, 10, 25),
        'excerpt': 'What a central government employee at Pay Level 4, 5, 6 or 7 actually takes home each month: basic pay, DA, HRA and transport allowance, minus NPS, CGHS and CGEGIS, with the formula to recalculate when DA changes.',
        'meta_description': 'In-hand salary for 7th CPC Pay Level 4, 5, 6 and 7: basic pay, DA, HRA, TA and deductions explained, with X and Z city examples and the formula.',
        'content': """<p>Job notifications mention a pay level, such as "Pay Level 7 (₹44,900 – ₹1,42,400)", but that range says little about what reaches your bank account. The first salary slip usually surprises new joiners in both directions: the gross is higher than the basic pay because of allowances, and the in-hand is lower than the gross because of deductions. This guide works through the numbers for Pay Levels 4 to 7, the levels of most SSC CGL, CHSL and similar Group B and C posts.</p>

<h2>Which Posts Fall in Levels 4 to 7?</h2>
<p>The pay level is always printed in the notification against each post. As a rough guide from recent SSC notifications:</p>
<ul>
<li><strong>Level 4 (starting basic ₹25,500):</strong> Postal / Sorting Assistant, Tax Assistant, Upper Division Clerk, Data Entry Operator (some departments)</li>
<li><strong>Level 5 (₹29,200):</strong> Auditor, Accountant, Junior Accountant</li>
<li><strong>Level 6 (₹35,400):</strong> Junior Statistical Officer, Sub-Inspector in CBI, Divisional Accountant</li>
<li><strong>Level 7 (₹44,900):</strong> Assistant Section Officer, Inspector (Income Tax / Central GST / Customs), Assistant Enforcement Officer</li>
</ul>
<p>The same post can sit at different levels in different departments, so always confirm the level in the official notification for your post.</p>

<h2>The Components of Your Salary</h2>

<h3>1. Basic Pay</h3>
<p>Every new joiner starts at the first cell of their level in the 7th CPC pay matrix: ₹25,500 for Level 4, ₹29,200 for Level 5, ₹35,400 for Level 6 and ₹44,900 for Level 7. Basic pay rises by one cell (about 3%) at each annual increment, which falls on 1 January or 1 July. Almost every other component is calculated from the basic, so it is the number that matters most.</p>

<h3>2. Dearness Allowance (DA)</h3>
<p>DA compensates for inflation and is a percentage of basic pay. The government revises it twice a year, effective January and July, usually announcing the change a few months late with arrears. <strong>The examples below use 63%</strong>, the rate in effect from 1 July 2026 (it was 58% from July 2025 and 60% from January 2026). If the rate has changed when you read this, recalculate with the formula at the end of this guide.</p>

<h3>3. House Rent Allowance (HRA)</h3>
<p>HRA depends on the city you are posted in. Since DA crossed 50% in January 2024, the rates are:</p>
<ul>
<li><strong>X cities</strong> (Delhi, Mumbai, Kolkata, Chennai, Bengaluru, Hyderabad, Ahmedabad, Pune): 30% of basic</li>
<li><strong>Y cities</strong> (most other large cities and state capitals): 20% of basic</li>
<li><strong>Z cities</strong> (all other places): 10% of basic</li>
</ul>
<p>You do not get HRA if you live in government accommodation; instead, a licence fee is deducted.</p>

<h3>4. Transport Allowance (TA)</h3>
<p>For Levels 3 to 8, TA is ₹3,600 a month in the larger cities on the government's transport allowance list, and ₹1,800 elsewhere. DA is paid on TA too, so at 63% DA the actual amounts are ₹5,868 and ₹2,934.</p>

<h2>The Deductions</h2>
<ul>
<li><strong>Pension contribution:</strong> under NPS, 10% of (basic + DA) is deducted, and the government adds 14% to your pension account. Employees who opt for the Unified Pension Scheme (UPS), available from April 2025, also contribute 10%, with a higher government share. The deduction from your salary is the same either way.</li>
<li><strong>CGHS:</strong> in cities covered by the Central Government Health Scheme, a monthly subscription is deducted: ₹250 for Levels 1 to 5, ₹450 for Level 6 and ₹650 for Levels 7 to 11.</li>
<li><strong>CGEGIS (group insurance):</strong> ₹30 a month for Group C posts and ₹60 for Group B posts.</li>
<li><strong>Income tax:</strong> covered in its own section below.</li>
</ul>

<h2>Monthly Salary: X City (Highest HRA and TA)</h2>
<table>
<thead><tr><th>Component</th><th>Level 4</th><th>Level 5</th><th>Level 6</th><th>Level 7</th></tr></thead>
<tbody>
<tr><td>Basic pay</td><td>₹25,500</td><td>₹29,200</td><td>₹35,400</td><td>₹44,900</td></tr>
<tr><td>DA (63%)</td><td>₹16,065</td><td>₹18,396</td><td>₹22,302</td><td>₹28,287</td></tr>
<tr><td>HRA (30%)</td><td>₹7,650</td><td>₹8,760</td><td>₹10,620</td><td>₹13,470</td></tr>
<tr><td>TA + DA on TA</td><td>₹5,868</td><td>₹5,868</td><td>₹5,868</td><td>₹5,868</td></tr>
<tr><td><strong>Gross</strong></td><td><strong>₹55,083</strong></td><td><strong>₹62,224</strong></td><td><strong>₹74,190</strong></td><td><strong>₹92,525</strong></td></tr>
<tr><td>NPS (10% of basic + DA)</td><td>₹4,157</td><td>₹4,760</td><td>₹5,770</td><td>₹7,319</td></tr>
<tr><td>CGHS</td><td>₹250</td><td>₹250</td><td>₹450</td><td>₹650</td></tr>
<tr><td>CGEGIS</td><td>₹30</td><td>₹30</td><td>₹30</td><td>₹60</td></tr>
<tr><td><strong>In-hand (before income tax)</strong></td><td><strong>₹50,646</strong></td><td><strong>₹57,184</strong></td><td><strong>₹67,940</strong></td><td><strong>₹84,496</strong></td></tr>
</tbody>
</table>

<h2>Monthly Salary: Z City (Lowest HRA and TA)</h2>
<table>
<thead><tr><th>Component</th><th>Level 4</th><th>Level 5</th><th>Level 6</th><th>Level 7</th></tr></thead>
<tbody>
<tr><td>Basic + DA</td><td>₹41,565</td><td>₹47,596</td><td>₹57,702</td><td>₹73,187</td></tr>
<tr><td>HRA (10%)</td><td>₹2,550</td><td>₹2,920</td><td>₹3,540</td><td>₹4,490</td></tr>
<tr><td>TA + DA on TA</td><td>₹2,934</td><td>₹2,934</td><td>₹2,934</td><td>₹2,934</td></tr>
<tr><td><strong>Gross</strong></td><td><strong>₹47,049</strong></td><td><strong>₹53,450</strong></td><td><strong>₹64,176</strong></td><td><strong>₹80,611</strong></td></tr>
<tr><td>Total deductions</td><td>₹4,437</td><td>₹5,040</td><td>₹6,250</td><td>₹8,029</td></tr>
<tr><td><strong>In-hand (before income tax)</strong></td><td><strong>₹42,612</strong></td><td><strong>₹48,410</strong></td><td><strong>₹57,926</strong></td><td><strong>₹72,582</strong></td></tr>
</tbody>
</table>
<p>The Z city figures assume CGHS is deducted; in places without CGHS cover there is no CGHS deduction, so the in-hand pay is slightly higher. Y city salaries fall between the two tables, with the TA depending on whether the city is on the transport allowance list.</p>

<h2>Is Income Tax Deducted?</h2>
<p>Under the new tax regime, which Budget 2026 left unchanged for FY 2026-27, salaried income up to ₹12.75 lakh a year (₹12 lakh plus the ₹75,000 standard deduction) attracts no tax because of the Section 87A rebate. Even the highest example above, Level 7 in an X city, comes to about ₹11.1 lakh a year in gross pay, so a new joiner at any of these levels pays no income tax in the first year under the new regime. That changes as DA and increments rise, so check each year, especially at Level 7.</p>

<h2>Recalculate It Yourself When DA Changes</h2>
<ol>
<li>DA = basic × current DA rate</li>
<li>HRA = basic × 30%, 20% or 10% depending on your city</li>
<li>TA = ₹3,600 or ₹1,800, plus the same DA percentage on it</li>
<li>Gross = basic + DA + HRA + TA</li>
<li>Deductions = 10% of (basic + DA) + CGHS + CGEGIS</li>
<li>In-hand = gross − deductions − any income tax</li>
</ol>
<p>Each 2% rise in DA adds roughly ₹500 (Level 4) to ₹900 (Level 7) to your gross each month, and the pension deduction rises by about a tenth of that.</p>

<h2>What About the 8th Pay Commission?</h2>
<p>The 8th Pay Commission has been set up to revise central government pay, but its recommendations had not been implemented at the time of writing. When they are, the pay matrix will be replaced and DA will typically reset to zero on a higher basic. Until then, the 7th CPC figures above are what employees are paid. Treat any "8th Pay Commission salary" figures you see online as estimates until an official notification is issued.</p>

<p><em>The figures in this guide are worked examples, not official numbers. Your department's pay slip and the official pay matrix are the final authority.</em></p>
""",
    },
    {
        'title': 'How to Read a Government Job Notification: A Section-by-Section Walkthrough',
        'slug': 'how-to-read-government-job-notification',
        'category': 'exam-guide',
        'published_date': datetime.date(2026, 10, 25),
        'excerpt': 'A government job notification can run to 30 pages. Here is what each section means, which lines decide whether you are eligible, and the details candidates most often miss.',
        'meta_description': 'How to read a sarkari job notification: vacancy tables, age and qualification cut-off dates, reservation, fees, selection process and common mistakes.',
        'content': """<p>Every government recruitment begins with an official notification, sometimes called an advertisement or information bulletin. It is a legal document: if you are found ineligible under its terms at any stage, even after selection, your candidature can be cancelled. Yet most candidates only skim the important dates and the fee. This guide walks through a typical notification section by section and points out the lines that actually decide your eligibility.</p>

<h2>1. Advertisement Number and Date</h2>
<p>At the top you will find an advertisement number, for example "Advt. No. 03/2026", and the date of publication. Note both down. You will need the number on application forms and in any correspondence, and the date matters because some eligibility conditions are counted from it. Always download the notification from the recruiting body's official website, not from a forwarded PDF, because corrigenda (corrections) are published there.</p>

<h2>2. Important Dates</h2>
<p>Look for three or four separate dates, not one:</p>
<ul>
<li>Opening date of online applications</li>
<li>Closing date for applications, often with a time such as 11 PM</li>
<li>Last date for fee payment, which can be a day or two after the closing date</li>
<li>Correction window dates, if the body allows edits after submission</li>
</ul>
<p>Exam dates are usually marked "tentative". Treat them as a planning guide, not a promise.</p>

<h2>3. Vacancy Details</h2>
<p>The vacancy table lists posts with category-wise numbers, usually in columns such as UR (unreserved), OBC, SC, ST and EWS, plus horizontal categories such as PwBD (persons with disabilities) and ESM (ex-servicemen). Two points are often misunderstood:</p>
<ul>
<li><strong>Vacancies are often "tentative".</strong> The final number can rise or fall before results.</li>
<li><strong>Horizontal reservation cuts across categories.</strong> A PwBD vacancy is not extra; it is counted within the UR, OBC, SC, ST or EWS seats.</li>
</ul>
<p>Check the pay level printed for each post. Two posts in the same exam can have very different salaries.</p>

<h2>4. Age Limit and the "As On" Date</h2>
<p>This is the most common reason for rejection. The notification gives a minimum and maximum age <strong>as on a specific date</strong>, for example "18–27 years as on 01-01-2026". That date is often neither the notification date nor the closing date. Work out your age on that exact date, and check whether the notification states a range of birth dates (for example, "born not earlier than 02-01-1999 and not later than 01-01-2008"), which removes any doubt.</p>
<p>Age relaxation for reserved categories is listed in a separate table. Relaxation only applies if you hold a valid certificate in the format the notification prescribes.</p>

<h2>5. Educational Qualification</h2>
<p>Read three things carefully:</p>
<ul>
<li><strong>The cut-off date for qualification.</strong> Usually you must hold the qualification by the closing date. Final-year students may or may not be allowed; the notification says so explicitly.</li>
<li><strong>Essential versus desirable qualifications.</strong> Essential ones are mandatory. Desirable ones may only help in shortlisting.</li>
<li><strong>Subject conditions.</strong> Some posts within the same exam need a specific subject, such as Statistics at graduation level.</li>
</ul>
<p>"Equivalent" qualifications are accepted only if the notification or a government order says so. If you have an unusual degree, check before applying, not after selection.</p>

<h2>6. Application Fee</h2>
<p>The fee table lists who pays and who is exempt. Women, SC/ST, PwBD and ex-servicemen candidates are commonly exempt, but this varies by recruiting body. Keep the payment receipt or transaction ID: if the payment fails but money is debited, you will need it to raise a complaint.</p>

<h2>7. Selection Process and Exam Pattern</h2>
<p>This section lists every stage, such as a computer-based test, typing or skill test, physical test, interview and document verification, and tells you which stages are qualifying only and which count towards the final merit. It also states whether there is negative marking and how marks are normalised across shifts. Your preparation plan should start from this section.</p>

<h2>8. Reservation Certificates</h2>
<p>If you are applying under OBC, EWS, SC, ST or PwBD, the notification specifies the certificate format and, often, the date by which it must have been issued. OBC candidates applying for central government posts need an OBC (Non-Creamy Layer) certificate in the central government format; a state OBC certificate may not be accepted. EWS certificates usually have to be for the correct financial year. Many selected candidates lose their seat at document verification because of an outdated or wrongly formatted certificate.</p>

<h2>9. How to Apply</h2>
<p>This section explains registration, photo and signature sizes, and any upload requirements. Prepare scanned documents in the exact sizes and formats requested before you start the form. Read the declaration before you submit; it is legally binding.</p>

<h2>10. General Instructions and Corrigenda</h2>
<p>The final pages cover rules on multiple applications, use of unfair means, and the authority's right to cancel the recruitment. After you apply, check the official website every week or so for corrigenda. They can change vacancies, dates or even eligibility, and they apply to you whether or not you have seen them.</p>

<h2>A Quick Checklist Before You Apply</h2>
<ul>
<li>Downloaded from the official website, and checked for corrigenda</li>
<li>Age calculated on the exact "as on" date</li>
<li>Qualification held by the required date, with any subject conditions met</li>
<li>Category certificate in the right format and validity period</li>
<li>Pay level and posting conditions of the post understood</li>
<li>Fee, closing date and closing time noted</li>
</ul>

<p>Ten minutes spent reading the notification properly can save months of preparation for an exam you were never eligible for. When in doubt, the notification itself and the recruiting body's helpline are the final authority, not coaching material or social media summaries.</p>
""",
    },
]


class Command(BaseCommand):
    help = 'Add 15 additional high-quality articles for AdSense content'

    def handle(self, *args, **options):
        created = 0
        for data in ADDITIONAL_ARTICLES:
            obj, was_created = upsert(Article, 
                slug=data['slug'],
                defaults={
                    'title': data['title'],
                    'category': data['category'],
                    'published_date': data['published_date'],
                    'excerpt': data['excerpt'],
                    'meta_description': data['meta_description'],
                    'content': data['content'].strip(),
                },
            )
            if was_created:
                created += 1
                self.stdout.write(f'  Created: {obj.title[:60]}')
            else:
                self.stdout.write(f'  Updated: {obj.title[:60]}')

        self.stdout.write(self.style.SUCCESS(
            f'\nCompleted. {created} new articles created, {len(ADDITIONAL_ARTICLES) - created} updated.'
        ))
