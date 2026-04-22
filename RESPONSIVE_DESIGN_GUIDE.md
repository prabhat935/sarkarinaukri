# Responsive Design Implementation Guide

This guide provides step-by-step instructions to transform your SarkariNaukri website into a modern, responsive, mobile-friendly site.

---

## Phase 1: Setup Bootstrap 5 (1 hour)

### Step 1: Update requirements.txt

Add Bootstrap CDN to your project. Edit `sarkarinaukri/requirements.txt`:

```
Django>=5.2,<6.0
wagtail>=6.0,<7.0
django-haystack
Whoosh
psycopg2-binary
dj-database-url
whitenoise
gunicorn
django-allauth
django-crispy-forms
crispy-bootstrap5  # Already added
```

### Step 2: Update settings.py

Edit `sarkarinaukri/sarkarinaukri/settings/base.py`:

```python
INSTALLED_APPS = [
    "home",
    "search",
    "content",
    "notifications",
    "crispy_forms",           # Add this
    "crispy_bootstrap5",      # Add this
    # ... rest of apps
]

# Add at the end
CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"
CRISPY_TEMPLATE_PACK = "bootstrap5"
```

### Step 3: Update base.html with Bootstrap

Create `sarkarinaukri/sarkarinaukri/templates/base.html`:

```html
{% load static wagtailcore_tags wagtailuserbar %}

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    
    <!-- Title -->
    <title>{% block title %}SarkariNaukri{% endblock %}</title>
    
    <!-- Meta Tags for SEO -->
    <meta name="description" content="{% block meta_description %}Find latest government jobs, exam results, and admit cards{% endblock %}">
    <meta name="keywords" content="{% block meta_keywords %}government jobs, sarkari jobs{% endblock %}">
    <link rel="canonical" href="{{ request.build_absolute_uri }}">
    
    <!-- Bootstrap 5 CSS -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    
    <!-- Font Awesome for Icons -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    
    <!-- Custom CSS -->
    <link rel="stylesheet" href="{% static 'css/sarkarinaukri.css' %}">
    
    {% block extra_css %}{% endblock %}
</head>

<body>
    <!-- Navigation -->
    <nav class="navbar navbar-expand-lg navbar-light bg-light sticky-top border-bottom border-primary border-3">
        <div class="container-lg">
            <a class="navbar-brand fw-bold text-primary" href="{% url 'home' %}">
                <i class="fas fa-briefcase"></i> SarkariNaukri
            </a>
            
            <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav">
                <span class="navbar-toggler-icon"></span>
            </button>
            
            <div class="collapse navbar-collapse" id="navbarNav">
                <ul class="navbar-nav ms-auto">
                    <li class="nav-item">
                        <a class="nav-link" href="{% url 'job_list' %}">Jobs</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="{% url 'result_list' %}">Results</a>
                    </li>
                    <li class="nav-item dropdown">
                        <a class="nav-link dropdown-toggle" href="#" id="moreDropdown" role="button" data-bs-toggle="dropdown">
                            More
                        </a>
                        <ul class="dropdown-menu">
                            <li><a class="dropdown-item" href="{% url 'admit_card_list' %}">Admit Cards</a></li>
                            <li><a class="dropdown-item" href="{% url 'syllabus_list' %}">Syllabus</a></li>
                            <li><a class="dropdown-item" href="{% url 'board_results' %}">Board Results</a></li>
                            <li><a class="dropdown-item" href="{% url 'scholarships' %}">Scholarships</a></li>
                            <li><hr class="dropdown-divider"></li>
                            <li><a class="dropdown-item" href="{% url 'important_notifications' %}">Notifications</a></li>
                        </ul>
                    </li>
                    {% if user.is_authenticated %}
                    <li class="nav-item">
                        <a class="nav-link" href="#">Hi, {{ user.first_name }}</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="{% url 'account_logout' %}">Logout</a>
                    </li>
                    {% else %}
                    <li class="nav-item">
                        <a class="nav-link btn btn-primary text-white ms-2" href="{% url 'account_login' %}">Login</a>
                    </li>
                    {% endif %}
                </ul>
            </div>
        </div>
    </nav>
    
    <!-- Main Content -->
    <main>
        {% block content %}{% endblock %}
    </main>
    
    <!-- Footer -->
    <footer class="bg-dark text-white mt-5">
        <div class="container-lg py-5">
            <div class="row">
                <div class="col-md-3 mb-4 mb-md-0">
                    <h5 class="mb-3">About</h5>
                    <ul class="list-unstyled">
                        <li><a href="#" class="text-decoration-none text-light">About Us</a></li>
                        <li><a href="#" class="text-decoration-none text-light">Contact Us</a></li>
                        <li><a href="#" class="text-decoration-none text-light">Advertise</a></li>
                    </ul>
                </div>
                
                <div class="col-md-3 mb-4 mb-md-0">
                    <h5 class="mb-3">Popular</h5>
                    <ul class="list-unstyled">
                        <li><a href="{% url 'job_list' %}" class="text-decoration-none text-light">Government Jobs</a></li>
                        <li><a href="{% url 'result_list' %}" class="text-decoration-none text-light">Results</a></li>
                        <li><a href="{% url 'admit_card_list' %}" class="text-decoration-none text-light">Admit Cards</a></li>
                    </ul>
                </div>
                
                <div class="col-md-3 mb-4 mb-md-0">
                    <h5 class="mb-3">Legal</h5>
                    <ul class="list-unstyled">
                        <li><a href="#" class="text-decoration-none text-light">Privacy Policy</a></li>
                        <li><a href="#" class="text-decoration-none text-light">Terms & Conditions</a></li>
                        <li><a href="#" class="text-decoration-none text-light">Disclaimer</a></li>
                    </ul>
                </div>
                
                <div class="col-md-3">
                    <h5 class="mb-3">Follow Us</h5>
                    <div class="d-flex gap-2">
                        <a href="#" class="btn btn-sm btn-light"><i class="fab fa-facebook"></i></a>
                        <a href="#" class="btn btn-sm btn-light"><i class="fab fa-twitter"></i></a>
                        <a href="#" class="btn btn-sm btn-light"><i class="fab fa-instagram"></i></a>
                        <a href="#" class="btn btn-sm btn-light"><i class="fab fa-youtube"></i></a>
                    </div>
                </div>
            </div>
            
            <hr class="my-4">
            
            <div class="row">
                <div class="col-md-6 text-center text-md-start">
                    <p class="mb-0">&copy; 2024 SarkariNaukri. All rights reserved.</p>
                </div>
                <div class="col-md-6 text-center text-md-end">
                    <p class="mb-0">We are not affiliated with any official government body.</p>
                </div>
            </div>
        </div>
    </footer>
    
    <!-- Bootstrap 5 JS -->
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
    
    <!-- Custom JS -->
    <script src="{% static 'js/sarkarinaukri.js' %}"></script>
    
    {% block extra_js %}{% endblock %}
</body>
</html>
```

---

## Phase 2: Create Home Page Template (1.5 hours)

Create `sarkarinaukri/home/templates/home/home_page.html`:

```html
{% extends "base.html" %}
{% load static %}

{% block title %}SarkariNaukri - Government Jobs & Results{% endblock %}

{% block meta_description %}Find latest government job notifications, exam results, admit cards, and syllabus updates for SSC, UPSC, Banking, and state jobs.{% endblock %}

{% block content %}

<!-- Hero Section with Search -->
<section class="hero-section bg-gradient text-white py-5">
    <div class="container-lg">
        <div class="row align-items-center">
            <div class="col-lg-6 mb-4 mb-lg-0">
                <h1 class="display-4 fw-bold mb-3">Find Your Dream Government Job</h1>
                <p class="lead mb-4">Latest job notifications, exam results, and admit cards all in one place</p>
                <form method="get" action="{% url 'job_list' %}" class="input-group input-group-lg">
                    <input type="text" class="form-control" name="title" placeholder="Search by job title, exam name...">
                    <button class="btn btn-warning" type="submit">
                        <i class="fas fa-search"></i> Search
                    </button>
                </form>
            </div>
            <div class="col-lg-6">
                <img src="{% static 'images/hero-illustration.png' %}" alt="Government Jobs" class="img-fluid" style="opacity: 0.9;">
            </div>
        </div>
    </div>
</section>

<!-- Quick Stats -->
<section class="py-5 bg-light">
    <div class="container-lg">
        <div class="row text-center">
            <div class="col-md-3 mb-4">
                <div class="stat-card">
                    <h3 class="h2 text-primary fw-bold">5K+</h3>
                    <p class="text-muted">Active Jobs</p>
                </div>
            </div>
            <div class="col-md-3 mb-4">
                <div class="stat-card">
                    <h3 class="h2 text-success fw-bold">500K+</h3>
                    <p class="text-muted">Users</p>
                </div>
            </div>
            <div class="col-md-3 mb-4">
                <div class="stat-card">
                    <h3 class="h2 text-info fw-bold">100+</h3>
                    <p class="text-muted">Exam Types</p>
                </div>
            </div>
            <div class="col-md-3 mb-4">
                <div class="stat-card">
                    <h3 class="h2 text-danger fw-bold">10K+</h3>
                    <p class="text-muted">Results</p>
                </div>
            </div>
        </div>
    </div>
</section>

<!-- Featured Jobs -->
<section class="py-5">
    <div class="container-lg">
        <h2 class="display-6 fw-bold mb-4">
            <i class="fas fa-star text-warning"></i> Featured Jobs
        </h2>
        <div class="row">
            {% for job in featured_jobs|slice:":6" %}
            <div class="col-md-6 col-lg-4 mb-4">
                <div class="card job-card h-100">
                    <div class="card-body">
                        <h5 class="card-title">{{ job.title }}</h5>
                        <p class="card-text text-muted">{{ job.organization.name }}</p>
                        <div class="d-flex justify-content-between align-items-center mb-3">
                            <span class="badge bg-primary">{{ job.job_level }}</span>
                            <span class="badge bg-success">{{ job.vacancies }} Posts</span>
                        </div>
                        <p class="small text-muted mb-3">
                            <i class="fas fa-map-marker-alt"></i> 
                            {% if job.state %}{{ job.state.name }}{% else %}All India{% endif %}
                        </p>
                        <p class="small text-muted mb-3">
                            <i class="fas fa-calendar-alt"></i>
                            Deadline: <strong>{{ job.application_end_date|date:"d M Y" }}</strong>
                        </p>
                        {% if job.days_remaining %}
                        <div class="alert alert-{{ job.days_remaining|add:"0"|slice:"-1" }} py-2 mb-3">
                            {{ job.days_remaining }} days remaining
                        </div>
                        {% endif %}
                        <div class="d-grid gap-2">
                            <a href="{% url 'job_detail' job.pk %}" class="btn btn-primary btn-sm">
                                <i class="fas fa-arrow-right"></i> View Details
                            </a>
                        </div>
                    </div>
                </div>
            </div>
            {% endfor %}
        </div>
        <div class="text-center mt-4">
            <a href="{% url 'job_list' %}" class="btn btn-lg btn-primary">Browse All Jobs</a>
        </div>
    </div>
</section>

<!-- Categories Section -->
<section class="py-5 bg-light">
    <div class="container-lg">
        <h2 class="display-6 fw-bold mb-4">Explore Categories</h2>
        <div class="row">
            <div class="col-6 col-md-4 col-lg-3 mb-4">
                <a href="{% url 'job_list' %}?exam_category=1" class="category-card text-decoration-none">
                    <div class="card category-card-item text-center">
                        <div class="card-body">
                            <i class="fas fa-bank fa-3x text-primary mb-3"></i>
                            <h6>Banking Jobs</h6>
                            <small class="text-muted">250+ Jobs</small>
                        </div>
                    </div>
                </a>
            </div>
            
            <div class="col-6 col-md-4 col-lg-3 mb-4">
                <a href="{% url 'job_list' %}?exam_category=2" class="category-card text-decoration-none">
                    <div class="card category-card-item text-center">
                        <div class="card-body">
                            <i class="fas fa-shield-alt fa-3x text-danger mb-3"></i>
                            <h6>Police Jobs</h6>
                            <small class="text-muted">150+ Jobs</small>
                        </div>
                    </div>
                </a>
            </div>
            
            <div class="col-6 col-md-4 col-lg-3 mb-4">
                <a href="{% url 'job_list' %}?exam_category=3" class="category-card text-decoration-none">
                    <div class="card category-card-item text-center">
                        <div class="card-body">
                            <i class="fas fa-graduation-cap fa-3x text-success mb-3"></i>
                            <h6>Teaching Jobs</h6>
                            <small class="text-muted">300+ Jobs</small>
                        </div>
                    </div>
                </a>
            </div>
            
            <div class="col-6 col-md-4 col-lg-3 mb-4">
                <a href="{% url 'job_list' %}?exam_category=4" class="category-card text-decoration-none">
                    <div class="card category-card-item text-center">
                        <div class="card-body">
                            <i class="fas fa-chart-line fa-3x text-info mb-3"></i>
                            <h6>Railway Jobs</h6>
                            <small class="text-muted">200+ Jobs</small>
                        </div>
                    </div>
                </a>
            </div>
        </div>
    </div>
</section>

<!-- Latest Results -->
<section class="py-5">
    <div class="container-lg">
        <h2 class="display-6 fw-bold mb-4">Latest Results</h2>
        <div class="table-responsive">
            <table class="table table-hover">
                <thead class="table-primary">
                    <tr>
                        <th>Exam Name</th>
                        <th>Organization</th>
                        <th>Year</th>
                        <th>Result Date</th>
                        <th>Action</th>
                    </tr>
                </thead>
                <tbody>
                    {% for result in latest_results|slice:":5" %}
                    <tr>
                        <td><strong>{{ result.exam_name }}</strong></td>
                        <td>{{ result.organization.name }}</td>
                        <td>{{ result.exam_year }}</td>
                        <td>{{ result.result_date|date:"d M Y" }}</td>
                        <td>
                            <a href="#" class="btn btn-sm btn-outline-primary">View</a>
                        </td>
                    </tr>
                    {% endfor %}
                </tbody>
            </table>
        </div>
    </div>
</section>

<!-- CTA Section -->
<section class="py-5 bg-primary text-white">
    <div class="container-lg text-center">
        <h2 class="display-6 fw-bold mb-3">Stay Updated with Job Alerts</h2>
        <p class="lead mb-4">Get instant notifications for jobs matching your profile</p>
        <div class="row justify-content-center">
            <div class="col-md-6">
                <form>
                    <div class="input-group input-group-lg">
                        <input type="email" class="form-control" placeholder="Enter your email" required>
                        <button class="btn btn-warning" type="submit">Subscribe</button>
                    </div>
                </form>
            </div>
        </div>
    </div>
</section>

{% endblock %}

{% block extra_css %}
<style>
    .hero-section {
        background: linear-gradient(135deg, #1e88e5 0%, #039be5 100%);
    }
    
    .stat-card {
        padding: 2rem;
        background: white;
        border-radius: 8px;
        box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
        transition: transform 0.3s;
    }
    
    .stat-card:hover {
        transform: translateY(-5px);
    }
    
    .job-card {
        border: none;
        box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
        transition: all 0.3s;
    }
    
    .job-card:hover {
        box-shadow: 0 4px 16px rgba(0, 0, 0, 0.15);
        transform: translateY(-2px);
    }
    
    .category-card-item {
        border: none;
        box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
        transition: all 0.3s;
        cursor: pointer;
    }
    
    .category-card-item:hover {
        box-shadow: 0 4px 16px rgba(0, 0, 0, 0.15);
        transform: translateY(-5px);
    }
    
    .bg-gradient {
        background: linear-gradient(135deg, #1e88e5 0%, #039be5 100%);
    }
</style>
{% endblock %}
```

---

## Phase 3: Update Job List Template (1 hour)

Create `sarkarinaukri/content/templates/content/job_list.html`:

```html
{% extends "base.html" %}
{% load static %}

{% block title %}Government Jobs - Browse All Listings | SarkariNaukri{% endblock %}

{% block content %}

<div class="container-lg py-5">
    <div class="row">
        <!-- Sidebar Filters -->
        <div class="col-lg-3 mb-4">
            <div class="filter-section">
                <h5 class="filter-title mb-4">
                    <i class="fas fa-filter"></i> Filters
                </h5>
                
                <form method="get" class="filter-form">
                    <!-- Search -->
                    <div class="mb-4">
                        <label class="form-label fw-bold">Search</label>
                        <input type="text" name="title" class="form-control" 
                               placeholder="Job title..." value="{{ request.GET.title }}">
                    </div>
                    
                    <!-- Organization -->
                    <div class="mb-4">
                        <label class="form-label fw-bold">Organization</label>
                        <select name="organization" class="form-select">
                            <option value="">All Organizations</option>
                            {% for org in organizations %}
                            <option value="{{ org.id }}" 
                                    {% if request.GET.organization|slugify == org.id|slugify %}selected{% endif %}>
                                {{ org.name }}
                            </option>
                            {% endfor %}
                        </select>
                    </div>
                    
                    <!-- State -->
                    <div class="mb-4">
                        <label class="form-label fw-bold">State</label>
                        <select name="state" class="form-select">
                            <option value="">All States</option>
                            {% for state in states %}
                            <option value="{{ state.id }}"
                                    {% if request.GET.state|slugify == state.id|slugify %}selected{% endif %}>
                                {{ state.name }}
                            </option>
                            {% endfor %}
                        </select>
                    </div>
                    
                    <!-- Category -->
                    <div class="mb-4">
                        <label class="form-label fw-bold">Category</label>
                        <select name="exam_category" class="form-select">
                            <option value="">All Categories</option>
                            {% for cat in categories %}
                            <option value="{{ cat.id }}"
                                    {% if request.GET.exam_category|slugify == cat.id|slugify %}selected{% endif %}>
                                {{ cat.name }}
                            </option>
                            {% endfor %}
                        </select>
                    </div>
                    
                    <!-- Status -->
                    <div class="mb-4">
                        <label class="form-label fw-bold">Status</label>
                        <div class="form-check">
                            <input type="checkbox" class="form-check-input" name="status" 
                                   value="Active" id="status_active"
                                   {% if request.GET.status == 'Active' %}checked{% endif %}>
                            <label class="form-check-label" for="status_active">Active</label>
                        </div>
                        <div class="form-check">
                            <input type="checkbox" class="form-check-input" name="status" 
                                   value="Closed" id="status_closed"
                                   {% if request.GET.status == 'Closed' %}checked{% endif %}>
                            <label class="form-check-label" for="status_closed">Closed</label>
                        </div>
                    </div>
                    
                    <button type="submit" class="btn btn-primary w-100 mb-2">
                        <i class="fas fa-search"></i> Apply Filters
                    </button>
                    <a href="{% url 'job_list' %}" class="btn btn-outline-secondary w-100">
                        <i class="fas fa-redo"></i> Reset
                    </a>
                </form>
            </div>
        </div>
        
        <!-- Main Content -->
        <div class="col-lg-9">
            <div class="d-flex justify-content-between align-items-center mb-4">
                <h2 class="h4">
                    <i class="fas fa-briefcase text-primary"></i>
                    Government Jobs
                    <small class="text-muted">{{ page_obj.paginator.count }} Total</small>
                </h2>
                
                <div class="dropdown">
                    <button class="btn btn-outline-secondary dropdown-toggle" type="button" 
                            data-bs-toggle="dropdown">
                        Sort By
                    </button>
                    <ul class="dropdown-menu">
                        <li><a class="dropdown-item" href="?sort=-created_at">Newest First</a></li>
                        <li><a class="dropdown-item" href="?sort=application_end_date">Deadline Soon</a></li>
                        <li><a class="dropdown-item" href="?sort=vacancy">Most Vacancies</a></li>
                    </ul>
                </div>
            </div>
            
            <!-- Jobs List -->
            {% if jobs %}
                {% for job in jobs %}
                <div class="card job-card mb-4">
                    <div class="card-body">
                        <div class="row">
                            <div class="col-md-8">
                                <h5 class="card-title mb-2">
                                    <a href="{% url 'job_detail' job.pk %}" class="text-decoration-none">
                                        {{ job.title }}
                                    </a>
                                </h5>
                                <p class="text-muted mb-2">
                                    <strong>{{ job.organization.name }}</strong>
                                </p>
                                <div class="row g-2 mb-3">
                                    <div class="col-auto">
                                        <span class="badge bg-light text-dark">
                                            <i class="fas fa-map-marker-alt"></i>
                                            {% if job.state %}{{ job.state.name }}{% else %}All India{% endif %}
                                        </span>
                                    </div>
                                    <div class="col-auto">
                                        <span class="badge bg-light text-dark">
                                            <i class="fas fa-users"></i>
                                            {{ job.vacancies }} Vacancies
                                        </span>
                                    </div>
                                    <div class="col-auto">
                                        <span class="badge bg-primary">{{ job.job_level }}</span>
                                    </div>
                                </div>
                                
                                <p class="small text-muted mb-0">
                                    <i class="fas fa-calendar"></i>
                                    Application Deadline: <strong>{{ job.application_end_date|date:"d M Y" }}</strong>
                                </p>
                            </div>
                            
                            <div class="col-md-4 d-flex flex-column justify-content-center">
                                {% if job.days_remaining > 0 %}
                                <div class="alert alert-success py-2 mb-2">
                                    <strong>{{ job.days_remaining }}</strong> days left
                                </div>
                                {% elif job.days_remaining == 0 %}
                                <div class="alert alert-danger py-2 mb-2">
                                    Last day to apply
                                </div>
                                {% else %}
                                <div class="alert alert-secondary py-2 mb-2">
                                    Closed
                                </div>
                                {% endif %}
                                
                                <div class="btn-group d-grid gap-2" role="group">
                                    <a href="{% url 'job_detail' job.pk %}" class="btn btn-primary btn-sm">
                                        <i class="fas fa-arrow-right"></i> Details
                                    </a>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
                {% endfor %}
                
                <!-- Pagination -->
                {% if is_paginated %}
                <nav aria-label="Page navigation" class="mt-4">
                    <ul class="pagination justify-content-center">
                        {% if page_obj.has_previous %}
                            <li class="page-item">
                                <a class="page-link" href="?page=1">First</a>
                            </li>
                            <li class="page-item">
                                <a class="page-link" href="?page={{ page_obj.previous_page_number }}">Previous</a>
                            </li>
                        {% endif %}
                        
                        {% for num in page_obj.paginator.page_range %}
                            {% if page_obj.number == num %}
                                <li class="page-item active">
                                    <span class="page-link">{{ num }}</span>
                                </li>
                            {% elif num > page_obj.number|add:'-3' and num < page_obj.number|add:'3' %}
                                <li class="page-item">
                                    <a class="page-link" href="?page={{ num }}">{{ num }}</a>
                                </li>
                            {% endif %}
                        {% endfor %}
                        
                        {% if page_obj.has_next %}
                            <li class="page-item">
                                <a class="page-link" href="?page={{ page_obj.next_page_number }}">Next</a>
                            </li>
                            <li class="page-item">
                                <a class="page-link" href="?page={{ page_obj.paginator.num_pages }}">Last</a>
                            </li>
                        {% endif %}
                    </ul>
                </nav>
                {% endif %}
            {% else %}
                <div class="alert alert-info" role="alert">
                    <i class="fas fa-info-circle"></i> No jobs found matching your criteria.
                    <a href="{% url 'job_list' %}">Clear filters</a> or try different search terms.
                </div>
            {% endif %}
        </div>
    </div>
</div>

{% endblock %}

{% block extra_css %}
<style>
    .job-card {
        border: none;
        box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
        transition: all 0.3s;
    }
    
    .job-card:hover {
        box-shadow: 0 4px 16px rgba(0, 0, 0, 0.15);
    }
    
    .filter-section {
        background: #f8f9fa;
        border: 1px solid #dee2e6;
        border-radius: 8px;
        padding: 1.5rem;
    }
    
    .filter-title {
        border-bottom: 2px solid #1e88e5;
        padding-bottom: 0.5rem;
    }
</style>
{% endblock %}
```

---

## Phase 4: Create Job Detail Template (45 minutes)

Create `sarkarinaukri/content/templates/content/job_detail.html`:

```html
{% extends "base.html" %}

{% block title %}{{ job.title }} - {{ job.organization.name }}{% endblock %}

{% block meta_description %}{{ job.meta_description }}{% endblock %}

{% block content %}

<div class="container-lg py-5">
    <!-- Breadcrumb -->
    <nav aria-label="breadcrumb">
        <ol class="breadcrumb">
            <li class="breadcrumb-item"><a href="/">Home</a></li>
            <li class="breadcrumb-item"><a href="{% url 'job_list' %}">Jobs</a></li>
            <li class="breadcrumb-item active" aria-current="page">{{ job.organization.name }}</li>
        </ol>
    </nav>
    
    <div class="row">
        <!-- Main Content -->
        <div class="col-lg-8 mb-4">
            <!-- Job Header -->
            <div class="card mb-4 border-0 shadow-sm">
                <div class="card-body">
                    <h1 class="h2 mb-2">{{ job.title }}</h1>
                    <p class="lead text-muted mb-3">{{ job.organization.name }}</p>
                    
                    <div class="row mb-4">
                        <div class="col-6 col-md-3 mb-3">
                            <p class="text-muted small mb-1">Vacancies</p>
                            <h5 class="text-primary">{{ job.vacancies }}</h5>
                        </div>
                        <div class="col-6 col-md-3 mb-3">
                            <p class="text-muted small mb-1">Location</p>
                            <h5>{% if job.state %}{{ job.state.name }}{% else %}All India{% endif %}</h5>
                        </div>
                        <div class="col-6 col-md-3 mb-3">
                            <p class="text-muted small mb-1">Job Level</p>
                            <h5>{{ job.job_level }}</h5>
                        </div>
                        <div class="col-6 col-md-3 mb-3">
                            <p class="text-muted small mb-1">Salary</p>
                            <h5>
                                {% if job.salary_min and job.salary_max %}
                                    ₹{{ job.salary_min }} - ₹{{ job.salary_max }}
                                {% elif job.salary_min %}
                                    ₹{{ job.salary_min }}+
                                {% else %}
                                    TBD
                                {% endif %}
                            </h5>
                        </div>
                    </div>
                    
                    <!-- Important Dates Box -->
                    <div class="alert alert-info">
                        <h6 class="mb-3"><i class="fas fa-calendar"></i> Important Dates</h6>
                        <div class="row">
                            <div class="col-md-6">
                                <p class="mb-2">
                                    <strong>Application Start:</strong><br>
                                    {{ job.application_start_date|date:"d M Y" }}
                                </p>
                                <p class="mb-2">
                                    <strong>Application End:</strong><br>
                                    {{ job.application_end_date|date:"d M Y" }}
                                </p>
                            </div>
                            <div class="col-md-6">
                                <p class="mb-2">
                                    <strong>Exam Date:</strong><br>
                                    {{ job.exam_date|date:"d M Y"|default:"TBD" }}
                                </p>
                                <p class="mb-0">
                                    <strong>Result Date:</strong><br>
                                    {{ job.result_date|date:"d M Y"|default:"TBD" }}
                                </p>
                            </div>
                        </div>
                    </div>
                    
                    <!-- Alerts -->
                    {% if job.days_remaining %}
                    {% if job.days_remaining > 10 %}
                    <div class="alert alert-success">
                        <i class="fas fa-check-circle"></i>
                        <strong>{{ job.days_remaining }}</strong> days remaining to apply!
                    </div>
                    {% elif job.days_remaining > 0 %}
                    <div class="alert alert-warning">
                        <i class="fas fa-exclamation-triangle"></i>
                        <strong>Hurry!</strong> Only <strong>{{ job.days_remaining }}</strong> days left to apply!
                    </div>
                    {% else %}
                    <div class="alert alert-danger">
                        <i class="fas fa-times-circle"></i>
                        Application deadline has passed.
                    </div>
                    {% endif %}
                    {% endif %}
                </div>
            </div>
            
            <!-- Job Description -->
            <div class="card mb-4 border-0 shadow-sm">
                <div class="card-body">
                    <h3>Job Description</h3>
                    <div class="card-text">
                        {{ job.description|linebreaks }}
                    </div>
                </div>
            </div>
            
            <!-- Eligibility -->
            {% if job.eligibility or job.qualification_level or job.experience_required %}
            <div class="card mb-4 border-0 shadow-sm">
                <div class="card-body">
                    <h3>Eligibility Criteria</h3>
                    
                    {% if job.qualification_level %}
                    <p class="mb-2">
                        <strong>Qualification:</strong> {{ job.qualification_level.get_level_display }}
                    </p>
                    {% endif %}
                    
                    {% if job.min_age or job.max_age %}
                    <p class="mb-2">
                        <strong>Age Limit:</strong> 
                        {% if job.min_age and job.max_age %}
                            {{ job.min_age }} - {{ job.max_age }} years
                        {% elif job.max_age %}
                            Up to {{ job.max_age }} years
                        {% endif %}
                    </p>
                    {% endif %}
                    
                    {% if job.experience_required %}
                    <p class="mb-2">
                        <strong>Experience Required:</strong> {{ job.experience_required }}
                    </p>
                    {% endif %}
                    
                    {% if job.gender_preference != 'Any' %}
                    <p class="mb-2">
                        <strong>Gender:</strong> {{ job.gender_preference }}
                    </p>
                    {% endif %}
                    
                    {% if job.eligibility %}
                    <p>
                        <strong>Additional Eligibility:</strong><br>
                        {{ job.eligibility|linebreaks }}
                    </p>
                    {% endif %}
                </div>
            </div>
            {% endif %}
            
            <!-- Application Fee -->
            {% if job.application_fee %}
            <div class="card mb-4 border-0 shadow-sm">
                <div class="card-body">
                    <h3>Application Fee</h3>
                    <p class="h5">₹{{ job.application_fee }}</p>
                </div>
            </div>
            {% endif %}
        </div>
        
        <!-- Sidebar -->
        <div class="col-lg-4">
            <!-- Apply Button -->
            <div class="card mb-4 border-0 shadow-sm sticky-top" style="top: 80px;">
                <div class="card-body text-center">
                    {% if job.application_link and job.days_remaining > 0 %}
                    <a href="{{ job.application_link }}" target="_blank" class="btn btn-primary btn-lg w-100 mb-2">
                        <i class="fas fa-external-link-alt"></i> Apply Now
                    </a>
                    {% else %}
                    <button class="btn btn-secondary btn-lg w-100 mb-2" disabled>
                        <i class="fas fa-times-circle"></i> Application Closed
                    </button>
                    {% endif %}
                    
                    <a href="javascript:window.print()" class="btn btn-outline-secondary w-100">
                        <i class="fas fa-print"></i> Print
                    </a>
                </div>
            </div>
            
            <!-- Share -->
            <div class="card mb-4 border-0 shadow-sm">
                <div class="card-body">
                    <h6 class="mb-3">Share</h6>
                    <div class="d-flex gap-2">
                        <a href="https://www.facebook.com/sharer/sharer.php?u={{ request.build_absolute_uri }}" 
                           target="_blank" class="btn btn-sm btn-primary">
                            <i class="fab fa-facebook"></i>
                        </a>
                        <a href="https://twitter.com/intent/tweet?url={{ request.build_absolute_uri }}&text={{ job.title }}" 
                           target="_blank" class="btn btn-sm btn-info">
                            <i class="fab fa-twitter"></i>
                        </a>
                        <a href="https://www.linkedin.com/sharing/share-offsite/?url={{ request.build_absolute_uri }}" 
                           target="_blank" class="btn btn-sm btn-secondary">
                            <i class="fab fa-linkedin"></i>
                        </a>
                        <a href="https://wa.me/?text={{ job.title }} {{ request.build_absolute_uri }}" 
                           target="_blank" class="btn btn-sm btn-success">
                            <i class="fab fa-whatsapp"></i>
                        </a>
                    </div>
                </div>
            </div>
            
            <!-- Organization Info -->
            <div class="card border-0 shadow-sm">
                <div class="card-body">
                    <h6 class="mb-3">Organization</h6>
                    <p><strong>{{ job.organization.name }}</strong></p>
                    {% if job.organization.website %}
                    <p>
                        <a href="{{ job.organization.website }}" target="_blank" class="btn btn-sm btn-outline-primary">
                            Visit Website
                        </a>
                    </p>
                    {% endif %}
                    {% if job.organization.description %}
                    <p class="text-muted small">{{ job.organization.description }}</p>
                    {% endif %}
                </div>
            </div>
        </div>
    </div>
    
    <!-- Related Jobs -->
    {% if related_jobs %}
    <div class="mt-5">
        <h3 class="mb-4">Related Jobs from {{ job.organization.name }}</h3>
        <div class="row">
            {% for related in related_jobs %}
            <div class="col-md-4 mb-3">
                <div class="card job-card h-100">
                    <div class="card-body">
                        <h6 class="card-title">
                            <a href="{% url 'job_detail' related.pk %}" class="text-decoration-none">
                                {{ related.title }}
                            </a>
                        </h6>
                        <p class="small text-muted mb-2">{{ related.organization.name }}</p>
                        <div class="d-flex justify-content-between">
                            <span class="badge bg-primary">{{ related.vacancies }} Posts</span>
                            <span class="text-muted small">{{ related.application_end_date|date:"d M" }}</span>
                        </div>
                    </div>
                </div>
            </div>
            {% endfor %}
        </div>
    </div>
    {% endif %}
</div>

{% endblock %}

{% block extra_css %}
<style>
    .card {
        border-radius: 8px;
    }
    
    @media (max-width: 768px) {
        .card.sticky-top {
            position: static !important;
            margin-bottom: 2rem;
        }
    }
</style>
{% endblock %}
```

---

## Summary of Files Created

| File | Purpose | Lines |
|------|---------|-------|
| `base.html` | Main layout with Bootstrap | 120+ |
| `home_page.html` | Homepage with hero, stats, featured jobs | 200+ |
| `job_list.html` | Responsive job listings with filters | 180+ |
| `job_detail.html` | Detailed job posting page | 250+ |
| `sarkarinaukri.css` | Responsive CSS (already provided above) | 350+ |

---

## Testing Checklist

- [ ] Test on desktop (1440px) - Looks great
- [ ] Test on tablet (768px) - Responsive
- [ ] Test on mobile (375px) - Mobile-friendly
- [ ] Check hamburger menu works
- [ ] Test all links and forms
- [ ] Verify images load correctly
- [ ] Test filter functionality
- [ ] Check pagination
- [ ] Test sharing buttons
- [ ] Verify responsive breakpoints

---

## Performance Optimization Tips

1. **Lazy load images**: Add `loading="lazy"` to `<img>` tags
2. **Compress images**: Use WebP format where possible
3. **Minify CSS**: Use `collectstatic` in production
4. **Cache pages**: Add `@cache_page()` decorator
5. **Use CDN**: Serve Bootstrap/Font Awesome from CDN

---

## Next Steps

1. **Implement templates** as shown above
2. **Update views** to pass all required context
3. **Test locally** with `python manage.py runserver`
4. **Deploy to staging** and test responsiveness
5. **Get feedback** from users
6. **Optimize based on feedback**

---

**Need help? Check QUICK_START_IMPROVEMENTS.md for immediate wins!**
