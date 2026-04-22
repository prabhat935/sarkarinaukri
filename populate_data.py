#!/usr/bin/env python
"""
Mass Data Population Script for SarkariNaukri
Creates realistic sample data similar to sarkariresult.com
"""

import os
import django
import random
from datetime import date, timedelta
from decimal import Decimal

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sarkarinaukri.settings.dev')
django.setup()

from content.models import (
    Organization, ExamCategory, State, QualificationLevel,
    JobPosting, ExamResult, AdmitCard, AnswerKey, Syllabus,
    BoardExamResult, Scholarship, ImportantNotification, OnlineForm,
    CertificateVerification
)

def create_mass_data():
    print("🚀 Starting mass data population...")

    # Get existing reference data
    organizations = list(Organization.objects.all())
    categories = list(ExamCategory.objects.all())
    states = list(State.objects.all())
    qualifications = list(QualificationLevel.objects.all())

    if not organizations:
        print("❌ No organizations found. Run import_initial_data first.")
        return

    print(f"📊 Found {len(organizations)} organizations, {len(categories)} categories, {len(states)} states")

    # ===== JOB POSTINGS =====
    print("📝 Creating job postings...")
    job_titles = [
        "Junior Engineer", "Clerk", "Teacher", "Constable", "Inspector",
        "Assistant", "Officer", "Supervisor", "Technician", "Manager",
        "Accountant", "Stenographer", "Driver", "Peon", "Security Guard",
        "Nurse", "Doctor", "Professor", "Lecturer", "Principal"
    ]

    organizations_list = [
        "SSC", "UPSC", "Railway", "Bank", "Police", "Teaching", "Defence", "Insurance"
    ]

    for i in range(200):  # Create 200 job postings
        org = random.choice(organizations)
        cat = random.choice(categories)
        state = random.choice(states) if random.random() > 0.3 else None

        title = f"{random.choice(job_titles)} {random.choice(organizations_list)} Recruitment {2024 + random.randint(0, 2)}"

        start_date = date.today() + timedelta(days=random.randint(-30, 60))
        end_date = start_date + timedelta(days=random.randint(15, 45))

        JobPosting.objects.create(
            title=title,
            description=f"Applications are invited for {random.randint(10, 1000)} {title} positions. Detailed notification available on official website.",
            organization=org,
            exam_category=cat,
            state=state,
            vacancies=random.randint(1, 2000),
            job_level=random.choice(['A', 'B', 'C', 'D']),
            qualification_level=random.choice(qualifications) if qualifications else None,
            min_age=random.randint(18, 25),
            max_age=random.randint(30, 60),
            salary_min=Decimal(str(random.randint(15000, 50000))),
            salary_max=Decimal(str(random.randint(50000, 200000))),
            eligibility=f"Minimum {random.choice(['10th', '12th', 'Graduate', 'Post Graduate'])} qualification required.",
            application_start_date=start_date,
            application_end_date=end_date,
            exam_date=end_date + timedelta(days=random.randint(30, 90)),
            application_link=f"https://{org.name.lower()}.gov.in/recruitment-{random.randint(1000, 9999)}",
            application_fee=Decimal(str(random.randint(100, 1000))),
            status=random.choice(['Active', 'Active', 'Active', 'Closed']),
            meta_description=f"Apply for {title} - {org.name} Recruitment {2024 + random.randint(0, 2)}"
        )

    print(f"✅ Created {JobPosting.objects.count()} job postings")

    # ===== EXAM RESULTS =====
    print("📊 Creating exam results...")
    exam_names = [
        "SSC CGL", "SSC CHSL", "SSC GD", "SSC MTS", "SSC JE",
        "UPSC IAS", "UPSC IPS", "UPSC IFS", "Railway NTPC", "Railway Group D",
        "Bank PO", "Bank Clerk", "IBPS PO", "IBPS Clerk", "SBI PO",
        "UPPSC PCS", "BPSC 68th", "MPPSC", "RPSC RAS", "HPSC HCS"
    ]

    for i in range(150):  # Create 150 exam results
        exam_name = random.choice(exam_names)
        year = random.randint(2020, 2024)
        org = random.choice(organizations)
        cat = random.choice(categories)
        state = random.choice(states) if random.random() > 0.4 else None

        ExamResult.objects.create(
            exam_name=f"{exam_name} {year}",
            description=f"Result declared for {exam_name} {year} examination conducted by {org.name}.",
            organization=org,
            exam_category=cat,
            state=state,
            exam_year=year,
            result_date=date.today() + timedelta(days=random.randint(-365, 30)),
            result_pdf_link=f"https://{org.name.lower()}.gov.in/results/{exam_name.lower().replace(' ', '-')}-{year}.pdf",
            total_posts=random.randint(100, 5000),
            selected_candidates=random.randint(50, 2000),
            is_official=random.choice([True, True, False]),
            meta_description=f"{exam_name} {year} Result - Check your result status"
        )

    print(f"✅ Created {ExamResult.objects.count()} exam results")

    # ===== ADMIT CARDS =====
    print("🎫 Creating admit cards...")
    for i in range(120):  # Create 120 admit cards
        exam_name = random.choice(exam_names)
        org = random.choice(organizations)
        cat = random.choice(categories)
        state = random.choice(states) if random.random() > 0.4 else None

        exam_date = date.today() + timedelta(days=random.randint(1, 90))

        AdmitCard.objects.create(
            exam_name=f"{exam_name} {random.randint(2024, 2026)}",
            description=f"Download admit card for {exam_name} examination.",
            organization=org,
            exam_category=cat,
            state=state,
            exam_date=exam_date,
            admit_card_date=exam_date - timedelta(days=random.randint(7, 21)),
            download_link=f"https://{org.name.lower()}.gov.in/admitcard/{exam_name.lower().replace(' ', '-')}-{random.randint(1000, 9999)}",
            exam_time="10:00 AM",
            exam_duration="2 hours",
            instructions="Candidates must bring original ID proof and admit card to the examination center."
        )

    print(f"✅ Created {AdmitCard.objects.count()} admit cards")

    # ===== ANSWER KEYS =====
    print("🔑 Creating answer keys...")
    for i in range(100):  # Create 100 answer keys
        exam_name = random.choice(exam_names)
        year = random.randint(2023, 2025)
        org = random.choice(organizations)
        cat = random.choice(categories)
        state = random.choice(states) if random.random() > 0.4 else None

        AnswerKey.objects.create(
            exam_name=f"{exam_name} {year}",
            description=f"Official answer key for {exam_name} {year} examination.",
            organization=org,
            exam_category=cat,
            state=state,
            exam_year=year,
            exam_date=date.today() + timedelta(days=random.randint(-180, -30)),
            shift_number=random.randint(1, 2),
            answer_key_link=f"https://{org.name.lower()}.gov.in/answerkey/{exam_name.lower().replace(' ', '-')}-{year}.pdf",
            solution_pdf_link=f"https://{org.name.lower()}.gov.in/solutions/{exam_name.lower().replace(' ', '-')}-{year}.pdf" if random.random() > 0.5 else "",
            is_official=random.choice([True, True, False]),
            is_provisional=random.choice([False, False, True])
        )

    print(f"✅ Created {AnswerKey.objects.count()} answer keys")

    # ===== SYLLABUS =====
    print("📚 Creating syllabus...")
    subjects = [
        "General Knowledge", "Mathematics", "English", "Reasoning", "Science",
        "History", "Geography", "Economics", "Computer Science", "Hindi",
        "General Science", "Current Affairs", "Quantitative Aptitude", "Logical Reasoning"
    ]

    for i in range(80):  # Create 80 syllabus entries
        exam_name = random.choice(exam_names)
        year = random.randint(2024, 2026)
        org = random.choice(organizations)
        cat = random.choice(categories)
        state = random.choice(states) if random.random() > 0.4 else None

        selected_subjects = random.sample(subjects, random.randint(3, 8))

        Syllabus.objects.create(
            exam_name=f"{exam_name} {year}",
            organization=org,
            exam_category=cat,
            state=state,
            exam_year=year,
            subjects=", ".join(selected_subjects),
            detailed_syllabus_link=f"https://{org.name.lower()}.gov.in/syllabus/{exam_name.lower().replace(' ', '-')}-{year}.pdf",
            important_topics=f"Focus on {', '.join(random.sample(selected_subjects, 3))}",
            previous_papers_link=f"https://{org.name.lower()}.gov.in/previous-papers/{exam_name.lower().replace(' ', '-')}.pdf" if random.random() > 0.6 else ""
        )

    print(f"✅ Created {Syllabus.objects.count()} syllabus entries")

    # ===== BOARD EXAM RESULTS =====
    print("🏫 Creating board exam results...")
    boards = ['CBSE', 'ICSE', 'UP Board', 'Bihar Board', 'MP Board', 'Rajasthan Board']

    for board in boards:
        for year in [2023, 2024, 2025]:
            for exam_type in ['10th', '12th']:
                BoardExamResult.objects.create(
                    board=board,
                    exam_type=exam_type,
                    year=year,
                    result_link=f"https://{board.lower().replace(' ', '')}.nic.in/results/class-{exam_type}-{year}",
                    digilocker_link="https://digilocker.gov.in/",
                    result_date=date(year, 5, 15) if year < 2025 else date.today() + timedelta(days=random.randint(-30, 30)),
                    is_declared=year < 2025 or random.random() > 0.5,
                    total_students=random.randint(500000, 2000000),
                    pass_percentage=Decimal(str(round(random.uniform(85, 98), 1)))
                )

    print(f"✅ Created {BoardExamResult.objects.count()} board exam results")

    # ===== SCHOLARSHIPS =====
    print("💰 Creating scholarships...")
    scholarship_types = [
        ("Post Matric Scholarship for SC Students", "SC/ST", "SC/ST students pursuing higher education"),
        ("OBC Scholarship Scheme", "OBC", "OBC students for professional courses"),
        ("Minority Scholarship", "Minority", "Minority community students"),
        ("Merit Scholarship", "Merit", "High performing students"),
        ("Pre Matric Scholarship", "General", "Students from economically weaker sections"),
        ("Girl Child Scholarship", "General", "Girl students for higher education"),
    ]

    for name, category, eligibility in scholarship_types:
        for state in random.sample(states, random.randint(2, 5)):
            Scholarship.objects.create(
                name=f"{name} - {state.name}",
                state=state,
                category=category,
                application_start_date=date.today() + timedelta(days=random.randint(-30, 30)),
                application_end_date=date.today() + timedelta(days=random.randint(30, 120)),
                application_link=f"https://scholarship.{state.name.lower().replace(' ', '')}.gov.in/",
                eligibility=f"{eligibility} in {state.name}",
                benefits="Full tuition fee waiver + maintenance allowance of ₹500-2000/month",
                status=random.choice(['Open', 'Open', 'Closed'])
            )

    print(f"✅ Created {Scholarship.objects.count()} scholarships")

    # ===== IMPORTANT NOTIFICATIONS =====
    print("📢 Creating important notifications...")
    notifications = [
        ("SSC CGL 2025 Notification Released", "Recruitment", "Staff Selection Commission has released the Combined Graduate Level 2025 notification with 5000+ vacancies."),
        ("UPSC IAS 2025 Application Started", "Recruitment", "Union Public Service Commission invites applications for Indian Administrative Service 2025."),
        ("Railway RRB NTPC Result Declared", "Exam", "Railway Recruitment Board has declared the NTPC examination result."),
        ("CBSE Class 10th Date Sheet 2025", "Exam", "Central Board of Secondary Education releases class 10th examination schedule."),
        ("New Education Policy Implementation", "Government", "Government announces implementation guidelines for New Education Policy 2020."),
        ("Scholarship Application Deadline Extended", "Admission", "Last date for various scholarship applications extended by 15 days."),
        ("Bank Exam Calendar 2025 Released", "Exam", "IBPS releases tentative calendar for banking examinations 2025."),
        ("Police Constable Recruitment 2025", "Recruitment", "Multiple states announce police constable recruitment drive."),
    ]

    for title, category, description in notifications:
        ImportantNotification.objects.create(
            title=title,
            category=category,
            description=description,
            notification_link=f"https://example.gov.in/notification/{random.randint(1000, 9999)}",
            pdf_link=f"https://example.gov.in/pdf/notification-{random.randint(1000, 9999)}.pdf" if random.random() > 0.5 else "",
            state=random.choice(states) if random.random() > 0.6 else None,
            organization=random.choice(organizations) if random.random() > 0.7 else None,
            is_urgent=random.random() > 0.8
        )

    print(f"✅ Created {ImportantNotification.objects.count()} important notifications")

    # ===== ONLINE FORMS =====
    print("📝 Creating online forms...")
    form_types = [
        ("SSC Various Post Online Form", "Job Application", "Staff Selection Commission recruitment"),
        ("UPSC NDA Online Form", "Job Application", "National Defence Academy application"),
        ("Railway Group D Online Form", "Job Application", "Railway recruitment for Group D posts"),
        ("Bank PO Online Form", "Job Application", "Probationary Officer recruitment"),
        ("UP Police Constable Online Form", "Job Application", "Uttar Pradesh Police recruitment"),
        ("BPSC 69th Online Form", "Job Application", "Bihar Public Service Commission"),
        ("CTET Online Form", "Job Application", "Central Teacher Eligibility Test"),
        ("NEET UG Online Form", "Admission", "Medical entrance examination"),
        ("JEE Main Online Form", "Admission", "Engineering entrance examination"),
        ("Scholarship Online Form", "Scholarship", "Various government scholarships"),
    ]

    for name, category, description in form_types:
        OnlineForm.objects.create(
            name=f"{name} {random.randint(2024, 2026)}",
            category=category,
            organization=random.choice(organizations),
            state=random.choice(states) if random.random() > 0.5 else None,
            form_link=f"https://apply.gov.in/form/{random.randint(10000, 99999)}",
            application_fee=Decimal(str(random.randint(0, 1500))),
            start_date=date.today() + timedelta(days=random.randint(-15, 15)),
            end_date=date.today() + timedelta(days=random.randint(15, 60)),
            eligibility=f"Age: {random.randint(18, 25)}-{random.randint(30, 45)} years, Qualification: {random.choice(['10th', '12th', 'Graduate', 'Post Graduate'])}",
            instructions="Fill all details carefully. Keep scanned documents ready.",
            status=random.choice(['Active', 'Active', 'Extended', 'Closed'])
        )

    print(f"✅ Created {OnlineForm.objects.count()} online forms")

    # ===== CERTIFICATE VERIFICATION =====
    print("🔍 Creating certificate verification...")
    verification_exams = [
        "SSC CGL", "SSC CHSL", "UPSC IAS", "Railway NTPC", "Bank PO",
        "UPPSC PCS", "BPSC", "MPPSC", "RPSC RAS", "CTET"
    ]

    for exam in verification_exams:
        org = random.choice(organizations)
        CertificateVerification.objects.create(
            exam_name=f"{exam} Certificate Verification",
            organization=org,
            exam_category=random.choice(categories),
            verification_link=f"https://{org.name.lower()}.gov.in/verify/{exam.lower().replace(' ', '-')}",
            year=random.randint(2020, 2024),
            instructions=f"Visit the official website to verify your {exam} certificate authenticity."
        )

    print(f"✅ Created {CertificateVerification.objects.count()} certificate verifications")

    print("\n🎉 Mass data population completed successfully!")
    print("📊 Final Content Counts:")
    print(f"• Job Postings: {JobPosting.objects.count()}")
    print(f"• Exam Results: {ExamResult.objects.count()}")
    print(f"• Admit Cards: {AdmitCard.objects.count()}")
    print(f"• Answer Keys: {AnswerKey.objects.count()}")
    print(f"• Syllabus: {Syllabus.objects.count()}")
    print(f"• Board Results: {BoardExamResult.objects.count()}")
    print(f"• Scholarships: {Scholarship.objects.count()}")
    print(f"• Notifications: {ImportantNotification.objects.count()}")
    print(f"• Online Forms: {OnlineForm.objects.count()}")
    print(f"• Verifications: {CertificateVerification.objects.count()}")

if __name__ == "__main__":
    create_mass_data()