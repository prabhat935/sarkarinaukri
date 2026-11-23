"""
Results and admit cards written for this site from the conducting body's
official notices. Every fact was checked against the notice named in the
`source` comment; the wording is our own. Each entry has a real write-up, so
it shows in the site's lists, menu and sitemap (see content.models.substantive).
"""
import datetime

from django.core.management.base import BaseCommand

from content.models import AdmitCard, ExamCategory, ExamResult, Organization
from content.seeding import upsert
from content.search_ping import SITE_URL, notify


RESULTS = [
    {
        # Source: ibps.in > CRP PO/MTs-XVI page ("Result Status of Online Main Examination", 20 Nov 2026)
        # and Detailed Notification CRP-PO/MTs-XVI (30.06.2026), Annexure I updated 27.08.2026
        'slug': 'ibps-po-mt-xvi-mains-result-2026',
        'exam_name': 'IBPS PO/MT-XVI Mains',
        'organization': 'ibps',
        'category': 'bank',
        'exam_year': 2026,
        'result_date': datetime.date(2026, 11, 20),
        'total_posts': 7565,
        'result_pdf_link': 'https://www.ibps.in/index.php/management-trainees-xvi/',
        'meta_description': (
            'IBPS PO/MT-XVI Mains result 2026 is out (20 Nov). How to check it, what the Personality Test and '
            'interview involve, and how the 80:20 final merit works.'
        ),
        'description': (
            'IBPS published the result status of the Online Main Examination for the Common Recruitment '
            'Process for Probationary Officers / Management Trainees (CRP PO/MTs-XVI) on 20 November 2026. '
            'This recruitment fills 7,565 PO/MT posts for 2027-28 in ten public sector banks, as per the '
            'vacancy table updated on 27 August 2026: Bank of Baroda 1,900, Canara Bank 1,500, Bank of '
            'Maharashtra 1,100, Indian Bank 650, Indian Overseas Bank 550, Punjab National Bank 504, Bank of '
            'India 500, Central Bank of India 500, UCO Bank 200 and Punjab & Sind Bank 161. Union Bank of '
            'India had not reported its vacancies.\n\n'
            'How to check: open the CRP PO/MTs-XVI page on ibps.in, click "Result Status of Online Main '
            'Examination for CRP-PO/MTs-XVI", and log in with your registration number or roll number and '
            'your password or date of birth. The page tells you whether you have been shortlisted. IBPS does '
            'not share Main exam scores with shortlisted candidates until the interview process is over.\n\n'
            'What happens next: shortlisted candidates first take a Personality Test (a self-report '
            'questionnaire). It is not scored for selection, but you must take it to be allowed into the '
            'interview, and your profile is placed before the interview panel. The interview is conducted by '
            'the participating banks and coordinated by a nodal bank in each state or region; call letters '
            'are downloaded from ibps.in and the date, centre and time cannot be changed. The interview is '
            'out of 100 marks, and you need at least 40 (35 for SC, ST, OBC and PwBD candidates).\n\n'
            'Final merit: the Main exam and the interview are combined in an 80:20 ratio. Preliminary marks '
            'do not count. IBPS planned interviews for November-December 2026 and provisional allotment to '
            'banks for January 2027.\n\n'
            'Preparing for the interview: keep the originals and photocopies of your certificates ready, '
            'including an OBC Non-Creamy Layer or EWS certificate in the central government format if you '
            'claim one, as these are checked at the interview. Read up on the banks you may be allotted, '
            'basic banking terms and current financial news; our guide to the IBPS PO and SBI PO '
            'selection process covers the stages in more detail.'
        ),
    },
]


ADMIT_CARDS = [
    {
        # Source: SBI CRPD/CR/2026-27/17 advertisement and "Acquaint Yourself Booklet" for the Main
        # Examination (sbi.bank.in/webfiles/uploads/files_2627/11/SBI_Junior_Associates_Mains_IH_Eng_2026_27_17.pdf)
        'slug': 'sbi-junior-associates-clerk-mains-admit-card-2026',
        'exam_name': 'SBI Junior Associates (Clerk) Mains 2026',
        'organization': 'sbi',
        'category': 'bank',
        'exam_date': datetime.date(2026, 11, 26),
        'admit_card_date': datetime.date(2026, 11, 18),
        'download_link': 'https://sbi.bank.in/web/careers/current-openings',
        'exam_duration': '2 hours 40 minutes',
        'description': (
            'State Bank of India has made the Main Examination call letters available for the recruitment of '
            'Junior Associates (Customer Support and Sales) under advertisement CRPD/CR/2026-27/17. The online '
            'Main exam is tentatively scheduled on 26 and 27 November 2026; your call letter shows your own '
            'date, reporting time and venue. The recruitment is for 7,680 regular vacancies plus backlog '
            'vacancies, and you compete only for the state you applied for.\n\n'
            'How to download: go to the SBI careers page (Current Openings), open the Junior Associates '
            'recruitment, click "Download Mains Exam Call Letter" and log in with your registration number '
            'and password or date of birth. SBI does not send call letters by post. If you applied under the '
            'separate SC/ST/OBC Special Recruitment Drive (CRPD/CR/SPLDRIVE/2026-27/16), use that drive\'s own '
            'call letter link.\n\n'
            'Exam pattern: 190 objective questions for 200 marks in 2 hours 40 minutes, with a separate time '
            'limit for each section: General/Financial Awareness (50 questions, 50 marks, 35 minutes), '
            'General English (40 questions, 40 marks, 35 minutes), Quantitative Aptitude (50 questions, 50 '
            'marks, 45 minutes) and Reasoning Ability and Computer Aptitude (50 questions, 60 marks, 45 '
            'minutes). Every question has five options, and a quarter of the marks for a question is '
            'deducted for a wrong answer. There is no sectional cut-off; you need a minimum aggregate set by '
            'the bank.\n\n'
            'How selection works after this exam: only the Main exam marks count for the final merit list, '
            'which is drawn state-wise and category-wise. Selected candidates who did not study the state\'s '
            'local language in Class 10 or 12 must pass a local language test before joining. A wait list '
            'of up to 50% of vacancies is kept for one year. The starting basic pay is Rs 26,730, and SBI '
            'puts total starting pay at about Rs 46,000 a month in a metro such as Mumbai.'
        ),
        'instructions': (
            'Report 15 minutes before the reporting time printed on your call letter; late comers are not '
            'allowed in.\n\n'
            'Carry: the Main exam call letter with a recent passport-size photo pasted on it; your Preliminary '
            'exam call letter and the photocopy of your ID that was stamped at the Preliminary exam; an '
            'original photo ID with a photocopy; and a ball-point pen. Without these you will not be allowed '
            'to sit the exam. Sign in running hand, not capital letters.\n\n'
            'Do not carry: mobile phones, smart watches or any watch, calculators, bags, wallets, belts, caps, '
            'jewellery or food. Only a transparent water bottle is allowed.\n\n'
            'At the end of the exam you must hand in both call letters, the ID photocopy and your rough '
            'sheets. Scribe candidates must bring the online scribe declaration form and the required medical '
            'certificate. SBI does not pay travel allowance for the exam.'
        ),
    },
]


class Command(BaseCommand):
    help = 'Add results and admit cards written from official notices'

    def handle(self, *args, **options):
        new_urls = []

        for data in RESULTS:
            org = Organization.objects.filter(slug=data['organization']).first()
            if org is None:
                self.stdout.write(self.style.WARNING(f"  SKIP (no org {data['organization']}): {data['slug']}"))
                continue
            obj, created = upsert(ExamResult, 
                slug=data['slug'],
                defaults={
                    'exam_name': data['exam_name'],
                    'organization': org,
                    'exam_category': ExamCategory.objects.filter(slug=data['category']).first(),
                    'exam_year': data['exam_year'],
                    'result_date': data['result_date'],
                    'total_posts': data['total_posts'],
                    'result_pdf_link': data['result_pdf_link'],
                    'description': data['description'],
                    'meta_description': data['meta_description'],
                    'is_official': True,
                },
            )
            self.stdout.write(f"  {'Created' if created else 'Updated'} result: {obj.exam_name}")
            if created:
                new_urls.append(f'{SITE_URL}/content/result/{obj.pk}/')

        for data in ADMIT_CARDS:
            org = Organization.objects.filter(slug=data['organization']).first()
            if org is None:
                self.stdout.write(self.style.WARNING(f"  SKIP (no org {data['organization']}): {data['slug']}"))
                continue
            obj, created = upsert(AdmitCard, 
                slug=data['slug'],
                defaults={
                    'exam_name': data['exam_name'],
                    'organization': org,
                    'exam_category': ExamCategory.objects.filter(slug=data['category']).first(),
                    'exam_date': data['exam_date'],
                    'admit_card_date': data['admit_card_date'],
                    'download_link': data['download_link'],
                    'exam_duration': data['exam_duration'],
                    'description': data['description'],
                    'instructions': data['instructions'],
                },
            )
            self.stdout.write(f"  {'Created' if created else 'Updated'} admit card: {obj.exam_name}")
            if created:
                new_urls.append(f'{SITE_URL}/content/admit-card/{obj.pk}/')

        if new_urls:
            # Google's Indexing API only covers job pages, so these go to IndexNow (Bing and others)
            result = notify(new_urls + [f'{SITE_URL}/content/results/', f'{SITE_URL}/content/admit-cards/'],
                            google=False, background=False)
            if result:
                self.stdout.write(f'    search ping: {result}')

        self.stdout.write(self.style.SUCCESS('Done. Verified results and admit cards.'))
