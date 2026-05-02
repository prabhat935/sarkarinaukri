(function () {
    'use strict';

    document.readyState === 'loading'
        ? document.addEventListener('DOMContentLoaded', init)
        : init();

    function init() {
        setupMobileNav();
        setupSmoothScroll();
        setupBackToTop();
        setupScrollAnimations();
        setupStatCountUp();
        setupTickerPause();
        autoDismissAlerts();
    }

    /* ── Mobile nav ────────────────────────────────────────────── */
    function setupMobileNav() {
        const hamburger = document.querySelector('.hamburger');
        const navLinks  = document.querySelector('.nav-links');
        if (!hamburger || !navLinks) return;

        hamburger.addEventListener('click', function () {
            const open = navLinks.classList.toggle('open');
            hamburger.setAttribute('aria-expanded', open);
            hamburger.innerHTML = open
                ? '<i class="fas fa-times"></i>'
                : '<i class="fas fa-bars"></i>';
        });

        // Close nav when a link is clicked
        navLinks.querySelectorAll('a').forEach(function (a) {
            a.addEventListener('click', function () {
                navLinks.classList.remove('open');
                hamburger.setAttribute('aria-expanded', 'false');
                hamburger.innerHTML = '<i class="fas fa-bars"></i>';
            });
        });
    }

    /* ── Smooth scroll ─────────────────────────────────────────── */
    function setupSmoothScroll() {
        document.querySelectorAll('a[href^="#"]').forEach(function (a) {
            a.addEventListener('click', function (e) {
                const href = this.getAttribute('href');
                if (href === '#') return;
                const target = document.querySelector(href);
                if (target) {
                    e.preventDefault();
                    target.scrollIntoView({ behavior: 'smooth', block: 'start' });
                }
            });
        });
    }

    /* ── Back-to-top button ────────────────────────────────────── */
    function setupBackToTop() {
        const btn = document.getElementById('back-to-top');
        if (!btn) return;

        window.addEventListener('scroll', function () {
            if (window.scrollY > 400) {
                btn.classList.add('visible');
            } else {
                btn.classList.remove('visible');
            }
        }, { passive: true });

        btn.addEventListener('click', function () {
            window.scrollTo({ top: 0, behavior: 'smooth' });
        });
    }

    /* ── Scroll-reveal animations ──────────────────────────────── */
    function setupScrollAnimations() {
        const items = document.querySelectorAll('.animate-on-scroll');
        if (!items.length) return;

        if (!('IntersectionObserver' in window)) {
            items.forEach(function (el) { el.classList.add('is-visible'); });
            return;
        }

        const observer = new IntersectionObserver(function (entries) {
            entries.forEach(function (entry) {
                if (entry.isIntersecting) {
                    entry.target.classList.add('is-visible');
                    observer.unobserve(entry.target);
                }
            });
        }, { threshold: 0.12, rootMargin: '0px 0px -40px 0px' });

        items.forEach(function (el) { observer.observe(el); });
    }

    /* ── Stat count-up ─────────────────────────────────────────── */
    function setupStatCountUp() {
        const stats = document.querySelectorAll('.stat-number[data-target]');
        if (!stats.length) return;

        if (!('IntersectionObserver' in window)) {
            stats.forEach(function (el) {
                el.textContent = el.dataset.target + (el.dataset.suffix || '');
            });
            return;
        }

        const observer = new IntersectionObserver(function (entries) {
            entries.forEach(function (entry) {
                if (!entry.isIntersecting) return;
                observer.unobserve(entry.target);
                countUp(entry.target);
            });
        }, { threshold: 0.5 });

        stats.forEach(function (el) { observer.observe(el); });
    }

    function countUp(el) {
        const target  = parseInt(el.dataset.target, 10);
        const suffix  = el.dataset.suffix || '';
        const duration = 1600;
        const step    = 16;
        const steps   = duration / step;
        let current   = 0;

        const timer = setInterval(function () {
            current += target / steps;
            if (current >= target) {
                el.textContent = target.toLocaleString('en-IN') + suffix;
                clearInterval(timer);
            } else {
                el.textContent = Math.floor(current).toLocaleString('en-IN') + suffix;
            }
        }, step);
    }

    /* ── Ticker pause on hover ─────────────────────────────────── */
    function setupTickerPause() {
        const ticker = document.querySelector('.ticker-track');
        if (!ticker) return;

        ticker.parentElement.addEventListener('mouseenter', function () {
            ticker.style.animationPlayState = 'paused';
        });
        ticker.parentElement.addEventListener('mouseleave', function () {
            ticker.style.animationPlayState = 'running';
        });
    }

    /* ── Auto-dismiss alerts ───────────────────────────────────── */
    function autoDismissAlerts() {
        document.querySelectorAll('.alert, .messages li').forEach(function (el) {
            setTimeout(function () {
                el.style.transition = 'opacity .4s';
                el.style.opacity = '0';
                setTimeout(function () { el.style.display = 'none'; }, 420);
            }, 5000);
        });
    }

})();
