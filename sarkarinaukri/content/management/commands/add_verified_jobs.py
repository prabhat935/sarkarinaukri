"""
Job posts written for this site from the recruiting body's official
notification. Every fact here was checked against the notification PDF named
in the job's `source` note; the wording is our own.
"""
import datetime
from decimal import Decimal

from django.core.management.base import BaseCommand
from content.models import ExamCategory, JobPosting, Organization


ORGANIZATIONS = [
    {'name': 'NLC India Limited', 'slug': 'nlc-india', 'website': 'https://www.nlcindia.in'},
    {'name': 'SIDBI', 'slug': 'sidbi', 'website': 'https://www.sidbi.in'},
]


VERIFIED_JOBS = [
    {
        # Source: NLCIL Advt. No. 10/2026 (official PDF on nlcindia.in)
        'slug': 'nlc-graduate-executive-trainee-gate-2025',
        'title': 'NLC India Graduate Executive Trainee Recruitment 2026 (143 Posts through GATE 2025)',
        'organization': 'nlc-india',
        'category': 'engineering',
        'vacancies': 143,
        'application_start_date': datetime.date(2026, 11, 13),
        'application_end_date': datetime.date(2026, 12, 14),
        'exam_date': None,
        'max_age': 30,
        'min_age': None,
        'salary_min': Decimal('50000'),
        'salary_max': Decimal('160000'),
        'application_fee': Decimal('854'),
        'application_link': 'https://www.nlcindia.in',
        'meta_description': (
            'NLC India GET 2026: 143 posts via GATE 2025 in Mechanical, Electrical, Civil and Mining. '
            'Rs 50,000 basic pay, last date 14 Dec 2026.'
        ),
        'eligibility': (
            'A full-time or part-time bachelor\'s degree in Mechanical, Electrical, Civil or Mining '
            'Engineering (or the closely related branches listed in the notification), with at least '
            '60% marks (50% for SC/ST), held on 1 November 2026. You must also have a valid GATE 2025 '
            'score in the matching paper (ME, EE, CE or MN); scores from other GATE years are not accepted.\n\n'
            'Upper age limit on 1 November 2026: 30 years for UR/EWS, 33 for OBC (NCL), 35 for SC/ST, '
            'with further relaxation for PwBD and ex-servicemen as per government rules.'
        ),
        'description': (
            'NLC India Limited, the Navratna public sector company known for lignite mining and thermal '
            'power at Neyveli, is hiring 143 Graduate Executive Trainees (Advertisement No. 10/2026). '
            'There is no separate written test: candidates are selected on their GATE 2025 score and an '
            'interview, which makes this a good option for engineers who already have a strong GATE result.\n\n'
            'Posts by discipline: Mechanical 66, Electrical 44, Civil 23 and Mining 10. The vacancies are '
            'spread over four work areas: thermal power stations, mines and allied services, renewable '
            'energy and projects, and services and support. You choose your preferred area when applying, '
            'and postings can be at Neyveli (Tamil Nadu), Barsingsar (Rajasthan), Talabira (Odisha), South '
            'Pachwara (Jharkhand), solar and wind project sites, or joint ventures at Tuticorin and Ghatampur.\n\n'
            'How selection works: your GATE 2025 marks carry 80% of the final score and the interview 20%. '
            'NLC shortlists candidates for interview area by area, in order of GATE marks, keeping the '
            'reservation rules in mind. Ties are broken by age (the older candidate ranks higher) and then '
            'alphabetically.\n\n'
            'Pay and training: trainees spend one year in training on a basic pay of Rs 50,000 a month in '
            'the E-2 scale (Rs 50,000 to 1,60,000), plus dearness allowance and a 35% common allowance. '
            'NLC puts the cost to company at about Rs 14.5 lakh a year. After training, officers move to the '
            'E-3 grade with a basic pay of Rs 60,000. Selected candidates cannot ask for a transfer during '
            'their first three years.\n\n'
            'Fee: Rs 854 for UR, EWS and OBC (NCL) candidates (a Rs 500 application fee plus a Rs 354 '
            'processing fee). SC, ST, PwBD and ex-servicemen candidates pay only the Rs 354 processing fee.\n\n'
            'Important dates: online registration is open from 13 November 2026 (10 am) to 14 December 2026 '
            '(5 pm). The last time to pay the fee online is 14 December 2026 at 11:45 pm, and candidates who '
            'registered and paid in time can complete their application until 16 December 2026 (5 pm). '
            'Apply only through the official website, www.nlcindia.in; paper applications are not accepted.\n\n'
            'Before you apply: check that your degree branch exactly matches one in the notification, because '
            'NLC says equivalent or combined branches will not be considered. If your university gives a '
            'CGPA, the notification treats 6.0 on a 10-point scale as 60%, and percentages are not rounded '
            'up. Reserved category candidates need certificates in the central government format; see our '
            'guides to the EWS certificate and the OBC Non-Creamy Layer certificate for the common mistakes.'
        ),
    },
    {
        # Source: SIDBI Advertisement No. 8/Grade 'A' and 'B'/2026-27 (official PDF on sidbi.in)
        'slug': 'sidbi-assistant-manager-grade-a-b-2026',
        'title': 'SIDBI Assistant Manager Grade A and Manager Grade B Recruitment 2026 (68 Posts)',
        'organization': 'sidbi',
        'category': 'bank',
        'vacancies': 68,
        'application_start_date': datetime.date(2026, 11, 21),
        'application_end_date': datetime.date(2026, 12, 11),
        'exam_date': datetime.date(2026, 12, 27),
        'max_age': 30,
        'min_age': 21,
        'salary_min': Decimal('62500'),
        'salary_max': Decimal('126100'),
        'application_fee': None,
        'application_link': 'https://www.sidbi.in/en/careers',
        'meta_description': (
            'SIDBI Assistant Manager Grade A and Manager Grade B 2026: 68 posts, 2 years experience needed, '
            'exam 27 Dec 2026, last date 11 Dec 2026.'
        ),
        'eligibility': (
            'Assistant Manager Grade A (General stream): a graduation degree in Commerce, Economics, '
            'Mathematics, Statistics, Business Administration or Engineering with at least 60% marks (50% '
            'for SC/ST/PwBD), or CA, CS, CMA, CFA, or a full-time two-year MBA/PGDM. You also need at least '
            'two years of work experience as an officer after your qualification. The Hindi, Legal and IT '
            'streams, and the Grade B posts, have their own qualification and experience rules in the '
            'notification.\n\n'
            'Age on 21 November 2026: 21 to 30 years for Grade A (born between 21 November 1996 and 21 '
            'November 2005) and 25 to 33 years for Grade B. Relaxation: 5 years for SC/ST, 3 years for '
            'OBC (NCL), 10 years for PwBD.'
        ),
        'description': (
            'The Small Industries Development Bank of India (SIDBI), the main financial institution for the '
            'MSME sector, is recruiting officers under Advertisement No. 8/Grade A and B/2026-27. There are '
            '68 posts in total: 63 for Assistant Manager Grade A and 5 for Manager Grade B.\n\n'
            'Grade A posts by stream: General 53, Hindi 2, Legal 3 and IT 5. Grade B (specialist) posts: '
            'Hindi 1, Legal 3 and IT 1. The IT posts look for skills in AI/ML automation, full-stack '
            'development, security, or infrastructure and networking. You can apply for only one post; if '
            'you submit more than one application, only the latest complete one is kept.\n\n'
            'Note the experience requirement. Unlike most bank PO exams, the General stream is not open to '
            'fresh graduates: you need at least two years of officer-level work experience after your '
            'qualification, counted up to 11 December 2026. Read the experience conditions in the '
            'notification carefully before you pay the fee.\n\n'
            'Selection has three phases. Phase I is a 60-mark objective screening test (reasoning, English, '
            'quantitative aptitude and general awareness, 15 questions each, 60 minutes in total). Phase II '
            'carries 200 marks: an English descriptive paper and a stream-specific paper. Phase I and II are '
            'held on the same day, and Phase II is evaluated only for candidates who clear the Phase I '
            'cut-off. Phase III is a 100-mark interview, which can include marks for achievements in '
            'extracurricular activities if you have documents to show for them.\n\n'
            'Pay: Grade A officers are in the Rs 62,500 to 1,26,100 scale, with gross monthly pay of about '
            'Rs 1.2 lakh to start. SIDBI puts the yearly cost to company at Rs 30 to 34 lakh for Grade A and '
            'Rs 40 to 43 lakh for Grade B, depending on the place of posting. New officers are on probation '
            'for two years, which SIDBI can extend to four.\n\n'
            'Important dates: registration and fee payment are open from 21 November to 11 December 2026. '
            'The online exam (Phase I and II) is tentatively on 27 December 2026, and interviews are expected '
            'in February 2027. Check the official notification on sidbi.in for the application fee and the '
            'full syllabus.\n\n'
            'Preparing in the short time available: with the exam about two weeks after the last date, '
            'focus on speed in the Phase I sections and practise writing short essays and letters for the '
            'descriptive paper. Our guide to negative marking explains when an educated guess is worth '
            'taking in objective tests.'
        ),
    },
]


class Command(BaseCommand):
    help = 'Add job posts written from verified official notifications'

    def handle(self, *args, **options):
        for org in ORGANIZATIONS:
            Organization.objects.get_or_create(slug=org['slug'], defaults=org)

        for data in VERIFIED_JOBS:
            org = Organization.objects.get(slug=data['organization'])
            category = ExamCategory.objects.filter(slug=data['category']).first()
            end = data['application_end_date']
            obj, created = JobPosting.objects.update_or_create(
                slug=data['slug'],
                defaults={
                    'title': data['title'],
                    'organization': org,
                    'exam_category': category,
                    'year': 2026,
                    'vacancies': data['vacancies'],
                    'application_start_date': data['application_start_date'],
                    'application_end_date': end,
                    'exam_date': data['exam_date'],
                    'min_age': data['min_age'],
                    'max_age': data['max_age'],
                    'salary_min': data['salary_min'],
                    'salary_max': data['salary_max'],
                    'application_fee': data['application_fee'],
                    'application_link': data['application_link'],
                    'eligibility': data['eligibility'],
                    'description': data['description'],
                    'meta_description': data['meta_description'],
                    'status': 'Active' if end >= datetime.date.today() else 'Closed',
                },
            )
            self.stdout.write(f"  {'Created' if created else 'Updated'}: {obj.title[:60]} ({obj.status})")

        self.stdout.write(self.style.SUCCESS(f'\nDone. {len(VERIFIED_JOBS)} verified jobs.'))
