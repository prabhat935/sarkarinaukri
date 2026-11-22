"""
Job posts written for this site from the recruiting body's official
notification. Every fact here was checked against the notification PDF named
in the job's `source` note; the wording is our own.
"""
import datetime
from decimal import Decimal

from django.core.management.base import BaseCommand
from content.models import ExamCategory, JobPosting, Organization, State


ORGANIZATIONS = [
    {'name': 'NLC India Limited', 'slug': 'nlc-india', 'website': 'https://www.nlcindia.in'},
    {'name': 'SIDBI', 'slug': 'sidbi', 'website': 'https://www.sidbi.in'},
    {'name': 'ASRB (ICAR)', 'slug': 'asrb', 'website': 'https://www.asrb.gov.in'},
    {'name': 'DSSSB', 'slug': 'dsssb', 'website': 'https://dsssb.delhi.gov.in'},
    {'name': 'RRC Central Railway', 'slug': 'rrc-central-railway', 'website': 'https://www.rrccr.com'},
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
    {
        # Source: ASRB F. No. 2(2)/2025-Exam dated 11 Nov 2026 (official PDF on asrb.gov.in)
        'slug': 'asrb-icar-technical-assistant-t3-t4-2026',
        'title': 'ASRB ICAR Technical Assistant (T-3) and Senior Technical Assistant (T-4) Recruitment 2026 (1393 Posts)',
        'organization': 'asrb',
        'category': 'ssc-central',
        'vacancies': 1393,
        'application_start_date': datetime.date(2026, 11, 18),
        'application_end_date': datetime.date(2026, 12, 17),
        'exam_date': None,
        'max_age': 30,
        'min_age': 21,
        'salary_min': Decimal('29200'),
        'salary_max': Decimal('112400'),
        'application_fee': Decimal('300'),
        'application_link': 'https://www.asrb.gov.in',
        'meta_description': (
            'ICAR Technical Assistant 2026: 1393 T-3 and T-4 posts for agriculture, veterinary, fisheries, '
            'engineering, IT and library graduates. Apply by 17 Dec 2026.'
        ),
        'eligibility': (
            'A bachelor\'s degree in the subject that matches the functional group you apply for, completed '
            'by 17 December 2026. Agriculture group: B.Sc. Agriculture, Horticulture, Agricultural Engineering, '
            'Agro-forestry, Food Science, Biotechnology, Environmental Science, Home/Community Science or '
            'Natural Farming. Animal Science: B.V.Sc. & A.H. Fisheries: B.F.Sc. Workshop posts (Civil, '
            'Agricultural/Mechanical, Electrical, Electronics): B.E./B.Tech or a three-year diploma in that '
            'branch. Library: a bachelor\'s in Library (and Information) Science. IT: BCA, B.Sc. Computer '
            'Science/IT, or B.E./B.Tech in IT, CS or ECE.\n\n'
            'Age on 17 December 2026: 21 to 30 years. Upper age relaxation: 5 years for SC/ST, 3 years for '
            'OBC (Non-Creamy Layer), 10 years for PwBD, and 3 years after deducting military service for '
            'ex-servicemen. In-service ICAR technical staff can apply up to 40 (UR).'
        ),
        'description': (
            'The Agricultural Scientists Recruitment Board (ASRB) is holding the Centralized Combined '
            'Examination 2026 to fill 1393 technical posts in the Indian Council of Agricultural Research: '
            '1254 Technical Assistant (T-3) posts in ICAR institutes and 139 Senior Technical Assistant (T-4) '
            'posts in Krishi Vigyan Kendras (KVKs). Most posts are for agriculture, veterinary and fisheries '
            'graduates, but there are also engineering, IT and library posts.\n\n'
            'Where the T-3 vacancies are: Agriculture 699 (476 field/farm technician and 223 laboratory '
            'technician), Information Technology 133, Animal Science 115, Fisheries 90, Library 59, Workshop '
            'Civil 51, Workshop Agricultural Engineering 42, Workshop Electrical 35, Workshop Electronics 25, '
            'and Home/Community Science 5. The T-4 posts in KVKs are Agriculture 73, IT 48, Animal Science 9, '
            'Fisheries 7 and Home/Community Science 2. ASRB says these numbers are tentative.\n\n'
            'Choose your group carefully. You can apply in only one functional group, even if your degree fits '
            'more than one. Within that group you can ask to be considered for T-3, T-4 or both, and if you pick '
            'both you must rank them. That order of preference cannot be changed later.\n\n'
            'How selection works: there is no interview. First comes a one-hour preliminary test of 100 '
            'questions (General Knowledge, General English, Quantitative Aptitude and General Agriculture, 25 '
            'each), with 0.25 marks deducted for each wrong answer. It only qualifies you: you need 30% (UR), '
            '25% (EWS/OBC) or 20% (SC/ST/PwBD), and about 15 candidates per vacancy in each group go through to '
            'the mains. The mains is a two-hour, 300-mark paper of 100 questions on your own subject, with one '
            'mark cut for each wrong answer. Your mains score alone decides the final merit list. Both papers '
            'are computer-based and in Hindi and English.\n\n'
            'Pay: T-3 is at Pay Level 5 (Rs 29,200 to 92,300) and T-4 at Pay Level 6 (Rs 35,400 to 1,12,400), '
            'plus central government allowances.\n\n'
            'Fee: Rs 300 for one post (T-3 or T-4) or Rs 600 for both if you are UR; Rs 150 or Rs 300 for EWS '
            'and OBC. Women, SC, ST, PwBD, transgender and ex-servicemen candidates pay nothing. The fee is paid '
            'through Bharatkosh, and a payment without a submitted form is neither counted nor refunded.\n\n'
            'Important dates: apply online at asrb.gov.in from 18 November to 17 December 2026 (11:59 pm); fee '
            'payment closes at the same time. A correction window runs from 18 to 20 December 2026. The '
            'preliminary exam is expected in February 2027, and the mains date will be announced later.\n\n'
            'Tips: ASRB checks documents only after the final result, so a wrong category or a certificate in '
            'the wrong format can cost you the job at the last step. Get your caste, EWS or OBC (Non-Creamy '
            'Layer) certificate in the central government format before you apply; our guides on these '
            'certificates list the usual mistakes. Since the mains carries a full one-mark penalty on a '
            'three-mark question, read our negative marking guide before deciding how much to guess.'
        ),
    },
    {
        # Source: DSSSB Advertisement No. 06/2026 dated 06 Nov 2026 (official PDF on dsssb.delhi.gov.in)
        'slug': 'dsssb-mts-junior-engineer-electrical-2026',
        'title': 'DSSSB MTS and Junior Engineer (Electrical) Recruitment 2026 (1260 Posts, Advt. 06/2026)',
        'organization': 'dsssb',
        'category': 'state-psc',
        'state': 'Delhi',
        'vacancies': 1260,
        'application_start_date': datetime.date(2026, 11, 12),
        'application_end_date': datetime.date(2026, 12, 11),
        'exam_date': None,
        'max_age': 27,
        'min_age': 18,
        'salary_min': Decimal('18000'),
        'salary_max': Decimal('151100'),
        'application_fee': Decimal('100'),
        'application_link': 'https://dsssbonline.nic.in',
        'meta_description': (
            'DSSSB 2026: 1075 MTS posts for 10th pass and 185 Junior Engineer (Electrical) posts in Delhi. '
            'Age 18-27, fee Rs 100, last date 11 Dec 2026.'
        ),
        'eligibility': (
            'Multi-Tasking Staff (all departments): 10th (Matriculation) pass from a recognised board; for the '
            'DUSIB MTS post an ITI pass also qualifies. Age 18 to 27 years.\n\n'
            'Junior Engineer (Electrical): Delhi Transco and DUSIB accept a degree or a diploma in Electrical '
            'Engineering with no experience. NDMC and MCD need a degree, or a diploma plus 2 years of '
            'professional experience. Delhi Agricultural Marketing Board needs a diploma plus 2 years of '
            'electrical installation or maintenance work. Age 18 to 27 years, except NDMC (18 to 32).\n\n'
            'Eligibility and age are judged on 11 December 2026. Upper age relaxation: 5 years for SC/ST, '
            '3 years for OBC, 10 years for PwBD (15 for PwBD SC/ST, 13 for PwBD OBC), plus further relaxation '
            'for ex-servicemen, departmental candidates and, for Group C posts, widowed or divorced women (up '
            'to 35). OBC relaxation and reservation apply only to holders of an OBC (Delhi) certificate.'
        ),
        'description': (
            'The Delhi Subordinate Services Selection Board (DSSSB) has announced 1260 posts under Advertisement '
            'No. 06/2026: 1075 Multi-Tasking Staff posts open to 10th-pass candidates, and 185 Junior Engineer '
            '(Electrical) posts for electrical diploma and degree holders. The jobs are in departments and local '
            'bodies of the Government of NCT of Delhi.\n\n'
            'MTS vacancies (post code 810/26): Directorate of Education 757 MTS (General Duty) and 239 MTS Aaya '
            '(women only), Department of Trade and Taxes 26, DUSIB 20, Weights and Measures 19, Land and '
            'Building 7, Directorate of Higher Education 3, Principal Accounts Office 2 and the Chief Electoral '
            'Officer 2. MTS posts are Group C at Pay Level 1 (Rs 18,000 to 56,900).\n\n'
            'Junior Engineer vacancies (post code 809/26): Delhi Transco 75, NDMC 67, MCD 26, DUSIB 14 and the '
            'Delhi Agricultural Marketing Board 3. These are Group B posts at Pay Level 6 (Rs 35,400 to '
            '1,12,400), except Delhi Transco, which is at Pay Level 8. Delhi Transco also accepts fresh diploma '
            'holders, so it is the best fit for most new electrical diploma graduates. Note that the '
            'qualification rules differ by department (see Eligibility).\n\n'
            'Exam pattern: MTS candidates take a single two-hour computer-based test of 200 one-mark questions, '
            '40 each on General Awareness, Reasoning, Arithmetic, Hindi and English. JE candidates take two '
            'tiers. Tier I (two hours) has 100 general questions and 100 electrical engineering questions; it '
            'only shortlists you for Tier II. Tier II (two and a half hours) has 100 one-mark and 50 two-mark '
            'questions on electrical engineering, and its marks decide the merit list. Wrong answers cost 0.25 '
            'marks on one-mark questions and 0.50 on two-mark questions. The minimum qualifying marks are 40% '
            'for General/EWS, 35% for OBC (Delhi) and 30% for SC/ST/PwBD.\n\n'
            'Fee: Rs 100, paid online through SBI e-pay. Women and SC, ST, PwBD and ex-servicemen candidates '
            'do not pay.\n\n'
            'Important dates: apply only online at dsssbonline.nic.in from 12 November 2026 (noon) to 11 '
            'December 2026 (11:59 pm). DSSSB will announce exam dates on its website later.\n\n'
            'Tips: if you are OBC from outside Delhi, you must apply as Unreserved, because DSSSB gives OBC '
            'benefits only for an OBC (Delhi) certificate issued on or before 11 December 2026. You cannot '
            'change any detail, including category, after you submit the form, so check it twice. The MTS test '
            'gives Hindi and English 40 marks each, as much as General Awareness or Arithmetic, so practise '
            'both languages instead of treating them as easy marks.'
        ),
    },
    {
        # Source: RRC Central Railway Notification No. RRC/CR/AA/2026 dated 03 Nov 2026 (official PDF on rrccr.com)
        'slug': 'rrc-central-railway-act-apprentice-2026',
        'title': 'Central Railway Act Apprentice Recruitment 2026 (2861 Slots, 10th + ITI, No Exam)',
        'organization': 'rrc-central-railway',
        'category': 'railway',
        'vacancies': 2861,
        'application_start_date': datetime.date(2026, 11, 3),
        'application_end_date': datetime.date(2026, 12, 2),
        'exam_date': None,
        'max_age': 24,
        'min_age': 15,
        'salary_min': Decimal('9600'),
        'salary_max': Decimal('9600'),
        'application_fee': Decimal('100'),
        'application_link': 'https://www.rrccr.com',
        'meta_description': (
            'Central Railway Apprentice 2026: 2861 slots for 10th pass with ITI, merit-based with no exam, '
            'Rs 9,600 stipend. Apply at rrccr.com by 2 Dec 2026, 5 pm.'
        ),
        'eligibility': (
            'Class 10 (or equivalent) passed with at least 50% aggregate marks, plus an ITI certificate (NCVT, or '
            'a provisional NCVT/SCVT certificate) in the trade you apply for. Engineering graduates and diploma '
            'holders cannot apply under this notification.\n\n'
            'Age on 3 November 2026: at least 15 and below 24 (UR candidates born between 3 November 2002 and '
            '3 November 2011). Upper age relaxation: 5 years for SC/ST, 3 years for OBC, 10 years for PwBD, and '
            'extra relaxation for ex-servicemen based on their service.'
        ),
        'description': (
            'Railway Recruitment Cell, Central Railway (Mumbai) is taking online applications for 2861 Act '
            'Apprentice training slots under the Apprentices Act 1961 (Notification No. RRC/CR/AA/2026). The '
            'training is at Central Railway workshops, loco sheds, carriage and wagon depots and other units in '
            'five clusters: Mumbai, Bhusawal, Pune, Nagpur and Solapur.\n\n'
            'There is no written test or interview. RRC makes a merit list from the simple average of your '
            'Class 10 percentage and your ITI percentage in the trade you apply for. The merit list is made '
            'separately for each cluster, unit, trade and category. If two candidates have the same marks, the '
            'older one ranks higher, and if the dates of birth also match, the one who passed Class 10 earlier.\n\n'
            'Trades include Fitter, Electrician, Welder, Turner, Machinist, several Mechanic trades, Painter, '
            'Carpenter, Mason, Crane Driver, Motor Mechanic and Stenographer (English or Hindi shorthand). The trade-wise slot tables in the notification show how many seats each unit has '
            'for your trade and category.\n\n'
            'Choose your cluster carefully. You may pick only one cluster, and within it you list the units you '
            'prefer. If you choose a cluster or unit with no slots for your ITI trade, your application is of '
            'no use, and you cannot edit it after final submission. Submitting more than one application gets '
            'all of them rejected.\n\n'
            'Training and stipend: one year of training for every trade, with a stipend of Rs 9,600 a month for '
            'National or State Trade Certificate holders. No hostel is provided. Completing the apprenticeship '
            'does not give you a right to a railway job.\n\n'
            'Fee: Rs 100 (non-refundable), paid online. SC, ST, PwBD and women candidates pay nothing.\n\n'
            'Important dates: apply only online at rrccr.com from 3 November 2026 (11 am) to 2 December 2026 '
            '(5 pm). Note the 5 pm deadline: the portal does not stay open until midnight on the last day.\n\n'
            'Tip for students with grades: if your board gave letter grades instead of marks, RRC asks you to '
            'enter the midpoint of the grade range (for example, 84.5 for an A grade covering 80 to 89). If '
            'there are only subject grades, average the midpoints of all subjects. Work this out before you fill '
            'in the form, because a mismatch between the figure you enter and RRC\'s own calculation leads to '
            'rejection.'
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
            extra = {}
            if data.get('state'):
                extra['state'] = State.objects.filter(name__iexact=data['state']).first()
            obj, created = JobPosting.objects.update_or_create(
                slug=data['slug'],
                defaults={
                    **extra,
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
