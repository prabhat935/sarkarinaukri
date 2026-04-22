# TESTING GUIDE: SarkariNaukri Website
## Comprehensive Testing Based on Requirements Specification

This guide provides end-to-end testing procedures for the SarkariNaukri website clone, covering all requirements from the specification.

---

## 1. PRE-TESTING SETUP

### Database Setup
```bash
# If using PostgreSQL (production)
createdb sarkarinaukri
# Set environment variables: PGDATABASE, PGUSER, PGPASSWORD

# Or switch to SQLite for testing (temporary)
# Edit sarkarinaukri/settings/base.py DATABASES to use sqlite3
```

### Install Dependencies & Migrate
```bash
cd sarkarinaukri
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
```

### Load Initial Data
```bash
python manage.py import_initial_data
```

### Start Server
```bash
python manage.py runserver
# Access at http://127.0.0.1:8000
```

---

## 2. FUNCTIONAL TESTING

### 2.1 Content Management Testing

**Test Admin Panel Access:**
- Navigate to `/admin/`
- Login with superuser credentials
- Verify dashboard loads
- Check all models are accessible: Organizations, Exam Categories, Job Postings, etc.

**Test Content Publishing:**
- Create a new Job Posting via admin
- Fill all fields: title, description, organization, category, vacancies, etc.
- Save and verify it appears on frontend
- Test Admit Card and Result publishing similarly

**Test CRUD Operations:**
- Create, Read, Update, Delete operations for all content types
- Verify slug generation and uniqueness
- Test image uploads for organization logos

### 2.2 Search & Filters Testing

**Basic Search:**
- Use search bar on homepage
- Search by exam name (e.g., "SSC CGL")
- Verify relevant results appear
- Test case-insensitive search

**Advanced Filters:**
- Test category filter (Bank, Police, Teaching)
- Test date range filters
- Test state-wise filtering
- Test organization filter
- Verify filter combinations work

**Search Results:**
- Check pagination (if implemented)
- Verify result sorting (newest first)
- Test search highlighting

### 2.3 User Accounts Testing (Optional)

**Registration:**
- Access registration page
- Create new user account
- Verify email confirmation (if implemented)
- Test login/logout

**Personalized Alerts:**
- Login as user
- Subscribe to exam categories
- Verify notification preferences save
- Test alert delivery (email/console)

### 2.4 Navigation Testing

**Menu Navigation:**
- Test all main menus: Jobs, Results, Admit Cards, Syllabus
- Verify dropdowns work on mobile
- Test breadcrumb navigation
- Check 404/500 error pages

**Responsive Design:**
- Test on different screen sizes
- Verify mobile menu functionality
- Check touch interactions

---

## 3. PERFORMANCE TESTING

### 3.1 Load Testing

**Tools Needed:**
- Apache Bench (ab) or Locust
- JMeter for complex scenarios

**Basic Load Test:**
```bash
# Install Apache Bench
# Test 100 requests with 10 concurrent
ab -n 100 -c 10 http://127.0.0.1:8000/

# Test search endpoint
ab -n 50 -c 5 http://127.0.0.1:8000/search/?q=ssc
```

**Traffic Spike Simulation:**
- Test during "result announcement" scenarios
- Monitor response times under load
- Check database connection pooling

### 3.2 Caching & CDN Testing

**Cache Testing:**
- Enable Django caching in settings
- Test page load times with/without cache
- Verify cache invalidation on content updates

**Static Files:**
- Check static file serving
- Test CDN integration (if implemented)
- Verify compression (gzip)

### 3.3 Database Performance

**Query Optimization:**
- Use Django Debug Toolbar
- Check query counts on listing pages
- Test database indexes effectiveness
- Monitor slow queries

---

## 4. SEO TESTING

### 4.1 On-Page SEO Validation

**Meta Tags Testing:**
```python
# Use this script to check meta tags
import requests
from bs4 import BeautifulSoup

url = "http://127.0.0.1:8000/job/ssc-cgl-2024/"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Check title
title = soup.find('title').text
print(f"Title: {title}")

# Check meta description
meta_desc = soup.find('meta', attrs={'name': 'description'})
print(f"Meta Description: {meta_desc['content'] if meta_desc else 'Missing'}")

# Check canonical URL
canonical = soup.find('link', attrs={'rel': 'canonical'})
print(f"Canonical: {canonical['href'] if canonical else 'Missing'}")
```

**Schema Markup Testing:**
- Use Google's Rich Results Test tool
- Test JobPosting schema
- Verify structured data for results/admit cards
- Check Organization schema

**Keyword Optimization:**
- Test keyword density in content
- Verify H1/H2 tags
- Check alt text on images
- Test URL structure and slugs

### 4.2 Technical SEO

**Page Speed:**
- Use Google PageSpeed Insights
- Test Core Web Vitals
- Check mobile performance
- Verify image optimization

**Sitemap & Robots:**
- Test `/sitemap.xml`
- Check `/robots.txt`
- Verify XML sitemap submission
- Test crawlability

### 4.3 Analytics Integration

**Google Analytics:**
- Verify GA tracking code
- Test event tracking
- Check real-time visitors
- Test goal conversions

**Search Console:**
- Submit sitemap
- Check indexing status
- Monitor search performance
- Test rich snippets

---

## 5. SECURITY TESTING

### 5.1 Basic Security Checks

**SSL Testing:**
```bash
# Test SSL certificate (in production)
openssl s_client -connect yourdomain.com:443
# Check certificate validity
```

**SQL Injection Testing:**
- Test search parameters: `?q=' OR '1'='1`
- Test form inputs with malicious SQL
- Verify Django's ORM protection

**XSS Testing:**
- Test comment fields (if any) with `<script>alert('xss')</script>`
- Check input sanitization
- Test reflected/stored XSS

**CSRF Protection:**
- Test form submissions without CSRF tokens
- Verify token validation
- Check AJAX requests

### 5.2 Penetration Testing

**Automated Tools:**
```bash
# Use OWASP ZAP or Burp Suite
# Scan for vulnerabilities
zap.sh -cmd -quickurl http://127.0.0.1:8000 -quickout report.html
```

**Manual Testing:**
- Test authentication bypass
- Check file upload vulnerabilities
- Test directory traversal
- Verify error handling doesn't leak info

### 5.3 Access Control

**Admin Panel Security:**
- Test unauthorized access to `/admin/`
- Verify permission levels
- Check session management
- Test password policies

---

## 6. ACCESSIBILITY TESTING

### 6.1 WCAG Compliance

**Automated Testing:**
- Use WAVE Web Accessibility Tool
- Test with axe DevTools
- Check color contrast
- Verify keyboard navigation

**Manual Testing:**
- Navigate with keyboard only
- Test screen reader compatibility
- Check focus indicators
- Verify alt text presence

---

## 7. CROSS-BROWSER TESTING

### 7.1 Browser Compatibility

**Test Matrix:**
- Chrome (latest)
- Firefox (latest)
- Safari (latest)
- Edge (latest)
- Mobile browsers (iOS Safari, Chrome Android)

**Key Tests:**
- Form functionality
- JavaScript features
- CSS rendering
- Responsive design

---

## 8. INTEGRATION TESTING

### 8.1 Email Notifications

**Email Testing:**
```python
# Test email sending
from django.core.mail import send_mail
send_mail(
    'Test Subject',
    'Test message',
    'from@example.com',
    ['to@example.com'],
    fail_silently=False,
)
```

**SMS Integration (if implemented):**
- Test SMS sending via API
- Verify delivery
- Check rate limiting

### 8.2 External APIs

**Test Third-party Integrations:**
- Payment gateways (if monetized)
- Social media sharing
- Analytics APIs
- CDN services

---

## 9. REGRESSION TESTING

### 9.1 Automated Test Suite

**Django Testing:**
```bash
# Run Django tests
python manage.py test

# Run with coverage
coverage run manage.py test
coverage report
```

**Create Test Cases:**
```python
# content/tests.py
from django.test import TestCase
from .models import JobPosting

class JobPostingTest(TestCase):
    def test_job_creation(self):
        job = JobPosting.objects.create(
            title="Test Job",
            description="Test description",
            # ... other fields
        )
        self.assertEqual(job.title, "Test Job")
```

---

## 10. PRODUCTION TESTING

### 10.1 Deployment Testing

**Staging Environment:**
- Deploy to staging server
- Test all functionality
- Verify environment variables
- Check log files

**Production Checks:**
- Test SSL certificate
- Verify domain configuration
- Check backup systems
- Test monitoring alerts

### 10.2 Monitoring Setup

**Uptime Monitoring:**
- Set up monitoring service (UptimeRobot, Pingdom)
- Test alert notifications
- Verify response times

**Error Logging:**
- Check error logging (Sentry, LogRocket)
- Test error reporting
- Verify log rotation

---

## 11. PERFORMANCE METRICS

### Target Benchmarks:
- Page load time: < 3 seconds
- Time to First Byte: < 1 second
- Search response: < 500ms
- Concurrent users: 1000+
- Uptime: 99.9%

### Monitoring Tools:
- Google Analytics
- Google Search Console
- Server monitoring (New Relic, DataDog)
- Database monitoring

---

## 12. TESTING CHECKLIST SUMMARY

- [ ] Functional testing complete
- [ ] Performance benchmarks met
- [ ] SEO validation passed
- [ ] Security vulnerabilities addressed
- [ ] Accessibility compliant
- [ ] Cross-browser compatible
- [ ] Integration tests passed
- [ ] Regression tests automated
- [ ] Production deployment tested
- [ ] Monitoring configured

---

## 13. TOOLS RECOMMENDED

**Testing Tools:**
- Selenium (browser automation)
- Postman (API testing)
- JMeter (load testing)
- OWASP ZAP (security)
- Lighthouse (performance)
- WAVE (accessibility)

**Monitoring:**
- Google Analytics
- Google Search Console
- Sentry (error tracking)
- UptimeRobot (monitoring)

This comprehensive testing guide ensures your SarkariNaukri clone meets all specification requirements and is ready for production deployment.