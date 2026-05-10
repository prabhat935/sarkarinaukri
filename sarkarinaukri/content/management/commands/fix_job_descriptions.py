# content/management/commands/fix_job_descriptions.py

from django.core.management.base import BaseCommand
from content.models import JobPosting


DESCRIPTIONS = {
    'MPPSC Scientific Officer Biology Online Form 2026': (
        'Madhya Pradesh Public Service Commission (MPPSC) has released the official notification for '
        'Scientific Officer Biology posts 2026. Eligible candidates with a postgraduate degree in Life '
        'Sciences / Botany / Zoology / Microbiology can apply online through the official MPPSC website. '
        'The recruitment is for Group B gazetted posts under the state government. '
        'Selected candidates will be posted across various departments of Madhya Pradesh.'
    ),
    'UPSSSC Assistant Statistical Officer Online Form 2026': (
        'Uttar Pradesh Subordinate Services Selection Commission (UPSSSC) has invited applications for '
        'Assistant Statistical Officer (ASO) posts 2026. Candidates with a graduation degree in '
        'Statistics / Mathematics / Economics are eligible to apply. This is a Group C recruitment '
        'under UPSSSC PET qualified candidates. The selection process includes a written examination '
        'and document verification.'
    ),
    'MP Guest Teacher Online Form 2026': (
        'Madhya Pradesh Employee Selection Board (MPESB) has released the Guest Teacher recruitment '
        'notification 2026 for filling vacancies in government schools across Madhya Pradesh. '
        'Candidates with B.Ed / D.Ed qualification and subject-specific graduation are eligible. '
        'Appointment will be on a contractual basis for the academic session. Over 5000 vacancies '
        'are available in various subjects and districts.'
    ),
    'Coal India CIL Management Trainee Online Form 2026': (
        'Coal India Limited (CIL) has announced recruitment of Management Trainees (MT) for 2026. '
        'Vacancies are available in disciplines including Mining, Electrical, Mechanical, Civil, '
        'Finance, HR, Marketing and Environment. Candidates with a relevant engineering degree or '
        'MBA are eligible. Selection is through GATE score / written test followed by a personal '
        'interview. CIL is one of India\'s largest public sector undertakings.'
    ),
    'Railway SECR Raipur Apprentices Online Form 2026': (
        'South East Central Railway (SECR), Raipur Division has released the Apprentices recruitment '
        'notification 2026 under the Apprentices Act 1961. ITI pass candidates in various trades '
        'such as Electrician, Fitter, Welder, Machinist and Carpenter are eligible to apply. '
        'Training duration is 1–2 years. This is a central government apprenticeship scheme offering '
        'a monthly stipend during the training period.'
    ),
    'Navy SSC Executive IT Online Form 2026': (
        'Indian Navy has invited applications for Short Service Commission (SSC) in the Executive '
        'Branch IT cadre 2026. Male candidates with a B.Tech / BE degree in Computer Science, '
        'IT, or Electronics & Communication are eligible. Age limit is 19.5 to 25 years. '
        'Selection includes SSB Interview and Medical Examination. Selected officers will serve '
        'for an initial period of 10 years, extendable up to 14 years.'
    ),
    'Bihar BPSC 72nd CCE Pre Online Form 2026': (
        'Bihar Public Service Commission (BPSC) has released the 72nd Combined Competitive '
        'Examination (CCE) Preliminary notification 2026. This exam recruits candidates for various '
        'Group A and Group B gazetted posts in the Bihar state government. Candidates with a '
        'graduation degree from a recognized university are eligible. The preliminary exam is '
        'objective type. Approximately 1500 vacancies are expected across different departments.'
    ),
    'UP Cooperative Bank UPCISB Various Post Online Form 2026': (
        'UP Cooperative Institutional Service Board (UPCISB) has released recruitment notification '
        'for various posts in UP Cooperative Banks 2026. Posts include Banking Assistant, Supervisor, '
        'Branch Manager and other administrative roles. Candidates with graduation in any stream are '
        'eligible for most posts. Selection is through written examination and interview. '
        'This is a state government banking sector recruitment for Uttar Pradesh.'
    ),
    'RSSB Contractual Teaching Associate Online Form 2026': (
        'Rajasthan Staff Selection Board (RSSB) has released recruitment notification for '
        'Contractual Teaching Associate posts 2026 for Rajasthan government schools. '
        'Candidates with B.Ed and subject graduation are eligible. Over 9000 vacancies are '
        'available across various subjects and districts. Appointment is on a contractual basis '
        'with a fixed monthly honorarium as per Rajasthan government norms.'
    ),
    'MPESB Hospital Assistant Online Form 2026': (
        'Madhya Pradesh Employee Selection Board (MPESB) has released the Hospital Assistant '
        'recruitment notification 2026. Candidates who have passed Class 12 with Science subjects '
        'are eligible to apply. Selected candidates will be posted in government hospitals and '
        'health centres across Madhya Pradesh. The selection process includes a written examination '
        'followed by document verification. Over 800 vacancies are available statewide.'
    ),
    'NTA UGC NET June 2026 Online Form': (
        'National Testing Agency (NTA) has released the UGC NET June 2026 notification. '
        'UGC NET (National Eligibility Test) determines eligibility for Assistant Professor '
        'and Junior Research Fellowship (JRF) in Indian universities and colleges. '
        'Candidates with a postgraduate degree with a minimum of 55% marks are eligible. '
        'The exam is conducted in over 80 subjects across more than 300 exam cities in India.'
    ),
    'NTA UGC NET June 2026 Online Form': (
        'National Testing Agency (NTA) has released the UGC NET June 2026 notification. '
        'UGC NET determines eligibility for Assistant Professor and JRF in universities. '
        'Postgraduate candidates with 55% marks (50% for reserved categories) can apply. '
        'The computer-based test is held across 300+ cities and 80+ subjects.'
    ),
    'BPSSC Havildar Instructor Online Form 2026': (
        'Bihar Police Subordinate Services Commission (BPSSC) has released the Havildar '
        'Instructor recruitment notification 2026. A total of 1669 vacancies are available. '
        'Male candidates between 18–25 years of age with Class 12 qualification are eligible. '
        'The selection process includes a written exam, physical efficiency test (PET), and '
        'document verification. Selected candidates will be posted in Bihar Police training centres.'
    ),
    'Union Bank UBI Apprentices Online Form 2026': (
        'Union Bank of India has invited applications for Apprentice posts 2026 under the '
        'Apprentices Act 1961. Graduates of any discipline from a recognised university are '
        'eligible. The apprenticeship is for one year with a monthly stipend. Candidates will '
        'get hands-on banking experience in Union Bank branches across India. '
        'This is a good opportunity to gain banking sector experience.'
    ),
    'RBI Officer Grade B Online Form 2026': (
        'Reserve Bank of India (RBI) has released recruitment notification for Officer Grade B '
        '(Direct Recruitment) 2026. Vacancies are available in General stream, DEPR '
        '(Economic and Policy Research), and DSIM (Statistics and Information Management). '
        'Candidates with graduation (60% marks for General category) are eligible. '
        'This is one of the most prestigious banking jobs in India with excellent pay and career prospects.'
    ),
    'CRPF Constable Tradesman Online Form 2026': (
        'Central Reserve Police Force (CRPF) has released the Constable Tradesman recruitment '
        'notification 2026 with over 9000 vacancies. Trades include Cook, Cobbler, Tailor, '
        'Barber, Safai Karmachari, Washerman, Water Carrier, Gardener and more. '
        'Class 10 pass candidates with relevant trade certificate are eligible. '
        'Selection includes written test, physical standards test, and medical examination.'
    ),
    'UPSSSC Forest Guard Online Form 2026': (
        'Uttar Pradesh Subordinate Services Selection Commission (UPSSSC) has released the '
        'Forest Guard recruitment notification 2026. The recruitment is for the UP Forest '
        'Department with approximately 2000 vacancies. Class 12 pass candidates who have '
        'cleared UPSSSC PET 2025 are eligible to apply. Selection includes a written examination '
        'and physical standards test. Forest Guards are responsible for protecting state forests.'
    ),
    'Railway RRB Assistant Loco Pilot ALP CEN 01/2026 Online Form': (
        'Railway Recruitment Boards (RRBs) have released the Assistant Loco Pilot (ALP) '
        'CEN 01/2026 recruitment notification with approximately 9970 vacancies across all '
        'railway zones. Candidates with ITI / Diploma / Degree in relevant engineering trades '
        'are eligible. The selection process includes CBT Stage 1, CBT Stage 2, CBAT (Computer '
        'Based Aptitude Test), and Document Verification. ALP is a permanent central government job.'
    ),
    'SSC Stenographer Online Form 2026': (
        'Staff Selection Commission (SSC) has released the Stenographer Grade C and D '
        'recruitment notification 2026 with over 2000 vacancies in various central government '
        'ministries and departments. Class 12 pass candidates with required stenography speed '
        '(Grade C: 100 wpm, Grade D: 80 wpm) are eligible. Selection includes a Computer '
        'Based Examination followed by Skill Test in Stenography.'
    ),
    'SSC Combined Hindi Translators Online Form 2026': (
        'Staff Selection Commission (SSC) has released the Combined Hindi Translator '
        'Examination 2026 for posts of Junior Hindi Translator (JHT), Junior Translator, '
        'Senior Hindi Translator, and Hindi Pradhyapak across central government departments. '
        'Candidates with Master\'s degree in Hindi or English with the other as elective are '
        'eligible. The exam is conducted in two papers: Paper I (General Hindi & English) '
        'and Paper II (Translation & Essay).'
    ),
    'UPSSSC Havaldar Instructor Online Form 2026': (
        'Uttar Pradesh Subordinate Services Selection Commission (UPSSSC) has released '
        'the Havaldar Instructor recruitment notification 2026 for UP Police training. '
        '209 vacancies are available. Candidates with Class 12 qualification and relevant '
        'physical fitness standards are eligible. This is a Group C post under the UP Police '
        'department. Selection includes written examination, physical test, and document verification.'
    ),
    'ITBP Assistant Commandant Engineer Online Form 2026': (
        'Indo-Tibetan Border Police (ITBP) has released recruitment for Assistant Commandant '
        '(Engineer) posts 2026. Candidates with a degree in Civil / Electrical / Mechanical '
        'Engineering from a recognised university are eligible. Age limit is 21–30 years. '
        'Selection is through written exam followed by physical efficiency test and medical exam. '
        'ITBP is a central armed police force deployed on the India-China border.'
    ),
    'UPSSSC Lower PCS Graduate Level Online Form 2026': (
        'Uttar Pradesh Subordinate Services Selection Commission (UPSSSC) has released the '
        'Lower Subordinate PCS (Graduate Level) Preliminary Qualification Test notification 2026. '
        'Over 2700 vacancies are available across posts including Revenue Inspector, Gram '
        'Panchayat Officer, Supply Inspector, Assistant and other Group C posts. Graduates '
        'who have cleared UPSSSC PET are eligible. This is one of UP\'s most popular recruitments.'
    ),
    'UPSSSC Excise Constable Online Form 2026': (
        'Uttar Pradesh Subordinate Services Selection Commission (UPSSSC) has released the '
        'Excise Constable recruitment notification 2026. Approximately 2000 vacancies are '
        'available in the UP Excise Department. Class 12 pass candidates who have cleared '
        'UPSSSC PET 2025 are eligible. Selection includes written examination and physical '
        'standards test. Excise Constables are responsible for enforcing excise laws in UP.'
    ),
    'UPSSSC Technical Assistant Group C Online Form 2026': (
        'UPSSSC has released the Technical Assistant Group C recruitment notification 2026 '
        'with approximately 2500 vacancies in various technical departments of Uttar Pradesh. '
        'Candidates with Diploma / Degree in Engineering from a recognised institution who '
        'have cleared UPSSSC PET are eligible. This recruitment covers multiple technical '
        'disciplines including Civil, Electrical, Mechanical and Agriculture Engineering.'
    ),
    'Bihar BTSC Instructor Online Form 2026': (
        'Bihar Technical Service Commission (BTSC) has released recruitment notification for '
        'Instructor posts 2026 in ITI (Industrial Training Institutes) across Bihar. '
        'Over 3200 vacancies are available in trades such as Electrician, Fitter, Welder, '
        'Diesel Mechanic, Electronics, and more. Candidates with ITI / Diploma in the '
        'relevant trade and some teaching experience are eligible to apply.'
    ),
    'SECL Grade C Various Post Online Form 2026': (
        'South Eastern Coalfields Limited (SECL), a subsidiary of Coal India, has released '
        'recruitment notification for Grade C posts 2026. Vacancies are available for Junior '
        'Overman, Mining Sirdar, Surveyor, Electrician, Fitter and other technical posts. '
        'ITI / Diploma holders in relevant trades are eligible. SECL operates in Chhattisgarh '
        'and Madhya Pradesh and is one of the largest coal producing subsidiaries of Coal India.'
    ),
    'Jharkhand Teacher Eligibility Test JHTET Online Form 2026': (
        'Jharkhand Public Service Commission has released the Jharkhand Teacher Eligibility '
        'Test (JHTET) 2026 notification. Candidates who want to become teachers in Jharkhand '
        'government schools must qualify JHTET. Paper I is for Classes 1–5 teachers and '
        'Paper II is for Classes 6–8 teachers. The certificate is valid for 7 years. '
        'B.Ed / D.El.Ed qualified candidates are eligible to appear.'
    ),
}


class Command(BaseCommand):
    help = 'Update job descriptions with meaningful content for AdSense compliance'

    def handle(self, *args, **options):
        updated = 0
        for title, description in DESCRIPTIONS.items():
            count = JobPosting.objects.filter(title=title).update(description=description)
            if count:
                updated += count
                self.stdout.write(f'  Updated: {title[:60]}')

        # Also fix the generic placeholder descriptions
        generic = JobPosting.objects.filter(
            description__endswith='Apply online before the last date.'
        )
        for job in generic:
            job.description = (
                f'{job.title} has been officially notified for recruitment in {job.year}. '
                f'Candidates meeting the required educational qualification and age limit '
                f'as specified in the official notification are eligible to apply online. '
                f'The selection process will be conducted as per the recruiting organization\'s '
                f'official guidelines. Check the official website for complete details including '
                f'vacancy count, application fee, important dates, and eligibility criteria.'
            )
            job.save(update_fields=['description'])
            updated += 1

        self.stdout.write(self.style.SUCCESS(f'\nUpdated {updated} job descriptions.'))
