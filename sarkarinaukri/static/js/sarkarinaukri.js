/* Sarkari Naukri — site-wide JS */

(function () {
    'use strict';

    // Back-to-top button
    var backToTop = document.getElementById('back-to-top');
    if (backToTop) {
        window.addEventListener('scroll', function () {
            if (window.scrollY > 300) {
                backToTop.classList.add('visible');
            } else {
                backToTop.classList.remove('visible');
            }
        });
        backToTop.addEventListener('click', function () {
            window.scrollTo({ top: 0, behavior: 'smooth' });
        });
    }

    // Auto-dismiss Django messages after 5 s
    document.querySelectorAll('.alert.alert-dismissible').forEach(function (el) {
        setTimeout(function () {
            var bsAlert = bootstrap.Alert && bootstrap.Alert.getOrCreateInstance(el);
            if (bsAlert) bsAlert.close();
        }, 5000);
    });

    // Preserve filter params across pagination clicks (list pages)
    document.querySelectorAll('.pagination-nav a.page-link').forEach(function (link) {
        var href = link.getAttribute('href');
        if (!href) return;
        var params = new URLSearchParams(window.location.search);
        var pageMatch = href.match(/[?&]page=(\d+)/);
        if (pageMatch) {
            params.set('page', pageMatch[1]);
            link.setAttribute('href', '?' + params.toString());
        }
    });
})();
