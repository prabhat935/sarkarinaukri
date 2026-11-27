/* Typing test used by the English and Hindi typing test pages.
   The page sets window.TYPING_TEST = { passages: [...], target: 35, language: 'English' }. */
(function () {
    var cfg = window.TYPING_TEST || {};
    var PASSAGES = cfg.passages || [];
    var TARGET = cfg.target || 35;
    var LANG = cfg.language || 'English';
    var MARGIN = Math.round(TARGET * 1.2);
    var $ = function (id) { return document.getElementById(id); };
    var words = [], start = null, timer = null, ended = false, minutes = 10;

    // Hindi text can be typed in different but equivalent Unicode orders, so compare normalised forms
    function norm(s) { return s.normalize ? s.normalize('NFC') : s; }
    function esc(s) { return s.replace(/&/g, '&amp;').replace(/</g, '&lt;'); }

    function score(final) {
        var typed = norm($('tt-input').value);
        var tw = typed.trim() ? typed.trim().split(/\s+/) : [];
        // While typing, the last word may be unfinished, so it is not judged yet
        var judged = final || /\s$/.test(typed) ? tw.length : Math.max(0, tw.length - 1);
        var correct = 0, chars = 0;
        for (var i = 0; i < judged; i++) {
            if (tw[i] === words[i]) { correct++; chars += words[i].length + 1; }
        }
        var elapsed = start ? Math.max(1, (Date.now() - start) / 1000) : 0;
        var mins = elapsed / 60;
        return {
            tw: tw, judged: judged, correct: correct,
            net: mins ? chars / 5 / mins : 0,
            kdph: mins ? typed.length / mins * 60 : 0,
            acc: judged ? correct / judged * 100 : 100,
            elapsed: elapsed
        };
    }

    function paint(s) {
        var h = '';
        for (var i = 0; i < words.length; i++) {
            var cls = i < s.judged ? (s.tw[i] === words[i] ? 'ok' : 'bad') : (i === s.judged ? 'cur' : '');
            h += (cls ? '<span class="' + cls + '">' : '<span>') + esc(words[i]) + '</span> ';
        }
        $('tt-passage').innerHTML = h;
        var cur = $('tt-passage').querySelector('.cur');
        if (cur) {
            var box = $('tt-passage');
            if (cur.offsetTop - box.offsetTop > box.scrollTop + box.clientHeight - 40) box.scrollTop = cur.offsetTop - box.offsetTop - 40;
        }
    }

    function show(s) {
        $('tt-net').textContent = Math.round(s.net);
        $('tt-kdph').textContent = Math.round(s.kdph).toLocaleString('en-IN');
        $('tt-acc').textContent = Math.round(s.acc) + '%';
        paint(s);
    }

    function tick() {
        var s = score(false);
        var left = Math.max(0, minutes * 60 - s.elapsed);
        $('tt-left').textContent = Math.floor(left / 60) + ':' + ('0' + Math.floor(left % 60)).slice(-2);
        show(s);
        if (start && left <= 0) finish();
    }

    function finish() {
        if (ended || !start) return;
        ended = true; clearInterval(timer);
        $('tt-input').disabled = true;
        var s = score(true);
        show(s);
        var pass = s.net >= TARGET;
        var h = '<div class="verdict ' + (pass ? 'ok' : 'no') + '">Net ' + s.net.toFixed(1) + ' WPM: ' +
            (pass ? 'above' : 'below') + ' the ' + TARGET + ' WPM ' + LANG + ' standard</div>';
        h += '<div class="res-row"><span>Time taken</span><span>' + Math.floor(s.elapsed / 60) + ' min ' + Math.round(s.elapsed % 60) + ' s</span></div>';
        h += '<div class="res-row"><span>Words typed / correct</span><span>' + s.judged + ' / ' + s.correct + '</span></div>';
        h += '<div class="res-row"><span>' + (LANG === 'English' ? 'Key depressions per hour' : 'Characters per hour') + '</span><span>' + Math.round(s.kdph).toLocaleString('en-IN') + '</span></div>';
        h += '<div class="res-row"><span>Word accuracy</span><span>' + s.acc.toFixed(1) + '%</span></div>';
        h += '<div class="res-note">' + (pass && s.net < MARGIN
            ? 'You are above the line but with little margin. Aim for about ' + MARGIN + ' WPM so exam nerves do not pull you below ' + TARGET + '.'
            : pass ? 'Good margin. Keep practising full 10-minute tests to hold this speed for the whole exam.'
                   : 'Keep going: daily practice of 30 to 45 minutes usually adds several WPM a month. Focus on accuracy first.') +
            ' This is a practice measure; SSC applies its own counting rules.</div>';
        $('tt-result').innerHTML = h;
    }

    function reset() {
        clearInterval(timer); start = null; ended = false;
        minutes = +$('tt-time').value;
        words = norm(PASSAGES[+$('tt-pass').value] || '').split(/\s+/);
        $('tt-input').value = ''; $('tt-input').disabled = false;
        $('tt-result').innerHTML = '';
        $('tt-passage').scrollTop = 0;
        tick();
    }

    $('tt-input').addEventListener('input', function () {
        if (ended) return;
        if (!start) { start = Date.now(); timer = setInterval(tick, 500); }
        tick();
        if (score(false).judged >= words.length) finish();
    });
    $('tt-input').addEventListener('paste', function (e) { e.preventDefault(); });
    $('tt-input').addEventListener('drop', function (e) { e.preventDefault(); });
    $('tt-reset').addEventListener('click', reset);
    $('tt-stop').addEventListener('click', finish);
    $('tt-time').addEventListener('change', reset);
    $('tt-pass').addEventListener('change', reset);
    reset();
})();
