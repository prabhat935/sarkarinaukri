from django.core.management.base import BaseCommand
from content.models import (
    Organization, ExamCategory, State, QualificationLevel,
    JobPosting, ExamResult, AdmitCard, AnswerKey, Syllabus,
    BoardExamResult, Scholarship, ImportantNotification, OnlineForm,
    CertificateVerification
)
import random
from datetime import date, timedelta
from decimal import Decimal

class Command(BaseCommand):
    help = 'Populate database with mass sample data'

    def handle(self, *args, **options):
        self.stdout.write('🚀 Starting mass data population...')

        # Get existing reference data
        organizations = list(Organization.objects.all())
        categories = list(ExamCategory.objects.all())
        states = list(State.objects.all())
        qualifications = list(QualificationLevel.objects.all())

        if not organizations:
            self.stdout.write(self.style.ERROR('❌ No organizations found. Run import_initial_data first.'))
            return

        self.stdout.write(f'📊 Found {len(organizations)} organizations, {len(categories)} categories, {len(states)} states')

        # ===== JOB POSTINGS =====
        if JobPosting.objects.count() == 0:
            self.stdout.write('📝 Creating job postings...')
            self._create_job_postings(organizations, categories, states, qualifications)
        else:
            self.stdout.write(f'📝 Job postings already exist ({JobPosting.objects.count()}), skipping...')

        # ===== EXAM RESULTS =====
        if ExamResult.objects.count() == 0:
            self.stdout.write('📊 Creating exam results...')
            self._create_exam_results(organizations, categories, states)
        else:
            self.stdout.write(f'📊 Exam results already exist ({ExamResult.objects.count()}), skipping...')

        # ===== ADMIT CARDS =====
        if AdmitCard.objects.count() == 0:
            self.stdout.write('🎫 Creating admit cards...')
            self._create_admit_cards(organizations, categories, states)
        else:
            self.stdout.write(f'🎫 Admit cards already exist ({AdmitCard.objects.count()}), skipping...')

        # ===== ANSWER KEYS =====
        if AnswerKey.objects.count() == 0:
            self.stdout.write('🔑 Creating answer keys...')
            self._create_answer_keys(organizations, categories, states)
        else:
            self.stdout.write(f'🔑 Answer keys already exist ({AnswerKey.objects.count()}), skipping...')

        # ===== SYLLABUS =====
        if Syllabus.objects.count() == 0:
            self.stdout.write('📚 Creating syllabus...')
            self._create_syllabus(organizations, categories, states)
        else:
            self.stdout.write(f'📚 Syllabus already exist ({Syllabus.objects.count()}), skipping...')

        # ===== BOARD EXAM RESULTS =====
        if BoardExamResult.objects.count() == 0:
            self.stdout.write('🏫 Creating board exam results...')
            self._create_board_results()
        else:
            self.stdout.write(f'🏫 Board exam results already exist ({BoardExamResult.objects.count()}), skipping...')

        # ===== SCHOLARSHIPS =====
        if Scholarship.objects.count() == 0:
            self.stdout.write('💰 Creating scholarships...')
            self._create_scholarships(states)
        else:
            self.stdout.write(f'💰 Scholarships already exist ({Scholarship.objects.count()}), skipping...')

        # ===== IMPORTANT NOTIFICATIONS =====
        if ImportantNotification.objects.count() == 0:
            self.stdout.write('📢 Creating important notifications...')
            self._create_notifications(organizations, states)
        else:
            self.stdout.write(f'📢 Important notifications already exist ({ImportantNotification.objects.count()}), skipping...')

        # ===== ONLINE FORMS =====
        if OnlineForm.objects.count() == 0:
            self.stdout.write('📝 Creating online forms...')
            self._create_online_forms(organizations, states)
        else:
            self.stdout.write(f'📝 Online forms already exist ({OnlineForm.objects.count()}), skipping...')

        # ===== CERTIFICATE VERIFICATION =====
        if CertificateVerification.objects.count() == 0:
            self.stdout.write('🔍 Creating certificate verification...')
            self._create_verifications(organizations, categories)
        else:
            self.stdout.write(f'🔍 Certificate verification already exists ({CertificateVerification.objects.count()}), skipping...')

        self.stdout.write(self.style.SUCCESS('\n🎉 Mass data population completed successfully!'))
        self._print_final_counts()

    def _create_job_postings(self, organizations, categories, states, qualifications):
        job_titles = [
            "Junior Engineer", "Clerk", "Teacher", "Constable", "Inspector",
            "Assistant", "Officer", "Supervisor", "Technician", "Manager",
            "Accountant", "Stenographer", "Driver", "Peon", "Security Guard",
            "Nurse", "Doctor", "Professor", "Lecturer", "Principal"
        ]

        organizations_list = [
            "SSC", "UPSC", "Railway", "Bank", "Police", "Teaching", "Defence", "Insurance"
        ]

        for i in range(200):
            org = random.choice(organizations)
            cat = random.choice(categories)
            state = random.choice(states) if random.random() > 0.3 else None

            # Make more jobs for 2026
            year = random.choices([2024, 2025, 2026], weights=[20, 30, 50])[0]
            title = f"{random.choice(job_titles)} {random.choice(organizations_list)} Recruitment {year}"
            start_date = date.today() + timedelta(days=random.randint(-30, 60))
            end_date = start_date + timedelta(days=random.randint(15, 45))

            JobPosting.objects.create(
                title=title,
                slug=f"{title.lower().replace(' ', '-').replace('recruitment', 'recruitment-' + str(i+1))}-{random.randint(1000, 9999)}",
                description=f"Applications are invited for {random.randint(10, 1000)} {title} positions.",
                organization=org, exam_category=cat, state=state,
                year=year,
                vacancies=random.randint(1, 2000), job_level=random.choice(['A', 'B', 'C', 'D']),
                qualification_level=random.choice(qualifications) if qualifications else None,
                min_age=random.randint(18, 25), max_age=random.randint(30, 60),
                salary_min=Decimal(str(random.randint(15000, 50000))),
                salary_max=Decimal(str(random.randint(50000, 200000))),
                eligibility=f"Minimum {random.choice(['10th', '12th', 'Graduate', 'Post Graduate'])} qualification required.",
                application_start_date=start_date, application_end_date=end_date,
                exam_date=end_date + timedelta(days=random.randint(30, 90)),
                application_link=f"https://{org.name.lower()}.gov.in/recruitment-{random.randint(1000, 9999)}",
                application_fee=Decimal(str(random.randint(100, 1000))),
                status=random.choice(['Active', 'Active', 'Active', 'Closed'])
            )

    def _create_exam_results(self, organizations, categories, states):
        exam_names = [
            "SSC CGL", "SSC CHSL", "SSC GD", "SSC MTS", "SSC JE",
            "UPSC IAS", "UPSC IPS", "UPSC IFS", "Railway NTPC", "Railway Group D",
            "Bank PO", "Bank Clerk", "IBPS PO", "IBPS Clerk", "SBI PO",
            "UPPSC PCS", "BPSC 68th", "MPPSC", "RPSC RAS", "HPSC HCS"
        ]

        created_exam_results = set()
        for i in range(150):
            exam_name = random.choice(exam_names)
            year = random.randint(2020, 2024)
            
            while (exam_name, year) in created_exam_results:
                exam_name = random.choice(exam_names)
                year = random.randint(2020, 2024)
            
            created_exam_results.add((exam_name, year))
            
            org = random.choice(organizations)
            cat = random.choice(categories)
            state = random.choice(states) if random.random() > 0.4 else None

            ExamResult.objects.create(
                exam_name=f"{exam_name} {year}",
                slug=f"{exam_name.lower().replace(' ', '-')}-{year}-{i+1}",
                description=f"Result declared for {exam_name} {year} examination.",
                organization=org, exam_category=cat, state=state, exam_year=year,
                result_date=date.today() + timedelta(days=random.randint(-365, 30)),
                result_pdf_link=f"https://{org.name.lower()}.gov.in/results/{exam_name.lower().replace(' ', '-')}-{year}.pdf",
                total_posts=random.randint(100, 5000), selected_candidates=random.randint(50, 2000),
                is_official=random.choice([True, True, False])
            )

    def _create_admit_cards(self, organizations, categories, states):
        exam_names = [
            "SSC CGL", "SSC CHSL", "SSC GD", "SSC MTS", "SSC JE",
            "UPSC IAS", "UPSC IPS", "UPSC IFS", "Railway NTPC", "Railway Group D",
            "Bank PO", "Bank Clerk", "IBPS PO", "IBPS Clerk", "SBI PO"
        ]

        for i in range(120):
            exam_name = random.choice(exam_names)
            org = random.choice(organizations)
            cat = random.choice(categories)
            state = random.choice(states) if random.random() > 0.4 else None
            exam_date = date.today() + timedelta(days=random.randint(1, 90))

            AdmitCard.objects.create(
                exam_name=f"{exam_name} {random.randint(2024, 2026)}",
                slug=f"{exam_name.lower().replace(' ', '-')}-admit-card-{i+1}",
                description=f"Download admit card for {exam_name} examination.",
                organization=org, exam_category=cat, state=state,
                exam_date=exam_date,
                admit_card_date=exam_date - timedelta(days=random.randint(7, 21)),
                download_link=f"https://{org.name.lower()}.gov.in/admitcard/{exam_name.lower().replace(' ', '-')}-{random.randint(1000, 9999)}",
                exam_time=f"{random.randint(9, 14):02d}:{random.randint(0, 59):02d}:00",
                exam_duration="2 hours",
                instructions="Candidates must bring original ID proof and admit card to the examination center."
            )

    def _create_answer_keys(self, organizations, categories, states):
        exam_names = [
            "SSC CGL", "SSC CHSL", "SSC GD", "SSC MTS", "SSC JE",
            "UPSC IAS", "Railway NTPC", "Bank PO", "IBPS PO", "SBI PO"
        ]

        created_answer_keys = set()
        for i in range(100):
            exam_name = random.choice(exam_names)
            year = random.randint(2023, 2025)
            shift = random.randint(1, 2)
            
            while (exam_name, year, shift) in created_answer_keys:
                exam_name = random.choice(exam_names)
                year = random.randint(2023, 2025)
                shift = random.randint(1, 2)
            
            created_answer_keys.add((exam_name, year, shift))
            
            org = random.choice(organizations)
            cat = random.choice(categories)
            state = random.choice(states) if random.random() > 0.4 else None

            AnswerKey.objects.create(
                exam_name=f"{exam_name} {year}",
                slug=f"{exam_name.lower().replace(' ', '-')}-answer-key-{year}-{shift}-{i+1}",
                description=f"Official answer key for {exam_name} {year} examination.",
                organization=org, exam_category=cat, state=state,
                exam_year=year,
                exam_date=date.today() + timedelta(days=random.randint(-180, -30)),
                shift_number=shift,
                answer_key_link=f"https://{org.name.lower()}.gov.in/answerkey/{exam_name.lower().replace(' ', '-')}-{year}.pdf",
                solution_pdf_link=f"https://{org.name.lower()}.gov.in/solutions/{exam_name.lower().replace(' ', '-')}-{year}.pdf" if random.random() > 0.5 else "",
                is_official=random.choice([True, True, False]),
                is_provisional=random.choice([False, False, True])
            )

    def _create_syllabus(self, organizations, categories, states):
        exam_names = [
            "SSC CGL", "SSC CHSL", "SSC GD", "SSC MTS", "SSC JE",
            "UPSC IAS", "Railway NTPC", "Bank PO", "IBPS PO", "SBI PO"
        ]

        subjects = [
            "General Knowledge", "Mathematics", "English", "Reasoning", "Science",
            "History", "Geography", "Economics", "Computer Science", "Hindi"
        ]

        for i in range(80):
            exam_name = random.choice(exam_names)
            year = random.randint(2024, 2026)
            org = random.choice(organizations)
            cat = random.choice(categories)
            state = random.choice(states) if random.random() > 0.4 else None
            selected_subjects = random.sample(subjects, random.randint(3, 8))

            Syllabus.objects.create(
                exam_name=f"{exam_name} {year}",
                slug=f"{exam_name.lower().replace(' ', '-')}-syllabus-{year}-{i+1}",
                organization=org, exam_category=cat, state=state, exam_year=year,
                subjects=", ".join(selected_subjects),
                detailed_syllabus_link=f"https://{org.name.lower()}.gov.in/syllabus/{exam_name.lower().replace(' ', '-')}-{year}.pdf",
                important_topics=f"Focus on {', '.join(random.sample(selected_subjects, 3))}",
                previous_papers_link=f"https://{org.name.lower()}.gov.in/previous-papers/{exam_name.lower().replace(' ', '-')}.pdf" if random.random() > 0.6 else ""
            )

    def _create_board_results(self):
        boards = ['CBSE', 'ICSE', 'UP Board', 'Bihar Board', 'MP Board', 'Rajasthan Board']

        for board in boards:
            for year in [2023, 2024, 2025]:
                for exam_type in ['10th', '12th']:
                    BoardExamResult.objects.create(
                        board=board, exam_type=exam_type, year=year,
                        result_link=f"https://{board.lower().replace(' ', '')}.nic.in/results/class-{exam_type}-{year}",
                        digilocker_link="https://digilocker.gov.in/",
                        result_date=date(year, 5, 15) if year < 2025 else date.today() + timedelta(days=random.randint(-30, 30)),
                        is_declared=year < 2025 or random.random() > 0.5,
                        total_students=random.randint(500000, 2000000),
                        pass_percentage=Decimal(str(round(random.uniform(85, 98), 1)))
                    )

    def _create_scholarships(self, states):
        scholarship_types = [
            ("Post Matric Scholarship for SC Students", "SC/ST", "SC/ST students pursuing higher education"),
            ("OBC Scholarship Scheme", "OBC", "OBC students for professional courses"),
            ("Minority Scholarship", "Minority", "Minority community students"),
            ("Merit Scholarship", "Merit", "High performing students"),
            ("Pre Matric Scholarship", "General", "Students from economically weaker sections"),
            ("Girl Child Scholarship", "General", "Girl students for higher education"),
        ]

        created_scholarships = set()
        for name, category, eligibility in scholarship_types:
            for state in random.sample(states, random.randint(2, 5)):
                scholarship_name = f"{name} - {state.name}"
                
                # Generate unique slug
                base_slug = f"{scholarship_name.lower().replace(' ', '-').replace('/', '-')}"
                slug = base_slug
                counter = 1
                while slug in created_scholarships:
                    slug = f"{base_slug}-{counter}"
                    counter += 1
                created_scholarships.add(slug)
                
                Scholarship.objects.create(
                    name=scholarship_name, state=state, category=category, slug=slug,
                    application_start_date=date.today() + timedelta(days=random.randint(-30, 30)),
                    application_end_date=date.today() + timedelta(days=random.randint(30, 120)),
                    application_link=f"https://scholarship.{state.name.lower().replace(' ', '')}.gov.in/",
                    eligibility=f"{eligibility} in {state.name}",
                    benefits="Full tuition fee waiver + maintenance allowance of ₹500-2000/month",
                    status=random.choice(['Open', 'Open', 'Closed'])
                )

    def _create_notifications(self, organizations, states):
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

        created_notifications = set()
        for title, category, description in notifications:
            # Generate unique slug
            base_slug = f"{title.lower().replace(' ', '-').replace('2025', '2025-' + str(random.randint(1000, 9999)))}"
            slug = base_slug
            counter = 1
            while slug in created_notifications:
                slug = f"{base_slug}-{counter}"
                counter += 1
            created_notifications.add(slug)
            
            ImportantNotification.objects.create(
                title=title, category=category, description=description, slug=slug,
                notification_link=f"https://example.gov.in/notification/{random.randint(1000, 9999)}",
                pdf_link=f"https://example.gov.in/pdf/notification-{random.randint(1000, 9999)}.pdf" if random.random() > 0.5 else "",
                state=random.choice(states) if random.random() > 0.6 else None,
                organization=random.choice(organizations) if random.random() > 0.7 else None,
                is_urgent=random.random() > 0.8
            )

    def _create_online_forms(self, organizations, states):
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

        created_forms = set()
        for name, category, description in form_types:
            form_name = f"{name} {random.randint(2024, 2026)}"
            
            # Generate unique slug
            base_slug = f"{form_name.lower().replace(' ', '-').replace('online-form', 'online-form-' + str(random.randint(1000, 9999)))}"
            slug = base_slug
            counter = 1
            while slug in created_forms:
                slug = f"{base_slug}-{counter}"
                counter += 1
            created_forms.add(slug)
            
            OnlineForm.objects.create(
                name=form_name, category=category, slug=slug,
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

    def _create_verifications(self, organizations, categories):
        verification_exams = [
            "SSC CGL", "SSC CHSL", "UPSC IAS", "Railway NTPC", "Bank PO",
            "UPPSC PCS", "BPSC", "MPPSC", "RPSC RAS", "CTET"
        ]

        created_verifications = set()
        for exam in verification_exams:
            org = random.choice(organizations)
            
            # Generate unique slug
            base_slug = f"{exam.lower().replace(' ', '-')}-certificate-verification-{random.randint(1000, 9999)}"
            slug = base_slug
            counter = 1
            while slug in created_verifications:
                slug = f"{base_slug}-{counter}"
                counter += 1
            created_verifications.add(slug)
            
            CertificateVerification.objects.create(
                exam_name=f"{exam} Certificate Verification", slug=slug,
                organization=org, exam_category=random.choice(categories),
                verification_link=f"https://{org.name.lower()}.gov.in/verify/{exam.lower().replace(' ', '-')}",
                year=random.randint(2020, 2024),
                instructions=f"Visit the official website to verify your {exam} certificate authenticity."
            )

    def _print_final_counts(self):
        self.stdout.write('📊 Final Content Counts:')
        self.stdout.write(f'• Job Postings: {JobPosting.objects.count()}')
        self.stdout.write(f'• Exam Results: {ExamResult.objects.count()}')
        self.stdout.write(f'• Admit Cards: {AdmitCard.objects.count()}')
        self.stdout.write(f'• Answer Keys: {AnswerKey.objects.count()}')
        self.stdout.write(f'• Syllabus: {Syllabus.objects.count()}')
        self.stdout.write(f'• Board Results: {BoardExamResult.objects.count()}')
        self.stdout.write(f'• Scholarships: {Scholarship.objects.count()}')
        self.stdout.write(f'• Notifications: {ImportantNotification.objects.count()}')
        self.stdout.write(f'• Online Forms: {OnlineForm.objects.count()}')
        self.stdout.write(f'• Verifications: {CertificateVerification.objects.count()}')
        total = sum([
            JobPosting.objects.count(), ExamResult.objects.count(), AdmitCard.objects.count(),
            AnswerKey.objects.count(), Syllabus.objects.count(), BoardExamResult.objects.count(),
            Scholarship.objects.count(), ImportantNotification.objects.count(),
            OnlineForm.objects.count(), CertificateVerification.objects.count()
        ])
        self.stdout.write(f'• TOTAL: {total} entries')