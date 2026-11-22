"""
Job posts written for this site from the recruiting body's official
notification. Every fact here was checked against the notification PDF named
in the job's `source` note; the wording is our own.
"""
import datetime
from decimal import Decimal

from django.core.management.base import BaseCommand
from content.models import ExamCategory, JobPosting, Organization, QualificationLevel, State
from content.search_ping import notify_jobs


ORGANIZATIONS = [
    {'name': 'NLC India Limited', 'slug': 'nlc-india', 'website': 'https://www.nlcindia.in'},
    {'name': 'SIDBI', 'slug': 'sidbi', 'website': 'https://www.sidbi.in'},
    {'name': 'ASRB (ICAR)', 'slug': 'asrb', 'website': 'https://www.asrb.gov.in'},
    {'name': 'DSSSB', 'slug': 'dsssb', 'website': 'https://dsssb.delhi.gov.in'},
    {'name': 'RRC Central Railway', 'slug': 'rrc-central-railway', 'website': 'https://www.rrccr.com'},
    {'name': 'RRC Northern Railway', 'slug': 'rrc-northern-railway', 'website': 'https://www.rrcnr.org'},
    {'name': 'UKSSSC', 'slug': 'uksssc', 'website': 'https://sssc.uk.gov.in'},
    {'name': 'Exim Bank', 'slug': 'exim-bank', 'website': 'https://www.eximbankindia.in'},
]


VERIFIED_JOBS = [
    {
        # Source: NLCIL Advt. No. 10/2026 (official PDF on nlcindia.in)
        'slug': 'nlc-graduate-executive-trainee-gate-2025',
        'qualification': 'graduate',
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
        'qualification': 'graduate',
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
        'qualification': 'graduate',
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
        'qualification': '10th',
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
        'qualification': '10th',
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
    {
        # Source: RRC Northern Railway Notification No. RRC/NR/03/2026/Act Apprentice dated 06 Nov 2026 (official PDF on rrcnr.org)
        'slug': 'rrc-northern-railway-act-apprentice-2026',
        'qualification': '10th',
        'title': 'Northern Railway Act Apprentice Recruitment 2026 (4651 Slots, 10th + ITI, Merit Based)',
        'organization': 'rrc-northern-railway',
        'category': 'railway',
        'vacancies': 4651,
        'application_start_date': datetime.date(2026, 11, 11),
        'application_end_date': datetime.date(2026, 12, 11),
        'exam_date': None,
        'max_age': 24,
        'min_age': 15,
        'salary_min': None,
        'salary_max': None,
        'application_fee': Decimal('100'),
        'application_link': 'https://www.rrcnr.org',
        'meta_description': (
            'Northern Railway Apprentice 2026: 4651 slots in Lucknow, Delhi, Ambala, Firozpur, Moradabad and '
            'Jammu for 10th + ITI. No exam. Apply by 11 Dec 2026.'
        ),
        'eligibility': (
            'Class 10 (or equivalent) passed with at least 50% aggregate marks, and an ITI pass in the relevant '
            'trade (NCVT or SCVT). Both results must already be out on 6 November 2026, the date of the '
            'notification; candidates whose Class 10 or ITI result was still awaited then cannot apply.\n\n'
            'Age on 11 December 2026: at least 15 and below 24. Upper age relaxation: 5 years for SC/ST, '
            '3 years for OBC, 10 years for PwBD, and up to 10 more years for ex-servicemen depending on their '
            'service.'
        ),
        'description': (
            'Railway Recruitment Cell, Northern Railway (New Delhi) has notified 4651 Act Apprentice training '
            'slots under the Apprentices Act 1961 (Notification No. RRC/NR/03/2026/Act Apprentice, dated 6 '
            'November 2026). It is open to ITI holders in a wide range of trades, with slots across north India.\n\n'
            'Slots by cluster: Lucknow 1525, Delhi 1312, Ambala 979, Firozpur 740, Moradabad 63 and Jammu 32. '
            'The units include workshops and sheds such as Charbagh and Alambagh in Lucknow, Tughlakabad diesel '
            'shed and Tilak Bridge in Delhi, and the Jagadhri workshop. The trade-wise and category-wise slot '
            'tables are in Annexure A of the notification.\n\n'
            'Selection is purely on marks: there is no written test or viva. RRC averages your Class 10 '
            'percentage and your ITI percentage with equal weight and prepares a separate merit list for each '
            'cluster, trade and category. Ties go to the older candidate, and then to the one who passed Class '
            '10 earlier. The merit list is expected in February 2027.\n\n'
            'Pick the right cluster and unit. Choose only where slots are notified for your ITI trade; an '
            'application for a cluster or unit with no slots in your trade is rejected and the fee is not '
            'refunded. You cannot change anything after final submission, and if you submit more than one '
            'application, all of them are rejected.\n\n'
            'Training: the stipend and training period follow the current apprenticeship rules. Before training '
            'starts, selected candidates sign a contract of apprenticeship (a guardian signs for a minor). '
            'Completing the training does not guarantee a railway job.\n\n'
            'Fee: Rs 100, paid online only. SC, ST, PwBD and women candidates pay nothing.\n\n'
            'Important dates: apply online at rrcnr.org from 11 November to 11 December 2026 (11:59 pm). RRC '
            'advises applying well before the last day, when the site gets slow.\n\n'
            'If your Class 10 board gave grades: RRC takes the midpoint of each subject\'s grade range, treats '
            'each subject as out of 100 and averages them. Convert your CGPA or grades to marks this way before '
            'you fill in the form, and add all subjects, not just a group of them. Applying to Central Railway '
            'too? Its apprentice notice (2861 slots) closes earlier, on 2 December, at 5 pm.'
        ),
    },
    {
        # Source: UKSSSC Advt. No. 84/UKSSSC/2026 dated 17 Nov 2026 (official PDF on sssc.uk.gov.in, in Hindi)
        'slug': 'uksssc-uniformed-constable-1694-posts-2026',
        'qualification': '12th',
        'title': 'UKSSSC Uniformed Constable Recruitment 2026 (1694 Posts: Police, PAC, Fireman, Forest, Jail and More)',
        'organization': 'uksssc',
        'category': 'police',
        'state': 'Uttarakhand',
        'vacancies': 1694,
        'application_start_date': datetime.date(2026, 11, 25),
        'application_end_date': datetime.date(2026, 12, 25),
        'exam_date': datetime.date(2027, 4, 4),
        'max_age': 35,
        'min_age': 18,
        'salary_min': Decimal('21700'),
        'salary_max': Decimal('69100'),
        'application_fee': Decimal('300'),
        'application_link': 'https://sssc.uk.gov.in',
        'meta_description': (
            'UKSSSC Constable 2026: 1694 posts in Uttarakhand Police, PAC, Fire, Forest, Jail and more. 12th pass, '
            'Rs 21,700-69,100. Apply 25 Nov to 25 Dec 2026.'
        ),
        'eligibility': (
            'Education: Intermediate (Class 12) from the Uttarakhand board (Ramnagar) or an equivalent. Preference '
            'is given to candidates with at least two years in the Territorial Army or an NCC B or C certificate.\n\n'
            'Uttarakhand link: as for other Group C posts outside UKPSC, you need one of these: an Uttarakhand '
            'domicile or permanent residence certificate, registration with an employment exchange in Uttarakhand '
            'by 25 December 2026, or Class 10 and Class 12 passed from schools in Uttarakhand.\n\n'
            'Age on 1 July 2026 depends on the post: Civil Police (men and women), PAC/IRB, Fireman, Forest '
            'Constable and Special Tiger Guard 18 to 25; Jail Warder (men and women) 21 to 35; Secretariat Guard '
            'and Transport Constable 18 to 30; Excise Constable 18 to 35. Reserved categories of Uttarakhand get '
            'age relaxation as per state rules.\n\n'
            'Height (men): 165 cm for General, SC and OBC, 160 cm for hill-area candidates, 157.5 cm for ST. '
            'Height (women): 152 cm for General, SC and OBC, 147 cm for ST and hill-area candidates. Chest for '
            'men: 78.8 cm unexpanded and 83.8 cm expanded (76.5 and 81.5 for ST and hill-area candidates).'
        ),
        'description': (
            'The Uttarakhand Subordinate Service Selection Commission (UKSSSC) has advertised 1694 uniformed '
            'constable (Group C) posts in several state departments under Advertisement No. 84/UKSSSC/2026, '
            'dated 17 November 2026. All the posts are in pay level 3 (Rs 21,700 to 69,100).\n\n'
            'Posts: Uttarakhand Police Constable, civil police (men) 464; Constable PAC/IRB (men) 284; Police '
            'Constable (women) 238; Fireman (men and women) 201; Forest Constable 171; Jail Warder 117; Special '
            'Tiger Guards 75; Secretariat Guard 54; Excise Constable 45; Women Jail Warder 27; and Transport '
            'Constable 18.\n\n'
            'Selection has two stages. First, a physical standards test and a physical efficiency test under the '
            'Uttarakhand uniformed constable recruitment rules (2025, as amended in 2026). The efficiency test is '
            'scored, and you must reach the minimum marks in every event; for the Excise Constable post, for '
            'example, the events include a run (5 km for men, 2 km for women), long jump, cricket ball throw, '
            'chin-ups for men and a shuttle race for women. Candidates who pass then sit a 100-mark, two-hour '
            'objective written test on an OMR sheet, offline. A quarter mark is deducted for each wrong answer, '
            'and you need at least 45% (UR, EWS, OBC) or 35% (SC, ST) to qualify. The written exam is '
            'provisionally fixed for 4 April 2027.\n\n'
            'Fee: Rs 300 for Unreserved and Uttarakhand OBC candidates; Rs 150 for Uttarakhand SC, ST and EWS '
            'candidates and for disabled candidates of Uttarakhand; no fee for orphans.\n\n'
            'Important dates: apply online at sssc.uk.gov.in from 25 November to 25 December 2026. A correction '
            'window runs from 28 to 30 December 2026. Admit cards will be on the website only, not sent by post.\n\n'
            'Before you apply: upload your high school certificate and both sides of your Aadhaar card, along with '
            'any reservation and hill-area certificates you are claiming; these are compulsory. Candidates for the '
            'Civil Police, PAC/IRB and Fireman posts sign a bond to serve at least five years after training, or '
            'repay the training cost and stipend. Check the age band for the exact post you want, because it '
            'ranges from 18-25 to 21-35 across this advertisement.'
        ),
    },
    {
        # Source: Exim Bank Advt. No. HRM/MT/M/2026-27/05 and addendum dated 20 Nov 2026 (official PDFs on eximbankindia.in/careers)
        'slug': 'exim-bank-management-trainee-manager-2026',
        'qualification': 'pg',
        'title': 'Exim Bank Management Trainee and Manager Recruitment 2026 (120 Posts)',
        'organization': 'exim-bank',
        'category': 'bank',
        'vacancies': 120,
        'application_start_date': datetime.date(2026, 11, 27),
        'application_end_date': datetime.date(2026, 12, 11),
        'exam_date': None,
        'max_age': 30,
        'min_age': 21,
        'salary_min': Decimal('48480'),
        'salary_max': Decimal('93960'),
        'application_fee': Decimal('600'),
        'application_link': 'https://www.eximbankindia.in/careers',
        'meta_description': (
            'Exim Bank 2026: 90 Management Trainee and 30 Manager posts. Rs 65,000 stipend, about Rs 25 lakh CTC '
            'after training. Apply 27 Nov to 11 Dec 2026.'
        ),
        'eligibility': (
            'Management Trainee: generally at least 60% in a three-year full-time graduation, plus a two-year '
            'full-time MBA/PGDBA/PGDBM/MMS (60%) in the specialisation the stream asks for, or CA (ICAI '
            'membership needed) or CMA for the banking operations streams. Some streams have their own rules: '
            'Legal needs an LLB with 60%; Digital Technology and Cyber Security need a B.E./B.Tech (or MCA) in '
            'CS, IT or ECE with 60%; Compliance needs ACS. Degrees through distance, part-time or online '
            'learning are not accepted. Final-year students can apply if they will finish by May 2027 and can '
            'show the qualification before joining (by 30 June 2027 at the latest).\n\n'
            'Manager (MM-II): the same kind of degree plus at least four years of relevant post-qualification '
            'experience in a bank, financial institution or a reputed organisation.\n\n'
            'Age on 1 November 2026: Management Trainee 21 to 28; Manager 24 to 30. Upper age limit goes up by '
            '5 years for SC/ST, 3 years for OBC (Non-Creamy Layer) and 10 years for PwBD (more for PwBD in '
            'reserved categories).'
        ),
        'description': (
            'Export-Import Bank of India (Exim Bank), the government-owned bank that finances India\'s '
            'international trade, is recruiting 120 officers under Advertisement No. HRM/MT/M/2026-27/05: '
            '90 Management Trainees and 30 Managers in Grade MM-II. By category, the trainee posts are UR 40, '
            'OBC 25, ST 9, EWS 9 and SC 7; the manager posts are UR 15, OBC 7, SC 3, EWS 3 and ST 2.\n\n'
            'Management Trainee streams: after an addendum on 20 November, there is now one combined stream of '
            '60 posts for Banking Operations (credit and loans, treasury and accounts, internal audit and risk '
            'management), which also accepts CMA. The other trainee streams are Legal 10, Digital Technology 9, '
            'Cyber Security 2, Compliance 2, Human Resources 2, Administration 2, International Relations 1, ESG '
            '1 and Corporate Communications 1. Manager posts cover areas such as credit appraisal, loan '
            'operations and documentary credit, internal audit, MSME lending and corporate communications or '
            'CSR, each needing four years of experience. You can apply for only one post; if you submit more, '
            'only your latest complete application is kept and the other fees are lost.\n\n'
            'Selection: a written test and then a personal interview. The written test is unusual for a bank '
            'exam: it is fully subjective, two and a half hours long and worth 100 marks. Part I (40 marks) is a '
            'compulsory question or case study on your chosen specialisation, and Part II (60 marks) asks you to '
            'answer 6 of 8 questions on the same specialisation. The exam is expected in December 2026 at '
            'Chennai, Guwahati, Kolkata, Mumbai or New Delhi, with interviews in Mumbai or New Delhi.\n\n'
            'Pay: trainees get a stipend of Rs 65,000 a month for one year and then become Deputy Managers '
            '(JM-I, basic pay Rs 48,480 to 85,920), which the bank puts at about Rs 25 lakh a year in CTC. '
            'Managers (MM-II, Rs 64,820 to 93,960) start at about Rs 30 lakh a year. Officers can be posted '
            'anywhere in India, and abroad with their consent.\n\n'
            'Service bond: trainees sign a Rs 3 lakh bond to serve one year as a trainee and at least five years '
            'as a Deputy Manager; managers sign a Rs 3 lakh bond for at least three years.\n\n'
            'Fee: Rs 600 for General and OBC candidates. SC, ST, PwBD, EWS and women candidates pay only Rs 100 '
            'as intimation charges.\n\n'
            'Important dates: the online application link opens on 27 November 2026 and closes on 11 December '
            '2026, which is also the last day to pay the fee. Registration counts only once the fee is paid.\n\n'
            'Preparing: with the exam likely within weeks of the last date, practise writing structured answers '
            'and short case analyses in your specialisation under time pressure; there is no objective section '
            'to make up marks. OBC candidates need a Non-Creamy Layer certificate issued within one year before '
            'the last date, with the caste name matching the central list exactly.'
        ),
    },
    {
        # Source: NLCIL Advt. No. 11/2026 (official PDF on web.nlcindia.in/rec112026)
        'slug': 'nlc-india-executive-recruitment-advt-11-2026',
        'qualification': 'graduate',
        'title': 'NLC India Executive Recruitment 2026 (145 Experienced Posts, E1 to E7 Grades, Advt. 11/2026)',
        'organization': 'nlc-india',
        'category': 'engineering',
        'vacancies': 145,
        'application_start_date': datetime.date(2026, 11, 20),
        'application_end_date': datetime.date(2026, 12, 19),
        'exam_date': None,
        'max_age': 36,
        'min_age': None,
        'salary_min': Decimal('50000'),
        'salary_max': Decimal('260000'),
        'application_fee': Decimal('854'),
        'application_link': 'https://www.nlcindia.in',
        'meta_description': (
            'NLC India Advt 11/2026: 145 executive posts for experienced engineers, HR, legal and security '
            'professionals. CTC up to Rs 29 lakh. Apply by 19 Dec 2026.'
        ),
        'eligibility': (
            'These are posts for experienced professionals, not freshers. Most are Executive Engineer (E-4) posts '
            'that need a full-time or part-time bachelor\'s degree in the relevant engineering branch and at least '
            'five years of post-qualification experience in the stated area (for example opencast or underground '
            'mines, heavy earth-moving machinery, or coal or lignite thermal power stations of 200 MW and above). '
            'Deputy General Manager (E-7) posts need 19 years of experience. HR, legal, security and other posts '
            'have their own qualification and experience rules in the notification.\n\n'
            'Upper age limit on 1 November 2026, including relaxation: E-7 52 (UR/EWS), 55 (OBC), 57 (SC/ST); '
            'E-6 47/50/52; E-4 36/39/41; E-3 32/35/37; E-2 and E-1 30/33/35. PwBD candidates get 10 more years '
            '(13 for OBC, 15 for SC/ST), with a ceiling of 58. Candidates from PSUs, government or public sector '
            'banks usually need at least two years in the next lower pay scale (one year for E-3 posts).'
        ),
        'description': (
            'NLC India Limited, the Navratna company behind the lignite mines and power stations at Neyveli, has '
            'advertised 145 executive posts under Advertisement No. 11/2026 for its units in Tamil Nadu, '
            'Rajasthan, Odisha and Jharkhand, its solar and wind sites, and its joint ventures at Tuticorin and '
            'Ghatampur. This is a lateral recruitment for experienced people, separate from NLC\'s Graduate '
            'Executive Trainee notice for GATE 2025 candidates.\n\n'
            'Posts range from E-1 to E-7 grade. The largest group is Executive Engineer (E-4): Mechanical (Mines) '
            'alone has 40 posts, and there are E-4 posts in mechanical thermal and projects, electrical, civil, '
            'mining (12), chemical and safety. There are also Deputy General Manager (E-7) posts in mechanical, '
            'electrical and civil, Manager (Scientific) posts at E-2, Deputy Manager posts in HR (7) and Legal '
            '(3) at E-3, and security posts at E-6 (Manager) and E-1 (Assistant Manager, for former armed forces '
            'officers).\n\n'
            'Pay and CTC (approximate, per year): E-7 Rs 1,00,000 to 2,60,000 basic (about Rs 29 lakh CTC); E-6 '
            'Rs 90,000 to 2,40,000 (about Rs 26 lakh); E-4 Rs 70,000 to 2,00,000 (about Rs 20.3 lakh); E-3 Rs '
            '60,000 to 1,80,000 (about Rs 17.4 lakh); E-2 Rs 50,000 to 1,60,000 (about Rs 14.5 lakh). Performance '
            'related pay, medical cover and township housing (subject to availability) are extra. New joiners '
            'are on probation for one year and can be posted to any NLC unit, subsidiary or joint venture.\n\n'
            'Selection: for most posts it is a personal interview only. If a post gets more than six applicants '
            'per vacancy, NLC may hold a computer-based screening test first and call candidates in a 1:6 ratio. '
            'You need at least 50% in the interview (40% for SC, ST, OBC and PwBD candidates on reserved posts). '
            'Legal posts have an 80-mark written test (50% to qualify) and a 20-mark interview.\n\n'
            'Fee: Rs 854 for UR, EWS and OBC (NCL) candidates (Rs 500 application fee plus Rs 354 processing '
            'fee). SC, ST, PwBD and ex-servicemen candidates pay only the Rs 354 processing fee.\n\n'
            'Important dates: register online from 20 November 2026 (10 am) to 19 December 2026 (5 pm). '
            'Category status, experience and age are all counted as on 1 November 2026.\n\n'
            'Before you apply: upload proof of every year of experience you claim in the exact area the post '
            'asks for, because NLC shortlists on the documents you upload. OBC (NCL) and EWS certificates must '
            'be issued on or after 1 April 2026, and if you work in a PSU or government body you will need a '
            'No Objection Certificate at the interview. Interviewed candidates get their travel fare reimbursed.'
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
            if data.get('qualification'):
                extra['qualification_level'], _ = QualificationLevel.objects.get_or_create(level=data['qualification'])
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
            if created:
                # New post: tell Google and Bing now (runs on deploy, so only
                # for posts that did not exist before)
                result = notify_jobs([obj], background=False)
                if result:
                    self.stdout.write(f'    search ping: {result}')

        # Jobs added by hand in the admin before qualification tags existed
        graduate, _ = QualificationLevel.objects.get_or_create(level='graduate')
        JobPosting.objects.filter(
            title__icontains='DVC Executive Trainee', qualification_level__isnull=True
        ).update(qualification_level=graduate)

        self.stdout.write(self.style.SUCCESS(f'\nDone. {len(VERIFIED_JOBS)} verified jobs.'))
