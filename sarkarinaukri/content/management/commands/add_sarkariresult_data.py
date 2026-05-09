# content/management/commands/add_sarkariresult_data.py

from django.core.management.base import BaseCommand
from django.utils.text import slugify
from content.models import (
    Organization, ExamCategory, State,
    JobPosting, ExamResult, AdmitCard, AnswerKey,
    Syllabus, AdmissionForm, CertificateVerification, BoardExamResult,
)
import datetime


def safe_slug(base, model_class, field='slug', suffix=''):
    """Generate a unique slug, appending suffix if needed."""
    slug = slugify(base + (' ' + suffix if suffix else ''))[:48]
    if not model_class.objects.filter(**{field: slug}).exists():
        return slug
    for i in range(2, 100):
        candidate = slugify(base)[:44] + f'-{i}'
        if not model_class.objects.filter(**{field: candidate}).exists():
            return candidate
    return slug + '-x'


class Command(BaseCommand):
    help = 'Add missing SarkariResult.com listings: jobs, results, admit cards, answer keys, syllabus, admissions'

    def handle(self, *args, **options):
        self.stdout.write('Adding missing SarkariResult data...\n')
        self._add_orgs()
        self._add_categories()
        self._add_states()
        self._add_jobs()
        self._add_results()
        self._add_admit_cards()
        self._add_answer_keys()
        self._add_syllabi()
        self._add_certificate_verifications()
        self._add_admissions()
        self._add_board_results()
        self.stdout.write(self.style.SUCCESS('\nAll SarkariResult data added successfully!'))

    # ------------------------------------------------------------------
    # Reference data
    # ------------------------------------------------------------------

    def _add_orgs(self):
        orgs = [
            {'name': 'BPSC', 'slug': 'bpsc', 'website': 'https://www.bpsc.bih.nic.in', 'is_featured': True},
            {'name': 'UPSSSC', 'slug': 'upsssc', 'website': 'https://upsssc.gov.in', 'is_featured': True},
            {'name': 'UPPSC', 'slug': 'uppsc', 'website': 'https://uppsc.up.nic.in', 'is_featured': True},
            {'name': 'MPPSC', 'slug': 'mppsc', 'website': 'https://mppsc.mp.gov.in', 'is_featured': False},
            {'name': 'MPESB', 'slug': 'mpesb', 'website': 'https://esb.mp.gov.in', 'is_featured': False},
            {'name': 'CRPF', 'slug': 'crpf', 'website': 'https://crpf.gov.in', 'is_featured': False},
            {'name': 'BPSSC', 'slug': 'bpssc', 'website': 'https://bpssc.bih.nic.in', 'is_featured': False},
            {'name': 'NTA', 'slug': 'nta', 'website': 'https://nta.ac.in', 'is_featured': True},
            {'name': 'UP Police', 'slug': 'up-police', 'website': 'https://uppbpb.gov.in', 'is_featured': True},
            {'name': 'Coal India', 'slug': 'coal-india', 'website': 'https://www.coalindia.in', 'is_featured': False},
            {'name': 'Indian Navy', 'slug': 'indian-navy', 'website': 'https://www.joinindiannavy.gov.in', 'is_featured': False},
            {'name': 'NTPC', 'slug': 'ntpc', 'website': 'https://www.ntpccareers.net', 'is_featured': False},
            {'name': 'PGCIL', 'slug': 'pgcil', 'website': 'https://www.powergridindia.com', 'is_featured': False},
            {'name': 'RSSB', 'slug': 'rssb', 'website': 'https://rsmssb.rajasthan.gov.in', 'is_featured': False},
            {'name': 'Union Bank of India', 'slug': 'union-bank', 'website': 'https://www.unionbankofindia.co.in', 'is_featured': False},
            {'name': 'DSSSB', 'slug': 'dsssb', 'website': 'https://dsssb.delhi.gov.in', 'is_featured': False},
            {'name': 'DDA', 'slug': 'dda', 'website': 'https://dda.org.in', 'is_featured': False},
            {'name': 'JPSC', 'slug': 'jpsc', 'website': 'https://jpsc.gov.in', 'is_featured': False},
            {'name': 'HPSC', 'slug': 'hpsc', 'website': 'https://hpsc.gov.in', 'is_featured': False},
            {'name': 'NABARD', 'slug': 'nabard', 'website': 'https://www.nabard.org', 'is_featured': False},
            {'name': 'IDBI Bank', 'slug': 'idbi-bank', 'website': 'https://www.idbibank.in', 'is_featured': False},
            {'name': 'IB / MHA', 'slug': 'ib-mha', 'website': 'https://mha.gov.in', 'is_featured': False},
            {'name': 'Indian Army', 'slug': 'indian-army', 'website': 'https://joinindianarmy.nic.in', 'is_featured': False},
            {'name': 'UPHESC', 'slug': 'uphesc', 'website': 'https://uphesc.org', 'is_featured': False},
            {'name': 'UP Cooperative Bank', 'slug': 'up-cooperative-bank', 'website': 'https://uppcb.com', 'is_featured': False},
            {'name': 'Bihar Vidhan Parishad', 'slug': 'bihar-vidhan-parishad', 'website': 'https://biharvidhanparishad.gov.in', 'is_featured': False},
            {'name': 'BSSC', 'slug': 'bssc', 'website': 'https://bssc.bihar.gov.in', 'is_featured': False},
            {'name': 'Patna High Court', 'slug': 'patna-high-court', 'website': 'https://patnahighcourt.gov.in', 'is_featured': False},
            {'name': 'Allahabad University', 'slug': 'allahabad-university', 'website': 'https://www.allduniv.ac.in', 'is_featured': False},
            {'name': 'NIELIT', 'slug': 'nielit', 'website': 'https://nielit.gov.in', 'is_featured': False},
            {'name': 'Jharkhand PSC', 'slug': 'jharkhand-psc', 'website': 'https://jpsc.gov.in', 'is_featured': False},
            {'name': 'CSBC Bihar', 'slug': 'csbc-bihar', 'website': 'https://csbc.bih.nic.in', 'is_featured': False},
            {'name': 'Chhattisgarh Board', 'slug': 'cgbse', 'website': 'https://cgbse.net', 'is_featured': False},
        ]
        for data in orgs:
            _, created = Organization.objects.get_or_create(slug=data['slug'], defaults=data)
            if created:
                self.stdout.write(f'  Org: {data["name"]}')

    def _add_categories(self):
        cats = [
            {'name': 'Engineering', 'slug': 'engineering', 'icon': 'fas fa-cogs', 'is_featured': False},
            {'name': 'Medical', 'slug': 'medical', 'icon': 'fas fa-hospital', 'is_featured': False},
            {'name': 'SSC / Central', 'slug': 'ssc-central', 'icon': 'fas fa-star', 'is_featured': True},
            {'name': 'State PSC', 'slug': 'state-psc', 'icon': 'fas fa-landmark', 'is_featured': True},
            {'name': 'Admission', 'slug': 'admission', 'icon': 'fas fa-school', 'is_featured': False},
        ]
        for data in cats:
            _, created = ExamCategory.objects.get_or_create(slug=data['slug'], defaults=data)
            if created:
                self.stdout.write(f'  Category: {data["name"]}')

    def _add_states(self):
        new_states = [
            {'name': 'Delhi', 'code': 'DL', 'is_featured': True},
            {'name': 'Jharkhand', 'code': 'JH', 'is_featured': False},
            {'name': 'Chhattisgarh', 'code': 'CG', 'is_featured': False},
            {'name': 'Himachal Pradesh', 'code': 'HP', 'is_featured': False},
            {'name': 'Uttarakhand', 'code': 'UK', 'is_featured': False},
            {'name': 'Goa', 'code': 'GA', 'is_featured': False},
            {'name': 'Kerala', 'code': 'KL', 'is_featured': False},
        ]
        for data in new_states:
            _, created = State.objects.get_or_create(code=data['code'], defaults=data)
            if created:
                self.stdout.write(f'  State: {data["name"]}')

    # ------------------------------------------------------------------
    # Helper to fetch FK objects safely
    # ------------------------------------------------------------------

    def _org(self, slug):
        return Organization.objects.filter(slug=slug).first()

    def _cat(self, slug):
        return ExamCategory.objects.filter(slug=slug).first()

    def _state(self, code):
        return State.objects.filter(code=code).first()

    # ------------------------------------------------------------------
    # Job Postings
    # ------------------------------------------------------------------

    def _add_jobs(self):
        today = datetime.date.today()
        end_june = datetime.date(2026, 6, 30)
        end_may = datetime.date(2026, 5, 31)
        end_july = datetime.date(2026, 7, 31)

        jobs = [
            {
                'title': 'MPPSC Scientific Officer Biology Online Form 2026',
                'organization': self._org('mppsc'),
                'exam_category': self._cat('state-psc'),
                'state': self._state('MP'),
                'year': 2026, 'vacancies': 70, 'job_level': 'B',
                'application_start_date': datetime.date(2026, 4, 15),
                'application_end_date': end_may,
                'status': 'Active',
                'description': 'MPPSC Scientific Officer Biology recruitment 2026. Graduate in Life Science required.',
            },
            {
                'title': 'UPSSSC Assistant Statistical Officer Online Form 2026',
                'organization': self._org('upsssc'),
                'exam_category': self._cat('state-psc'),
                'state': self._state('UP'),
                'year': 2026, 'vacancies': 400, 'job_level': 'C',
                'application_start_date': datetime.date(2026, 3, 20),
                'application_end_date': end_june,
                'status': 'Active',
                'description': 'UPSSSC Assistant Statistical Officer 2026 – Graduation with Statistics required.',
            },
            {
                'title': 'MP Guest Teacher Online Form 2026',
                'organization': self._org('mpesb'),
                'exam_category': self._cat('teaching'),
                'state': self._state('MP'),
                'year': 2026, 'vacancies': 5000, 'job_level': 'C',
                'application_start_date': datetime.date(2026, 4, 1),
                'application_end_date': end_may,
                'status': 'Active',
                'description': 'MP Guest Teacher recruitment 2026 for various subjects in government schools.',
            },
            {
                'title': 'UPPSC APO 2025 Mains Online Form',
                'organization': self._org('uppsc'),
                'exam_category': self._cat('state-psc'),
                'state': self._state('UP'),
                'year': 2025, 'vacancies': 52, 'job_level': 'B',
                'application_start_date': datetime.date(2026, 4, 10),
                'application_end_date': datetime.date(2026, 5, 10),
                'status': 'Active',
                'description': 'UPPSC Assistant Prosecution Officer 2025 Mains Examination Online Form.',
            },
            {
                'title': 'MPESB Hospital Assistant Online Form 2026',
                'organization': self._org('mpesb'),
                'exam_category': self._cat('medical'),
                'state': self._state('MP'),
                'year': 2026, 'vacancies': 800, 'job_level': 'C',
                'application_start_date': datetime.date(2026, 4, 20),
                'application_end_date': end_june,
                'status': 'Active',
                'description': 'MPESB Hospital Assistant recruitment 2026. 12th pass with Science eligible.',
            },
            {
                'title': 'Coal India CIL Management Trainee Online Form 2026',
                'organization': self._org('coal-india'),
                'exam_category': self._cat('engineering'),
                'state': None,
                'year': 2026, 'vacancies': 640, 'job_level': 'A',
                'application_start_date': datetime.date(2026, 4, 5),
                'application_end_date': datetime.date(2026, 5, 5),
                'status': 'Active',
                'description': 'Coal India CIL Management Trainee 2026 for Engineering and Finance graduates.',
            },
            {
                'title': 'Railway SECR Raipur Apprentices Online Form 2026',
                'organization': self._org('rrb'),
                'exam_category': self._cat('railway'),
                'state': self._state('CG'),
                'year': 2026, 'vacancies': 432, 'job_level': 'D',
                'application_start_date': datetime.date(2026, 4, 18),
                'application_end_date': end_may,
                'status': 'Active',
                'description': 'Railway SECR Raipur Apprentices 2026. ITI pass candidates can apply.',
            },
            {
                'title': 'SSC Stenographer 2025 Option Cum Preference Form',
                'organization': self._org('ssc'),
                'exam_category': self._cat('ssc-central'),
                'state': None,
                'year': 2025, 'vacancies': 2006, 'job_level': 'C',
                'application_start_date': datetime.date(2026, 4, 25),
                'application_end_date': datetime.date(2026, 5, 15),
                'status': 'Active',
                'description': 'SSC Stenographer Grade C & D 2025 Option Cum Preference Form.',
            },
            {
                'title': 'Navy SSC Executive IT Online Form 2026',
                'organization': self._org('indian-navy'),
                'exam_category': self._cat('defence'),
                'state': None,
                'year': 2026, 'vacancies': 50, 'job_level': 'A',
                'application_start_date': datetime.date(2026, 4, 22),
                'application_end_date': datetime.date(2026, 5, 22),
                'status': 'Active',
                'description': 'Indian Navy SSC Executive IT Branch online form 2026 for engineering graduates.',
            },
            {
                'title': 'BPSC 72nd CCE Pre Online Form 2026',
                'organization': self._org('bpsc'),
                'exam_category': self._cat('state-psc'),
                'state': self._state('BR'),
                'year': 2026, 'vacancies': 1500, 'job_level': 'B',
                'application_start_date': datetime.date(2026, 3, 15),
                'application_end_date': datetime.date(2026, 4, 30),
                'status': 'Active',
                'description': 'BPSC 72nd Combined Competitive Exam Pre 2026 notification.',
            },
            {
                'title': 'UP Cooperative Bank UPCISB Various Post Online Form 2026',
                'organization': self._org('up-cooperative-bank'),
                'exam_category': self._cat('bank'),
                'state': self._state('UP'),
                'year': 2026, 'vacancies': 694, 'job_level': 'C',
                'application_start_date': datetime.date(2026, 4, 28),
                'application_end_date': end_may,
                'status': 'Active',
                'description': 'UP Cooperative Bank UPCISB recruitment 2026 for various banking posts.',
            },
            {
                'title': 'RSSB Contractual Teaching Associate Online Form 2026',
                'organization': self._org('rssb'),
                'exam_category': self._cat('teaching'),
                'state': self._state('RJ'),
                'year': 2026, 'vacancies': 9000, 'job_level': 'C',
                'application_start_date': datetime.date(2026, 4, 10),
                'application_end_date': end_june,
                'status': 'Active',
                'description': 'RSSB Contractual Teaching Associate 2026 for Rajasthan government schools.',
            },
            {
                'title': 'BPSSC Havildar Instructor Online Form 2026',
                'organization': self._org('bpssc'),
                'exam_category': self._cat('police'),
                'state': self._state('BR'),
                'year': 2026, 'vacancies': 1669, 'job_level': 'C',
                'application_start_date': datetime.date(2026, 4, 14),
                'application_end_date': end_may,
                'status': 'Active',
                'description': 'BPSSC Havildar Instructor 2026 for Bihar Police department.',
            },
            {
                'title': 'NTA UGC NET June 2026 Online Form',
                'organization': self._org('nta'),
                'exam_category': self._cat('teaching'),
                'state': None,
                'year': 2026, 'vacancies': 0, 'job_level': 'A',
                'application_start_date': datetime.date(2026, 5, 1),
                'application_end_date': end_june,
                'status': 'Active',
                'description': 'NTA UGC NET June 2026 Online Form for Assistant Professor and JRF eligibility.',
            },
            {
                'title': 'UPHESC Assistant Professor BEd Online Form 2026',
                'organization': self._org('uphesc'),
                'exam_category': self._cat('teaching'),
                'state': self._state('UP'),
                'year': 2026, 'vacancies': 2504, 'job_level': 'B',
                'application_start_date': datetime.date(2026, 4, 5),
                'application_end_date': end_may,
                'status': 'Active',
                'description': 'UPHESC Assistant Professor BEd Online Form 2026 Re-Apply.',
            },
            {
                'title': 'Union Bank UBI Apprentices Online Form 2026',
                'organization': self._org('union-bank'),
                'exam_category': self._cat('bank'),
                'state': None,
                'year': 2026, 'vacancies': 500, 'job_level': 'D',
                'application_start_date': datetime.date(2026, 4, 25),
                'application_end_date': datetime.date(2026, 5, 20),
                'status': 'Active',
                'description': 'Union Bank of India UBI Apprentices recruitment 2026.',
            },
            {
                'title': 'BPSC 33rd Civil Judge Online Form 2026',
                'organization': self._org('bpsc'),
                'exam_category': self._cat('state-psc'),
                'state': self._state('BR'),
                'year': 2026, 'vacancies': 90, 'job_level': 'A',
                'application_start_date': datetime.date(2026, 4, 20),
                'application_end_date': end_june,
                'status': 'Active',
                'description': 'BPSC 33rd Civil Judge recruitment 2026 for Bihar state judiciary.',
            },
            {
                'title': 'RBI Officer Grade B Online Form 2026',
                'organization': self._org('rbi'),
                'exam_category': self._cat('bank'),
                'state': None,
                'year': 2026, 'vacancies': 95, 'job_level': 'B',
                'application_start_date': datetime.date(2026, 5, 1),
                'application_end_date': end_june,
                'status': 'Active',
                'description': 'RBI Officer Grade B Direct Recruitment 2026 for General, DEPR, and DSIM streams.',
            },
            {
                'title': 'MPPSC ADPO Online Form 2026',
                'organization': self._org('mppsc'),
                'exam_category': self._cat('state-psc'),
                'state': self._state('MP'),
                'year': 2026, 'vacancies': 75, 'job_level': 'B',
                'application_start_date': datetime.date(2026, 4, 30),
                'application_end_date': end_june,
                'status': 'Active',
                'description': 'MPPSC Assistant District Prosecution Officer (ADPO) Online Form 2026.',
            },
            {
                'title': 'UP Anganwadi Worker Online Form 2026',
                'organization': self._org('up-police'),
                'exam_category': self._cat('state-psc'),
                'state': self._state('UP'),
                'year': 2026, 'vacancies': 23753, 'job_level': 'D',
                'application_start_date': datetime.date(2026, 4, 8),
                'application_end_date': end_may,
                'status': 'Active',
                'description': 'UP Anganwadi Worker / Mini Anganwadi Worker / Anganwadi Helper Online Form 2026.',
            },
            {
                'title': 'SSC Stenographer Grade C & D Online Form 2026',
                'organization': self._org('ssc'),
                'exam_category': self._cat('ssc-central'),
                'state': None,
                'year': 2026, 'vacancies': 2006, 'job_level': 'C',
                'application_start_date': datetime.date(2026, 4, 5),
                'application_end_date': datetime.date(2026, 5, 5),
                'status': 'Active',
                'description': 'SSC Stenographer Grade C & D 2026 recruitment for central government departments.',
            },
            {
                'title': 'NTPC Assistant Executive Operation Online Form 2026',
                'organization': self._org('ntpc'),
                'exam_category': self._cat('engineering'),
                'state': None,
                'year': 2026, 'vacancies': 160, 'job_level': 'B',
                'application_start_date': datetime.date(2026, 4, 12),
                'application_end_date': datetime.date(2026, 5, 12),
                'status': 'Active',
                'description': 'NTPC Assistant Executive (Operation) Online Form 2026 for Engineering graduates.',
            },
            {
                'title': 'SSC Combined Hindi Translator Online Form 2026',
                'organization': self._org('ssc'),
                'exam_category': self._cat('ssc-central'),
                'state': None,
                'year': 2026, 'vacancies': 312, 'job_level': 'B',
                'application_start_date': datetime.date(2026, 4, 15),
                'application_end_date': datetime.date(2026, 5, 15),
                'status': 'Active',
                'description': 'SSC Combined Hindi Translator 2026 for Junior Hindi Translator and Hindi Pradhyapak posts.',
            },
            {
                'title': 'Jharkhand Teacher Eligibility Test JHTET Online Form 2026',
                'organization': self._org('jharkhand-psc'),
                'exam_category': self._cat('teaching'),
                'state': self._state('JH'),
                'year': 2026, 'vacancies': 0, 'job_level': 'C',
                'application_start_date': datetime.date(2026, 4, 25),
                'application_end_date': end_may,
                'status': 'Active',
                'description': 'Jharkhand Teacher Eligibility Test JHTET 2026 online application form.',
            },
            {
                'title': 'PGCIL Diploma Trainee Online Form 2026',
                'organization': self._org('pgcil'),
                'exam_category': self._cat('engineering'),
                'state': None,
                'year': 2026, 'vacancies': 200, 'job_level': 'C',
                'application_start_date': datetime.date(2026, 4, 10),
                'application_end_date': datetime.date(2026, 5, 10),
                'status': 'Active',
                'description': 'PGCIL Power Grid Diploma Trainee 2026 for various engineering disciplines.',
            },
            {
                'title': 'CRPF Constable Tradesman Online Form 2026',
                'organization': self._org('crpf'),
                'exam_category': self._cat('police'),
                'state': None,
                'year': 2026, 'vacancies': 9212, 'job_level': 'D',
                'application_start_date': datetime.date(2026, 4, 20),
                'application_end_date': end_june,
                'status': 'Active',
                'description': 'CRPF Constable Tradesman recruitment 2026 for various trades.',
            },
            {
                'title': 'UPSSSC Assistant Boring Technician Online Form 2026',
                'organization': self._org('upsssc'),
                'exam_category': self._cat('engineering'),
                'state': self._state('UP'),
                'year': 2026, 'vacancies': 585, 'job_level': 'C',
                'application_start_date': datetime.date(2026, 4, 22),
                'application_end_date': end_may,
                'status': 'Active',
                'description': 'UPSSSC Assistant Boring Technician 2026 for UP Jal Nigam.',
            },
            {
                'title': 'SSC Selection Post Phase 14 Online Form 2026',
                'organization': self._org('ssc'),
                'exam_category': self._cat('ssc-central'),
                'state': None,
                'year': 2026, 'vacancies': 2000, 'job_level': 'C',
                'application_start_date': datetime.date(2026, 4, 28),
                'application_end_date': end_may,
                'status': 'Active',
                'description': 'SSC Selection Post Phase 14 2026 for 10th, 12th and Graduate level posts.',
            },
        ]

        created_count = 0
        for job in jobs:
            if not job.get('organization'):
                self.stdout.write(self.style.WARNING(f'  Skipped (no org): {job["title"]}'))
                continue
            if JobPosting.objects.filter(title=job['title'], year=job['year']).exists():
                continue
            slug = safe_slug(job['title'], JobPosting)
            JobPosting.objects.create(
                title=job['title'],
                slug=slug,
                description=job.get('description', ''),
                organization=job['organization'],
                exam_category=job.get('exam_category'),
                state=job.get('state'),
                year=job['year'],
                vacancies=job.get('vacancies', 0),
                job_level=job.get('job_level', 'C'),
                application_start_date=job.get('application_start_date'),
                application_end_date=job.get('application_end_date'),
                status=job.get('status', 'Active'),
            )
            created_count += 1
        self.stdout.write(self.style.SUCCESS(f'  Jobs created: {created_count}'))

    # ------------------------------------------------------------------
    # Exam Results
    # ------------------------------------------------------------------

    def _add_results(self):
        results = [
            {'exam_name': 'MPESB MP Police ASI HC Computer Result', 'exam_year': 2026,
             'organization': self._org('mpesb'), 'exam_category': self._cat('police'), 'state': self._state('MP'),
             'result_date': datetime.date(2026, 5, 5), 'is_official': True,
             'description': 'MPESB MP Police ASI and Head Constable Computer Operator Result 2026 declared.'},
            {'exam_name': 'IDBI Bank JAM Assistant Manager Result', 'exam_year': 2026,
             'organization': self._org('idbi-bank'), 'exam_category': self._cat('bank'), 'state': None,
             'result_date': datetime.date(2026, 5, 1), 'is_official': True,
             'description': 'IDBI Bank Junior Assistant Manager (JAM) & Assistant Manager Result 2026.'},
            {'exam_name': 'UPSC CDS I Result', 'exam_year': 2026,
             'organization': self._org('upsc'), 'exam_category': self._cat('defence'), 'state': None,
             'result_date': datetime.date(2026, 4, 28), 'is_official': True,
             'description': 'UPSC Combined Defence Services CDS I 2026 Written Exam Result.'},
            {'exam_name': 'UPSC IFS Final Result', 'exam_year': 2025,
             'organization': self._org('upsc'), 'exam_category': self._cat('civil-service'), 'state': None,
             'result_date': datetime.date(2026, 4, 20), 'is_official': True,
             'description': 'UPSC Indian Forest Service IFS 2025 Final Result declared.'},
            {'exam_name': 'UPSC NDA I Result', 'exam_year': 2026,
             'organization': self._org('upsc'), 'exam_category': self._cat('defence'), 'state': None,
             'result_date': datetime.date(2026, 5, 3), 'is_official': True,
             'description': 'UPSC NDA I National Defence Academy 2026 Written Exam Result.'},
            {'exam_name': 'RRB Railway Section Officer Result Score Card', 'exam_year': 2026,
             'organization': self._org('rrb'), 'exam_category': self._cat('railway'), 'state': None,
             'result_date': datetime.date(2026, 4, 15), 'is_official': True,
             'description': 'RRB Railway Section Officer Score Card 2026 released.'},
            {'exam_name': 'IB Security Assistant Executive Tier II Result', 'exam_year': 2026,
             'organization': self._org('ib-mha'), 'exam_category': self._cat('police'), 'state': None,
             'result_date': datetime.date(2026, 5, 6), 'is_official': True,
             'description': 'IB ACIO Security Assistant Executive Tier II Result 2026.'},
            {'exam_name': 'UP Police Sub Inspector SI Result', 'exam_year': 2026,
             'organization': self._org('up-police'), 'exam_category': self._cat('police'), 'state': self._state('UP'),
             'result_date': datetime.date(2026, 5, 2), 'is_official': True,
             'description': 'UP Police Sub Inspector SI Written Exam Result 2026.'},
            {'exam_name': 'RRB NTPC CEN 05 2024 Final Result', 'exam_year': 2024,
             'organization': self._org('rrb'), 'exam_category': self._cat('railway'), 'state': None,
             'result_date': datetime.date(2026, 4, 25), 'is_official': True,
             'description': 'Railway RRB NTPC CEN 05/2024 Final Result and Document Verification list.'},
            {'exam_name': 'DDA Stenographer Final Result', 'exam_year': 2025,
             'organization': self._org('dda'), 'exam_category': self._cat('ssc-central'), 'state': self._state('DL'),
             'result_date': datetime.date(2026, 4, 18), 'is_official': True,
             'description': 'DDA Stenographer 2025 Final Selection Result declared.'},
            {'exam_name': 'BPSSC Range Officer Forests Marksheet', 'exam_year': 2025,
             'organization': self._org('bpssc'), 'exam_category': self._cat('state-psc'), 'state': self._state('BR'),
             'result_date': datetime.date(2026, 4, 22), 'is_official': True,
             'description': 'BPSSC Range Officer Forests 2025 Final Result Marksheet released.'},
            {'exam_name': 'NABARD Assistant Manager Grade A Final Result', 'exam_year': 2026,
             'organization': self._org('nabard'), 'exam_category': self._cat('bank'), 'state': None,
             'result_date': datetime.date(2026, 5, 7), 'is_official': True,
             'description': 'NABARD Assistant Manager Grade A 2026 Final Result declared.'},
            {'exam_name': 'NTA JEE MAIN Session II Paper 2 Result', 'exam_year': 2026,
             'organization': self._org('nta'), 'exam_category': self._cat('engineering'), 'state': None,
             'result_date': datetime.date(2026, 4, 30), 'is_official': True,
             'description': 'NTA JEE Main 2026 Session II Paper 2 (B.Arch / B.Planning) Result.'},
            {'exam_name': 'Bihar OFSS 11th Admission First Merit List Cutoff', 'exam_year': 2026,
             'organization': self._org('bpsc'), 'exam_category': self._cat('admission'), 'state': self._state('BR'),
             'result_date': datetime.date(2026, 5, 8), 'is_official': True,
             'description': 'Bihar OFSS 11th Class First Merit List and Category-wise Cutoff 2026.'},
            {'exam_name': 'RSSB Jail Prahari Final Result', 'exam_year': 2024,
             'organization': self._org('rssb'), 'exam_category': self._cat('police'), 'state': self._state('RJ'),
             'result_date': datetime.date(2026, 4, 12), 'is_official': True,
             'description': 'RSSB Rajasthan Jail Prahari 2024 Final Selection Result.'},
            {'exam_name': 'HPSC HCS Pre Result', 'exam_year': 2026,
             'organization': self._org('hpsc'), 'exam_category': self._cat('state-psc'), 'state': self._state('HR'),
             'result_date': datetime.date(2026, 5, 4), 'is_official': True,
             'description': 'HPSC Haryana Civil Services HCS Pre 2026 Written Exam Result.'},
            {'exam_name': 'MHA IB SA MT Final Result', 'exam_year': 2025,
             'organization': self._org('ib-mha'), 'exam_category': self._cat('police'), 'state': None,
             'result_date': datetime.date(2026, 4, 26), 'is_official': True,
             'description': 'MHA IB Security Assistant & Multi-Tasking Staff 2025 Final Result.'},
            {'exam_name': 'UPPSC APO Pre Result', 'exam_year': 2025,
             'organization': self._org('uppsc'), 'exam_category': self._cat('state-psc'), 'state': self._state('UP'),
             'result_date': datetime.date(2026, 5, 1), 'is_official': True,
             'description': 'UPPSC Assistant Prosecution Officer 2025 Preliminary Exam Result.'},
            {'exam_name': 'UPSSSC Sachiv Grade II Final Result', 'exam_year': 2024,
             'organization': self._org('upsssc'), 'exam_category': self._cat('state-psc'), 'state': self._state('UP'),
             'result_date': datetime.date(2026, 4, 20), 'is_official': True,
             'description': 'UPSSSC Gram Panchayat Sachiv Grade II 2024 Final Result declared.'},
            {'exam_name': 'UPSSSC Forest Guard PET Result', 'exam_year': 2023,
             'organization': self._org('upsssc'), 'exam_category': self._cat('state-psc'), 'state': self._state('UP'),
             'result_date': datetime.date(2026, 5, 5), 'is_official': True,
             'description': 'UPSSSC Forest Guard 2023 Physical Efficiency Test PET Result.'},
            {'exam_name': 'UPSSSC Enforcement Constable PET Result', 'exam_year': 2023,
             'organization': self._org('upsssc'), 'exam_category': self._cat('police'), 'state': self._state('UP'),
             'result_date': datetime.date(2026, 5, 5), 'is_official': True,
             'description': 'UPSSSC Enforcement Constable 2023 PET Result released.'},
            {'exam_name': 'SSC Delhi Police Constable Driver Result', 'exam_year': 2026,
             'organization': self._org('ssc'), 'exam_category': self._cat('police'), 'state': self._state('DL'),
             'result_date': datetime.date(2026, 4, 28), 'is_official': True,
             'description': 'SSC Delhi Police Constable (Driver) 2026 Written Exam Result.'},
            {'exam_name': 'UPPSC Assistant Registrar Final Result', 'exam_year': 2024,
             'organization': self._org('uppsc'), 'exam_category': self._cat('state-psc'), 'state': self._state('UP'),
             'result_date': datetime.date(2026, 4, 15), 'is_official': True,
             'description': 'UPPSC Assistant Registrar 2024 Final Result declared.'},
        ]

        created_count = 0
        for r in results:
            if not r.get('organization'):
                continue
            if ExamResult.objects.filter(exam_name=r['exam_name'], exam_year=r['exam_year']).exists():
                continue
            slug = safe_slug(r['exam_name'] + ' ' + str(r['exam_year']), ExamResult)
            ExamResult.objects.create(
                exam_name=r['exam_name'],
                slug=slug,
                description=r.get('description', ''),
                organization=r['organization'],
                exam_category=r.get('exam_category'),
                state=r.get('state'),
                exam_year=r['exam_year'],
                result_date=r.get('result_date'),
                is_official=r.get('is_official', False),
            )
            created_count += 1
        self.stdout.write(self.style.SUCCESS(f'  Results created: {created_count}'))

    # ------------------------------------------------------------------
    # Admit Cards
    # ------------------------------------------------------------------

    def _add_admit_cards(self):
        today = datetime.date.today()
        cards = [
            {'exam_name': 'MPESB Nursing Officer Sister Tutor Admit Card 2026',
             'organization': self._org('mpesb'), 'exam_category': self._cat('medical'), 'state': self._state('MP'),
             'exam_date': datetime.date(2026, 6, 15), 'admit_card_date': datetime.date(2026, 5, 20),
             'download_link': 'https://esb.mp.gov.in', 'description': 'MPESB Nursing Officer and Sister Tutor Exam 2026 Admit Card.'},
            {'exam_name': 'Bihar Vidhan Parishad LDC DEO Admit Card 2026',
             'organization': self._org('bihar-vidhan-parishad'), 'exam_category': self._cat('state-psc'), 'state': self._state('BR'),
             'exam_date': datetime.date(2026, 6, 20), 'admit_card_date': datetime.date(2026, 5, 25),
             'download_link': 'https://biharvidhanparishad.gov.in', 'description': 'Bihar Vidhan Parishad LDC and DEO 2026 Exam Admit Card.'},
            {'exam_name': 'NIELIT CCC Admit Card May 2026',
             'organization': self._org('nielit'), 'exam_category': self._cat('ssc-central'), 'state': None,
             'exam_date': datetime.date(2026, 5, 24), 'admit_card_date': datetime.date(2026, 5, 10),
             'download_link': 'https://nielit.gov.in', 'description': 'NIELIT CCC Exam May 2026 Admit Card.'},
            {'exam_name': 'UP PGT 2022 Admit Card',
             'organization': self._org('uphesc'), 'exam_category': self._cat('teaching'), 'state': self._state('UP'),
             'exam_date': datetime.date(2026, 6, 5), 'admit_card_date': datetime.date(2026, 5, 15),
             'download_link': 'https://uphesc.org', 'description': 'UP PGT 2022 Exam Admit Card released for written examination.'},
            {'exam_name': 'Indian Army Agniveer CEE Admit Card 2026',
             'organization': self._org('indian-army'), 'exam_category': self._cat('defence'), 'state': None,
             'exam_date': datetime.date(2026, 6, 25), 'admit_card_date': datetime.date(2026, 5, 30),
             'download_link': 'https://joinindianarmy.nic.in', 'description': 'Indian Army Agniveer CEE 2026 Common Entrance Exam Admit Card.'},
            {'exam_name': 'RRB NTPC UG CEN 07 2025 Admit Card',
             'organization': self._org('rrb'), 'exam_category': self._cat('railway'), 'state': None,
             'exam_date': datetime.date(2026, 6, 10), 'admit_card_date': datetime.date(2026, 5, 25),
             'download_link': 'https://www.rrbcdg.gov.in', 'description': 'Railway RRB NTPC UG CEN 07/2025 CBT Exam Admit Card.'},
            {'exam_name': 'RSSB Lab Assistant Admit Card 2026',
             'organization': self._org('rssb'), 'exam_category': self._cat('medical'), 'state': self._state('RJ'),
             'exam_date': datetime.date(2026, 6, 1), 'admit_card_date': datetime.date(2026, 5, 18),
             'download_link': 'https://rsmssb.rajasthan.gov.in', 'description': 'RSSB Rajasthan Lab Assistant Exam 2026 Admit Card.'},
            {'exam_name': 'Navy SSR Medical Admit Card 2026',
             'organization': self._org('indian-navy'), 'exam_category': self._cat('defence'), 'state': None,
             'exam_date': datetime.date(2026, 5, 28), 'admit_card_date': datetime.date(2026, 5, 12),
             'download_link': 'https://www.joinindiannavy.gov.in', 'description': 'Indian Navy SSR Medical Exam 2026 Admit Card.'},
            {'exam_name': 'Navy SSR MR INET Admit Card 2026',
             'organization': self._org('indian-navy'), 'exam_category': self._cat('defence'), 'state': None,
             'exam_date': datetime.date(2026, 6, 5), 'admit_card_date': datetime.date(2026, 5, 20),
             'download_link': 'https://www.joinindiannavy.gov.in', 'description': 'Navy SSR and MR INET Online Exam 2026 Admit Card.'},
            {'exam_name': 'UPPSC GIC Lecturer New Exam Date 2026',
             'organization': self._org('uppsc'), 'exam_category': self._cat('teaching'), 'state': self._state('UP'),
             'exam_date': datetime.date(2026, 7, 10), 'admit_card_date': datetime.date(2026, 6, 25),
             'download_link': 'https://uppsc.up.nic.in', 'description': 'UPPSC GIC Lecturer New Exam Date 2026 Admit Card.'},
            {'exam_name': 'UPPSC LT Grade Assistant Teacher Mains Exam Date 2026',
             'organization': self._org('uppsc'), 'exam_category': self._cat('teaching'), 'state': self._state('UP'),
             'exam_date': datetime.date(2026, 7, 20), 'admit_card_date': datetime.date(2026, 7, 5),
             'download_link': 'https://uppsc.up.nic.in', 'description': 'UPPSC LT Grade Assistant Teacher Mains 2026 New Exam Date.'},
            {'exam_name': 'NTA CUET UG 2026 Admit Card',
             'organization': self._org('nta'), 'exam_category': self._cat('admission'), 'state': None,
             'exam_date': datetime.date(2026, 5, 15), 'admit_card_date': datetime.date(2026, 5, 8),
             'download_link': 'https://cuet.samarth.ac.in', 'description': 'NTA CUET UG 2026 Common University Entrance Test Admit Card.'},
            {'exam_name': 'UPSSSC Lekhpal Mains Exam Fee Payment 2026',
             'organization': self._org('upsssc'), 'exam_category': self._cat('state-psc'), 'state': self._state('UP'),
             'exam_date': datetime.date(2026, 7, 15), 'admit_card_date': datetime.date(2026, 7, 1),
             'download_link': 'https://upsssc.gov.in', 'description': 'UPSSSC Lekhpal Mains 2026 Exam Fee Payment and Exam Date.'},
            {'exam_name': 'MP PAT 2026 Admit Card',
             'organization': self._org('mpesb'), 'exam_category': self._cat('admission'), 'state': self._state('MP'),
             'exam_date': datetime.date(2026, 6, 8), 'admit_card_date': datetime.date(2026, 5, 22),
             'download_link': 'https://esb.mp.gov.in', 'description': 'MP Pre Agriculture Test PAT 2026 Exam Admit Card.'},
            {'exam_name': 'BSSC Office Attendant 2022 Exam Date',
             'organization': self._org('bssc'), 'exam_category': self._cat('state-psc'), 'state': self._state('BR'),
             'exam_date': datetime.date(2026, 6, 14), 'admit_card_date': datetime.date(2026, 5, 30),
             'download_link': 'https://bssc.bihar.gov.in', 'description': 'BSSC Office Attendant 2022 Exam Date 2026 Admit Card.'},
            {'exam_name': 'BPSSC Sub Inspector 2025 Mains Exam Date',
             'organization': self._org('bpssc'), 'exam_category': self._cat('police'), 'state': self._state('BR'),
             'exam_date': datetime.date(2026, 6, 28), 'admit_card_date': datetime.date(2026, 6, 10),
             'download_link': 'https://bpssc.bih.nic.in', 'description': 'BPSSC Sub Inspector 2025 Mains Exam Date and Admit Card.'},
            {'exam_name': 'UPSSSC Junior Engineer JE Civil Admit Card 2026',
             'organization': self._org('upsssc'), 'exam_category': self._cat('engineering'), 'state': self._state('UP'),
             'exam_date': datetime.date(2026, 5, 30), 'admit_card_date': datetime.date(2026, 5, 12),
             'download_link': 'https://upsssc.gov.in', 'description': 'UPSSSC Junior Engineer JE Civil Exam 2026 Admit Card.'},
            {'exam_name': 'NTA NEET UG 2026 Exam Admit Card',
             'organization': self._org('nta'), 'exam_category': self._cat('medical'), 'state': None,
             'exam_date': datetime.date(2026, 5, 4), 'admit_card_date': datetime.date(2026, 4, 25),
             'download_link': 'https://neet.nta.nic.in', 'description': 'NTA NEET UG 2026 National Eligibility cum Entrance Test Admit Card.'},
            {'exam_name': 'BPSSC Havildar Exam Date 2026',
             'organization': self._org('bpssc'), 'exam_category': self._cat('police'), 'state': self._state('BR'),
             'exam_date': datetime.date(2026, 7, 5), 'admit_card_date': datetime.date(2026, 6, 18),
             'download_link': 'https://bpssc.bih.nic.in', 'description': 'BPSSC Havildar Instructor 2026 Exam Date and Admit Card.'},
            {'exam_name': 'SSC GD Constable 2025 Admit Card',
             'organization': self._org('ssc'), 'exam_category': self._cat('police'), 'state': None,
             'exam_date': datetime.date(2026, 5, 20), 'admit_card_date': datetime.date(2026, 5, 5),
             'download_link': 'https://ssc.nic.in', 'description': 'SSC GD Constable 2025 Physical Efficiency Test PET Admit Card.'},
            {'exam_name': 'MPESB Subedar Sub Inspector Second Phase Admit Card 2026',
             'organization': self._org('mpesb'), 'exam_category': self._cat('police'), 'state': self._state('MP'),
             'exam_date': datetime.date(2026, 6, 12), 'admit_card_date': datetime.date(2026, 5, 28),
             'download_link': 'https://esb.mp.gov.in', 'description': 'MPESB Subedar and Sub Inspector Second Phase Exam 2026 Admit Card.'},
            {'exam_name': 'NTA NTET 2026 Admit Card',
             'organization': self._org('nta'), 'exam_category': self._cat('teaching'), 'state': None,
             'exam_date': datetime.date(2026, 6, 18), 'admit_card_date': datetime.date(2026, 6, 1),
             'download_link': 'https://nta.ac.in', 'description': 'NTA National Teacher Eligibility Test NTET 2026 Admit Card.'},
            {'exam_name': 'JPSC Jharkhand Eligibility Test JET Admit Card 2026',
             'organization': self._org('jpsc'), 'exam_category': self._cat('teaching'), 'state': self._state('JH'),
             'exam_date': datetime.date(2026, 6, 22), 'admit_card_date': datetime.date(2026, 6, 5),
             'download_link': 'https://jpsc.gov.in', 'description': 'JPSC JET Jharkhand Teacher Eligibility Test 2026 Admit Card.'},
            {'exam_name': 'NTA NIFT Stage II Admit Card 2026',
             'organization': self._org('nta'), 'exam_category': self._cat('admission'), 'state': None,
             'exam_date': datetime.date(2026, 5, 18), 'admit_card_date': datetime.date(2026, 5, 8),
             'download_link': 'https://nta.ac.in', 'description': 'NTA NIFT Stage II Situational Test and Group Discussion Admit Card 2026.'},
            {'exam_name': 'NTA NCHM JEE Admit Card 2026',
             'organization': self._org('nta'), 'exam_category': self._cat('admission'), 'state': None,
             'exam_date': datetime.date(2026, 5, 10), 'admit_card_date': datetime.date(2026, 4, 28),
             'download_link': 'https://nchm.samarth.ac.in', 'description': 'NTA National Council of Hotel Management JEE 2026 Admit Card.'},
            {'exam_name': 'Delhi DSSSB Exam Date 2026',
             'organization': self._org('dsssb'), 'exam_category': self._cat('ssc-central'), 'state': self._state('DL'),
             'exam_date': datetime.date(2026, 6, 1), 'admit_card_date': datetime.date(2026, 5, 18),
             'download_link': 'https://dsssb.delhi.gov.in', 'description': 'DSSSB June–September 2026 Exam Date Schedule.'},
            {'exam_name': 'UP Police Home Guard Admit Card 2026',
             'organization': self._org('up-police'), 'exam_category': self._cat('police'), 'state': self._state('UP'),
             'exam_date': datetime.date(2026, 5, 25), 'admit_card_date': datetime.date(2026, 5, 10),
             'download_link': 'https://uppbpb.gov.in', 'description': 'UP Police Home Guard Recruitment 2026 Admit Card.'},
        ]

        created_count = 0
        for c in cards:
            if not c.get('organization'):
                continue
            if AdmitCard.objects.filter(
                exam_name=c['exam_name'], exam_date=c['exam_date']
            ).exists():
                continue
            slug = safe_slug(c['exam_name'], AdmitCard)
            AdmitCard.objects.create(
                exam_name=c['exam_name'],
                slug=slug,
                description=c.get('description', ''),
                organization=c['organization'],
                exam_category=c.get('exam_category'),
                state=c.get('state'),
                exam_date=c['exam_date'],
                admit_card_date=c['admit_card_date'],
                download_link=c['download_link'],
            )
            created_count += 1
        self.stdout.write(self.style.SUCCESS(f'  Admit Cards created: {created_count}'))

    # ------------------------------------------------------------------
    # Answer Keys
    # ------------------------------------------------------------------

    def _add_answer_keys(self):
        keys = [
            {'exam_name': 'NTA NCHMJEE Answer Key', 'exam_year': 2026,
             'organization': self._org('nta'), 'exam_category': self._cat('admission'), 'state': None,
             'exam_date': datetime.date(2026, 5, 10), 'answer_key_link': 'https://nchm.samarth.ac.in',
             'is_official': True, 'is_provisional': True,
             'description': 'NTA NCHM JEE 2026 Official Answer Key for objection filing.'},
            {'exam_name': 'UP Police Home Guard Answer Key', 'exam_year': 2026,
             'organization': self._org('up-police'), 'exam_category': self._cat('police'), 'state': self._state('UP'),
             'exam_date': datetime.date(2026, 4, 28), 'answer_key_link': 'https://uppbpb.gov.in',
             'is_official': True, 'is_provisional': True,
             'description': 'UP Police Home Guard Recruitment 2026 Written Exam Answer Key.'},
            {'exam_name': 'UP Police Sub Inspector SI Final Answer Key', 'exam_year': 2026,
             'organization': self._org('up-police'), 'exam_category': self._cat('police'), 'state': self._state('UP'),
             'exam_date': datetime.date(2026, 4, 10), 'answer_key_link': 'https://uppbpb.gov.in',
             'is_official': True, 'is_provisional': False,
             'description': 'UP Police Sub Inspector SI 2026 Final Answer Key declared.'},
            {'exam_name': 'NEET UG Answer Key', 'exam_year': 2026,
             'organization': self._org('nta'), 'exam_category': self._cat('medical'), 'state': None,
             'exam_date': datetime.date(2026, 5, 4), 'answer_key_link': 'https://neet.nta.nic.in',
             'is_official': True, 'is_provisional': True,
             'description': 'NTA NEET UG 2026 Provisional Answer Key released for challenge filing.'},
            {'exam_name': 'UPSSSC Junior Engineer JE Civil Answer Key', 'exam_year': 2024,
             'organization': self._org('upsssc'), 'exam_category': self._cat('engineering'), 'state': self._state('UP'),
             'exam_date': datetime.date(2024, 11, 15), 'answer_key_link': 'https://upsssc.gov.in',
             'is_official': True, 'is_provisional': True,
             'description': 'UPSSSC JE Civil 2024 Exam Official Answer Key for objections.'},
        ]

        created_count = 0
        for k in keys:
            if not k.get('organization'):
                continue
            if AnswerKey.objects.filter(
                exam_name=k['exam_name'], exam_year=k['exam_year'], shift_number=1
            ).exists():
                continue
            slug = safe_slug(k['exam_name'] + ' ' + str(k['exam_year']), AnswerKey)
            AnswerKey.objects.create(
                exam_name=k['exam_name'],
                slug=slug,
                description=k.get('description', ''),
                organization=k['organization'],
                exam_category=k.get('exam_category'),
                state=k.get('state'),
                exam_year=k['exam_year'],
                exam_date=k['exam_date'],
                answer_key_link=k['answer_key_link'],
                is_official=k.get('is_official', False),
                is_provisional=k.get('is_provisional', False),
            )
            created_count += 1
        self.stdout.write(self.style.SUCCESS(f'  Answer Keys created: {created_count}'))

    # ------------------------------------------------------------------
    # Syllabi
    # ------------------------------------------------------------------

    def _add_syllabi(self):
        syllabi = [
            {'exam_name': 'UPSSSC UP Vidhan Bhawan Guard Fireman Syllabus', 'exam_year': 2026,
             'organization': self._org('upsssc'), 'exam_category': self._cat('state-psc'), 'state': self._state('UP'),
             'subjects': 'General Hindi, General Knowledge, Elementary Arithmetic, Reasoning',
             'description': 'UPSSSC UP Vidhan Bhawan Guard and Fireman 2026 Official Syllabus.'},
            {'exam_name': 'MPESB Nursing Officer Sister Tutor Syllabus', 'exam_year': 2026,
             'organization': self._org('mpesb'), 'exam_category': self._cat('medical'), 'state': self._state('MP'),
             'subjects': 'Anatomy, Physiology, Biochemistry, Pharmacology, Nutrition, Medical-Surgical Nursing, Community Health Nursing',
             'description': 'MPESB Nursing Officer and Sister Tutor 2026 Exam Detailed Syllabus.'},
            {'exam_name': 'Patna High Court Technical Assistant Syllabus', 'exam_year': 2026,
             'organization': self._org('patna-high-court'), 'exam_category': self._cat('engineering'), 'state': self._state('BR'),
             'subjects': 'Computer Science, General Knowledge, English, Mathematics, Reasoning',
             'description': 'Patna High Court Technical Assistant 2026 Exam Syllabus and Exam Pattern.'},
            {'exam_name': 'Jharkhand Teacher Eligibility Test JHTET Syllabus', 'exam_year': 2026,
             'organization': self._org('jharkhand-psc'), 'exam_category': self._cat('teaching'), 'state': self._state('JH'),
             'subjects': 'Child Development and Pedagogy, Language I (Hindi/English), Language II, Mathematics, Environmental Studies',
             'description': 'JHTET 2026 Jharkhand Teacher Eligibility Test Paper I and Paper II Syllabus.'},
            {'exam_name': 'UPTET Syllabus', 'exam_year': 2026,
             'organization': self._org('uppsc'), 'exam_category': self._cat('teaching'), 'state': self._state('UP'),
             'subjects': 'Child Development & Pedagogy, Language I, Language II, Mathematics, Environmental Studies, Science, Social Studies',
             'description': 'UPTET 2026 Uttar Pradesh Teacher Eligibility Test Paper I and Paper II Syllabus.'},
        ]

        created_count = 0
        for s in syllabi:
            if not s.get('organization'):
                continue
            if Syllabus.objects.filter(exam_name=s['exam_name'], exam_year=s['exam_year']).exists():
                continue
            slug = safe_slug(s['exam_name'] + ' ' + str(s['exam_year']), Syllabus)
            Syllabus.objects.create(
                exam_name=s['exam_name'],
                slug=slug,
                organization=s['organization'],
                exam_category=s.get('exam_category'),
                state=s.get('state'),
                exam_year=s['exam_year'],
                subjects=s['subjects'],
            )
            created_count += 1
        self.stdout.write(self.style.SUCCESS(f'  Syllabi created: {created_count}'))

    # ------------------------------------------------------------------
    # Certificate Verifications
    # ------------------------------------------------------------------

    def _add_certificate_verifications(self):
        certs = [
            {'exam_name': 'CTET February 2026 Certificate Download',
             'organization': self._org('nta'), 'exam_category': self._cat('teaching'), 'year': 2026,
             'verification_link': 'https://ctet.nic.in',
             'instructions': 'Download CTET February 2026 Certificate from official portal using registration number.'},
            {'exam_name': 'NTA CSIR NET December 2025 E Certificate',
             'organization': self._org('nta'), 'exam_category': self._cat('teaching'), 'year': 2025,
             'verification_link': 'https://csirnet.nta.nic.in',
             'instructions': 'Download CSIR NET December 2025 E Certificate from NTA official portal.'},
            {'exam_name': 'NTA UGC NET December 2025 E Certificate Download',
             'organization': self._org('nta'), 'exam_category': self._cat('teaching'), 'year': 2025,
             'verification_link': 'https://ugcnet.nta.nic.in',
             'instructions': 'Download UGC NET December 2025 E Certificate from NTA portal.'},
            {'exam_name': 'NTA UGC NET December 2024 E Certificate Download',
             'organization': self._org('nta'), 'exam_category': self._cat('teaching'), 'year': 2024,
             'verification_link': 'https://ugcnet.nta.nic.in',
             'instructions': 'Download UGC NET December 2024 E Certificate from NTA portal.'},
        ]

        created_count = 0
        for c in certs:
            if not c.get('organization'):
                continue
            if CertificateVerification.objects.filter(exam_name=c['exam_name']).exists():
                continue
            slug = safe_slug(c['exam_name'], CertificateVerification)
            CertificateVerification.objects.create(
                exam_name=c['exam_name'],
                slug=slug,
                organization=c['organization'],
                exam_category=c.get('exam_category'),
                year=c.get('year'),
                verification_link=c['verification_link'],
                instructions=c.get('instructions', ''),
            )
            created_count += 1
        self.stdout.write(self.style.SUCCESS(f'  Certificate Verifications created: {created_count}'))

    # ------------------------------------------------------------------
    # Admissions
    # ------------------------------------------------------------------

    def _add_admissions(self):
        admissions = [
            {'name': 'UPBED 2026 Correction Edit Form',
             'institution_name': 'UP BEd Joint Entrance Examination', 'state': self._state('UP'),
             'exam_category': self._cat('admission'),
             'form_start_date': datetime.date(2026, 4, 20), 'form_end_date': datetime.date(2026, 5, 15),
             'form_link': 'https://upbed.in', 'status': 'Open',
             'eligibility': 'Graduation with 50% marks for general, 45% for reserved categories.'},
            {'name': 'UP CAHET Online Form 2026',
             'institution_name': 'UP Combined Agriculture and Technology Entrance Test', 'state': self._state('UP'),
             'exam_category': self._cat('admission'),
             'form_start_date': datetime.date(2026, 4, 15), 'form_end_date': datetime.date(2026, 5, 20),
             'form_link': 'https://cahetup.org', 'status': 'Open',
             'eligibility': '12th pass with PCB/PCM for agriculture engineering admissions.'},
            {'name': 'Allahabad University PGAT Admissions Online Form 2026',
             'institution_name': 'University of Allahabad', 'state': self._state('UP'),
             'exam_category': self._cat('admission'),
             'form_start_date': datetime.date(2026, 4, 1), 'form_end_date': datetime.date(2026, 5, 31),
             'form_link': 'https://www.allduniv.ac.in', 'status': 'Open',
             'eligibility': 'Graduation for PG admissions in various disciplines.'},
            {'name': 'JEECUP 2026 Online Form Extended',
             'institution_name': 'Joint Entrance Exam Council Uttar Pradesh', 'state': self._state('UP'),
             'exam_category': self._cat('admission'),
             'form_start_date': datetime.date(2026, 3, 1), 'form_end_date': datetime.date(2026, 5, 15),
             'form_link': 'https://jeecup.admissions.nic.in', 'status': 'Open',
             'eligibility': '10th pass for Polytechnic / Diploma courses.'},
            {'name': 'Bihar 2 Year BEd Admissions Online Form 2026',
             'institution_name': 'Bihar BEd CET Admission', 'state': self._state('BR'),
             'exam_category': self._cat('admission'),
             'form_start_date': datetime.date(2026, 4, 10), 'form_end_date': datetime.date(2026, 5, 25),
             'form_link': 'https://www.biharboardonline.bihar.gov.in', 'status': 'Open',
             'eligibility': 'Graduation with 50% marks for BEd admission in Bihar.'},
            {'name': 'UP GNM Entrance Exam UPGET Online Form 2026',
             'institution_name': 'UP General Nursing and Midwifery Entrance Test', 'state': self._state('UP'),
             'exam_category': self._cat('medical'),
             'form_start_date': datetime.date(2026, 4, 25), 'form_end_date': datetime.date(2026, 5, 31),
             'form_link': 'https://upnrhm.gov.in', 'status': 'Open',
             'eligibility': '12th pass with PCB and 45% marks for GNM nursing program.'},
            {'name': 'NTA JIPMAT 2026 Online Form',
             'institution_name': 'Joint Integrated Programme in Management Aptitude Test', 'state': None,
             'exam_category': self._cat('admission'),
             'form_start_date': datetime.date(2026, 4, 5), 'form_end_date': datetime.date(2026, 5, 10),
             'form_link': 'https://jipmat.nta.nic.in', 'status': 'Open',
             'eligibility': '10+2 with 60% for IIM Bodh Gaya and IIM Jammu 5 year IPM program.'},
            {'name': 'NTA CUET UG 2026 Update Subject Details',
             'institution_name': 'Common University Entrance Test (CUET UG)', 'state': None,
             'exam_category': self._cat('admission'),
             'form_start_date': datetime.date(2026, 3, 20), 'form_end_date': datetime.date(2026, 5, 5),
             'form_link': 'https://cuet.samarth.ac.in', 'status': 'Open',
             'eligibility': '12th pass or appearing for UG admissions in central and state universities.'},
            {'name': 'DUVASU Mathura PVT Admissions Online Form 2026',
             'institution_name': 'Deen Dayal Upadhyaya Veterinary University Mathura', 'state': self._state('UP'),
             'exam_category': self._cat('admission'),
             'form_start_date': datetime.date(2026, 4, 20), 'form_end_date': datetime.date(2026, 5, 31),
             'form_link': 'https://duvasu.ac.in', 'status': 'Open',
             'eligibility': '12th pass with PCB/PCM for Veterinary and Animal Science courses.'},
            {'name': 'Bihar ITICAT Admissions 2026 Online Form',
             'institution_name': 'Bihar ITI Common Admission Test', 'state': self._state('BR'),
             'exam_category': self._cat('admission'),
             'form_start_date': datetime.date(2026, 4, 15), 'form_end_date': datetime.date(2026, 5, 20),
             'form_link': 'https://bceceboard.bihar.gov.in', 'status': 'Open',
             'eligibility': '10th pass for ITI trade courses in Bihar.'},
            {'name': 'MUIT Noida Lucknow Admission Online Form 2026',
             'institution_name': 'Mewar University Institute of Technology', 'state': self._state('UP'),
             'exam_category': self._cat('admission'),
             'form_start_date': datetime.date(2026, 3, 15), 'form_end_date': datetime.date(2026, 6, 30),
             'form_link': 'https://muit.in', 'status': 'Open',
             'eligibility': '10+2 for BTech and other degree programs.'},
            {'name': 'UP CNET 2026 Online Form',
             'institution_name': 'UP Combined Nursing Entrance Test', 'state': self._state('UP'),
             'exam_category': self._cat('medical'),
             'form_start_date': datetime.date(2026, 4, 22), 'form_end_date': datetime.date(2026, 5, 31),
             'form_link': 'https://upnrhm.gov.in', 'status': 'Open',
             'eligibility': '12th with PCB 45% marks for nursing entrance test.'},
        ]

        created_count = 0
        for a in admissions:
            if AdmissionForm.objects.filter(name=a['name']).exists():
                continue
            slug = safe_slug(a['name'], AdmissionForm)
            AdmissionForm.objects.create(
                name=a['name'],
                slug=slug,
                institution_name=a['institution_name'],
                exam_category=a.get('exam_category'),
                state=a.get('state'),
                form_start_date=a['form_start_date'],
                form_end_date=a['form_end_date'],
                form_link=a['form_link'],
                eligibility=a.get('eligibility', ''),
                status=a.get('status', 'Open'),
            )
            created_count += 1
        self.stdout.write(self.style.SUCCESS(f'  Admissions created: {created_count}'))

    # ------------------------------------------------------------------
    # Board Results
    # ------------------------------------------------------------------

    def _add_board_results(self):
        board_results = [
            {'board': 'Maharashtra Board', 'exam_type': '10th', 'year': 2026,
             'result_link': 'https://mahresult.nic.in', 'result_date': datetime.date(2026, 5, 3),
             'is_declared': True, 'pass_percentage': 95.84},
            {'board': 'Maharashtra Board', 'exam_type': '12th', 'year': 2026,
             'result_link': 'https://mahresult.nic.in', 'result_date': datetime.date(2026, 5, 7),
             'is_declared': True, 'pass_percentage': 93.12},
            {'board': 'ICSE', 'exam_type': '10th', 'year': 2026,
             'result_link': 'https://www.cisce.org', 'result_date': datetime.date(2026, 5, 6),
             'is_declared': True, 'pass_percentage': 98.76},
            {'board': 'ICSE', 'exam_type': '12th', 'year': 2026,
             'result_link': 'https://www.cisce.org', 'result_date': datetime.date(2026, 5, 6),
             'is_declared': True, 'pass_percentage': 97.55},
        ]

        # Also create ExamResult entries for Chhattisgarh Board (not in BoardExamResult choices)
        cg_board_results = [
            {'exam_name': 'Chhattisgarh Board Class 10th Result', 'exam_year': 2026,
             'organization': self._org('cgbse'), 'state': self._state('CG'),
             'result_date': datetime.date(2026, 5, 5), 'is_official': True,
             'description': 'Chhattisgarh Board CGBSE Class 10th Result 2026 declared.'},
            {'exam_name': 'Chhattisgarh Board Class 12th Result', 'exam_year': 2026,
             'organization': self._org('cgbse'), 'state': self._state('CG'),
             'result_date': datetime.date(2026, 5, 5), 'is_official': True,
             'description': 'Chhattisgarh Board CGBSE Class 12th Result 2026 declared.'},
        ]

        created_count = 0
        for br in board_results:
            if BoardExamResult.objects.filter(
                board=br['board'], exam_type=br['exam_type'], year=br['year']
            ).exists():
                continue
            BoardExamResult.objects.create(**br)
            created_count += 1

        for r in cg_board_results:
            if not r.get('organization'):
                continue
            if ExamResult.objects.filter(exam_name=r['exam_name'], exam_year=r['exam_year']).exists():
                continue
            slug = safe_slug(r['exam_name'] + ' ' + str(r['exam_year']), ExamResult)
            ExamResult.objects.create(
                exam_name=r['exam_name'],
                slug=slug,
                description=r.get('description', ''),
                organization=r['organization'],
                state=r.get('state'),
                exam_year=r['exam_year'],
                result_date=r.get('result_date'),
                is_official=r.get('is_official', False),
            )
            created_count += 1

        self.stdout.write(self.style.SUCCESS(f'  Board Results created: {created_count}'))
