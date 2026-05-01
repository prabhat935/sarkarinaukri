/* Sarkari Naukri Main JavaScript */

(function() {
    'use strict';

    // Initialize when DOM is ready
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', init);
    } else {
        init();
    }

    function init() {
        console.log('Sarkari Naukri initialized');
        setupEventListeners();
        setupNavigationToggle();
        setupSmoothScroll();
    }

    // Setup event listeners
    function setupEventListeners() {
        // Close alerts after 5 seconds
        const alerts = document.querySelectorAll('[class*="alert"]');
        alerts.forEach(alert => {
            setTimeout(() => {
                alert.style.display = 'none';
            }, 5000);
        });
    }

    // Toggle navigation on mobile
    function setupNavigationToggle() {
        const nav = document.querySelector('nav');
        if (!nav) return;

        // Create toggle button if not exists
        let toggleBtn = document.querySelector('.nav-toggle');
        if (!toggleBtn) {
            toggleBtn = document.createElement('button');
            toggleBtn.className = 'nav-toggle';
            toggleBtn.innerHTML = '☰';
            toggleBtn.style.display = 'none';
            toggleBtn.style.background = 'none';
            toggleBtn.style.border = 'none';
            toggleBtn.style.color = 'white';
            toggleBtn.style.fontSize = '1.5rem';
            toggleBtn.style.cursor = 'pointer';
            nav.parentElement.insertBefore(toggleBtn, nav);
        }

        toggleBtn.addEventListener('click', function() {
            nav.style.display = nav.style.display === 'none' ? 'flex' : 'none';
        });

        // Show toggle on mobile
        if (window.innerWidth <= 768) {
            toggleBtn.style.display = 'block';
            nav.style.display = 'none';
        }

        window.addEventListener('resize', function() {
            if (window.innerWidth > 768) {
                toggleBtn.style.display = 'none';
                nav.style.display = 'flex';
            } else {
                toggleBtn.style.display = 'block';
            }
        });
    }

    // Smooth scroll for anchor links
    function setupSmoothScroll() {
        document.querySelectorAll('a[href^="#"]').forEach(anchor => {
            anchor.addEventListener('click', function(e) {
                const href = this.getAttribute('href');
                if (href === '#') return;

                e.preventDefault();
                const target = document.querySelector(href);
                if (target) {
                    target.scrollIntoView({
                        behavior: 'smooth',
                        block: 'start'
                    });
                }
            });
        });
    }

    // Utility function to format date
    window.formatDate = function(dateString) {
        const date = new Date(dateString);
        return date.toLocaleDateString('en-IN', {
            year: 'numeric',
            month: 'long',
            day: 'numeric'
        });
    };

    // Utility function to calculate days remaining
    window.daysRemaining = function(endDate) {
        const today = new Date();
        const end = new Date(endDate);
        const diff = end - today;
        return Math.ceil(diff / (1000 * 60 * 60 * 24));
    };

})();
