"""Populate FAQ section with common government job questions."""

from django.core.management.base import BaseCommand
from content.models import FAQ


FAQS = [
    # Eligibility
    {
        'question': 'What is the basic eligibility for government exams like SSC CGL?',
        'slug': 'ssc-cgl-basic-eligibility',
        'category': 'eligibility',
        'answer': 'For SSC CGL, you need a graduation degree from a recognized university in any subject. However, some specific posts have subject requirements. For example, Junior Statistical Officer requires Statistics as one of the subjects. The age limit is 18–27 years for most posts, with relaxation available for OBC, SC/ST, and other categories.',
        'order': 1,
    },
    {
        'question': 'Can I apply for UPSC if I have any graduation degree?',
        'slug': 'upsc-any-graduation',
        'category': 'eligibility',
        'answer': 'Yes, UPSC Civil Services accepts candidates with any bachelor\'s degree from a recognized university in any subject. There is no stream restriction (Arts, Science, Commerce, Engineering all are acceptable). However, your optional subject choice (for Mains) should ideally be something you have studied or are passionate about.',
        'order': 2,
    },
    {
        'question': 'What is the age limit for Railway Group D and RRB NTPC?',
        'slug': 'railway-age-limit',
        'category': 'eligibility',
        'answer': 'For Railway Group D, the age limit is 18–36 years. For RRB NTPC (Non-Technical Popular Categories), the age limit varies by post — typically 18–30 years for most posts, and up to 36 years for some senior posts. Age is calculated as of the date of notification release.',
        'order': 3,
    },
    {
        'question': 'Can I apply for defense exams after 12th pass?',
        'slug': 'defense-jobs-12th',
        'category': 'eligibility',
        'answer': 'Yes, you can apply for several defense jobs with 12th pass qualification. Army recruits Soldier (GD) with 45% in 12th, and Soldier Technical with PCM. NDA (National Defence Academy) is open to 12th pass candidates (16.5–19.5 years). CRPF, BSF, and other forces recruit Constable GD with 10th pass.',
        'order': 4,
    },

    # Application
    {
        'question': 'What documents do I need to apply for government exams online?',
        'slug': 'online-application-documents',
        'category': 'application',
        'answer': 'Most online government exam applications require: (1) Passport-size photograph in JPEG format (usually 50–100 KB), (2) Scanned signature, (3) Scanned left thumb impression (for some exams), (4) Category certificate if applying under reserved category. All scans must be at 200 DPI. Check the specific exam notification for exact specifications.',
        'order': 1,
    },
    {
        'question': 'Can I change my application after submitting it?',
        'slug': 'change-application-after-submit',
        'category': 'application',
        'answer': 'Most exams do not allow changes after final submission. However, some large exams like UPSC open a correction window 1–2 weeks after the application deadline where you can modify certain fields. Always check the official notification for the specific exam you\'re applying to. It\'s best to triple-check before submitting.',
        'order': 2,
    },
    {
        'question': 'What is the typical application fee for government exams?',
        'slug': 'government-exam-application-fee',
        'category': 'application',
        'answer': 'Application fees typically range from ₹100 to ₹1000 depending on the exam and post. SSC exams charge ₹100–500. UPSC charges ₹100–125 (excluding fee refunds). Railway exams charge ₹250. SC/ST candidates often get full or partial fee exemption. Women candidates also get fee waivers in some exams. Check the official notification for your specific exam.',
        'order': 3,
    },
    {
        'question': 'When should I apply — early or closer to the deadline?',
        'slug': 'when-to-apply-deadline',
        'category': 'application',
        'answer': 'Always apply 5–7 days before the deadline. Government servers often experience heavy traffic in the final days, leading to crashes and failed submissions. Applying early gives you time to resolve technical issues, retake photographs if needed, or verify details. Never wait until the last day.',
        'order': 4,
    },

    # Exams
    {
        'question': 'What is the difference between Prelims and Mains in SSC CGL?',
        'slug': 'ssc-cgl-prelims-mains',
        'category': 'exams',
        'answer': 'SSC CGL Prelims (Tier I) is a 1-hour CBT with 100 MCQs testing General Awareness, Mathematics, Reasoning, and English. Mains (Tier II) is a descriptive exam with multiple papers testing deeper knowledge — Mathematical Abilities, Reasoning, General Studies (Finance/Economics), and English Language. Prelims is qualifying; Mains determines your final rank.',
        'order': 1,
    },
    {
        'question': 'How is the final rank determined in UPSC Civil Services?',
        'slug': 'upsc-final-rank-calculation',
        'category': 'exams',
        'answer': 'Your UPSC rank is determined by combining Mains marks (1750 marks from 9 papers) and Interview marks (275 marks). Total is 2025 marks. Prelims is only a screening test and doesn\'t count toward the final rank — its only purpose is to shortlist candidates for Mains. Interview performance is crucial as 275 marks out of 2025 (13%) is substantial.',
        'order': 2,
    },
    {
        'question': 'What happens if I fail the physical efficiency test (PET) in police recruitment?',
        'slug': 'police-pet-failure',
        'category': 'exams',
        'answer': 'PET is a go/no-go gate. If you fail to meet the physical standards (1.6 km run time, long jump, high jump), you are immediately eliminated regardless of your written exam performance. There is typically no second chance within the same recruitment cycle. You can only apply in the next recruitment cycle. Start physical training 4–5 months before the exam.',
        'order': 3,
    },

    # Age & Category
    {
        'question': 'How much age relaxation do SC/ST candidates get?',
        'slug': 'sc-st-age-relaxation',
        'category': 'age',
        'answer': 'SC (Scheduled Caste) and ST (Scheduled Tribe) candidates get 5 years age relaxation across most central government exams. For example, if the age limit for general candidates is 18–27 years, SC/ST candidates can apply up to 32 years. Age is calculated as of the cutoff date mentioned in the notification.',
        'order': 1,
    },
    {
        'question': 'What is OBC-NCL and why is it important?',
        'slug': 'obc-ncl-importance',
        'category': 'age',
        'answer': 'OBC-NCL stands for Other Backward Class — Non-Creamy Layer. This is for economically backward OBC candidates whose parents\' income is below ₹8 lakh per year. Only OBC-NCL candidates get age relaxation (3 years) and reservation benefits. Creamy layer OBC candidates are treated as general candidates. Your OBC-NCL certificate must be issued within 1 year of the exam.',
        'order': 2,
    },
    {
        'question': 'Can disabled candidates apply for defense forces?',
        'slug': 'disabled-candidates-defense-forces',
        'category': 'age',
        'answer': 'Yes, candidates with 40% or more disability can apply for many government jobs and get 10 years age relaxation. However, defense forces like Army have specific disability restrictions — visual and hearing impairments may disqualify you. Always check the specific exam notification for disability criteria. You need a disability certificate from an authorized medical board.',
        'order': 3,
    },

    # Documents
    {
        'question': 'What should I do if my name differs between my 10th and 12th certificates?',
        'slug': 'name-mismatch-documents',
        'category': 'documents',
        'answer': 'Name discrepancies across documents are problematic for document verification. Before appearing for any exam, get the discrepancy corrected officially (through revenue office or school). Alternatively, get a notarized affidavit from a notary explaining the name change (e.g., due to marriage or correction) and carry it to document verification.',
        'order': 1,
    },
    {
        'question': 'Is my 10-year-old Caste Certificate valid for government exams?',
        'slug': 'caste-certificate-validity',
        'category': 'documents',
        'answer': 'SC/ST certificates are permanent and valid indefinitely. However, OBC-NCL and EWS certificates are valid for only 1 year from the date of issue. If your OBC certificate is older than 1 year, you must get a new one before applying. Check the certificate\'s issue date carefully.',
        'order': 2,
    },

    # Salary
    {
        'question': 'What is the basic salary for a Constable in central armed police forces?',
        'slug': 'constable-salary-capf',
        'category': 'salary',
        'answer': 'A Constable in CRPF, BSF, CISF, ITBP, and SSB earns ₹21,700 per month (Level 3 of the Pay Matrix) as basic pay. With dearness allowance (DA), house rent allowance (HRA), and other allowances, the total monthly in-hand salary ranges from ₹30,000 to ₹35,000. Additionally, you get free accommodation, free medical, and pension benefits.',
        'order': 1,
    },
    {
        'question': 'What is the salary of an IAS officer?',
        'slug': 'ias-officer-salary',
        'category': 'salary',
        'answer': 'An IAS officer at entry level (rank of Assistant Secretary) earns ₹56,100 per month as basic pay (Level 10). With allowances, the total monthly CTC is around ₹1,00,000. As you progress to higher positions (District Collector, Chief Secretary, Cabinet Secretary), salary increases significantly. A Cabinet Secretary can earn up to ₹2,50,000+ per month.',
        'order': 2,
    },
    {
        'question': 'Do teachers in government schools get good salary and benefits?',
        'slug': 'government-teacher-salary-benefits',
        'category': 'salary',
        'answer': 'Government teachers have stable and decent salaries. A Primary Teacher starts at ₹21,700 per month (Level 1), and a Senior Secondary Teacher starts at ₹44,900 (Level 7), depending on qualifications and state. Benefits include pension, medical insurance, housing loan at low interest, and education allowance for children. The job offers excellent work-life balance with 60+ days vacation annually.',
        'order': 3,
    },

    # Career Growth
    {
        'question': 'What is the career progression from Constable to Officer in police?',
        'slug': 'constable-to-officer-progression',
        'category': 'career',
        'answer': 'In police forces, the typical progression is: Constable → Head Constable → Assistant Sub-Inspector (ASI) → Sub-Inspector (SI) → Inspector → Deputy Superintendent of Police (DSP). Promotions up to SI are usually internal (departmental exam). For DSP and above, you typically need to clear the Staff Selection Commission (SSC) exam or compete in civil services exams.',
        'order': 1,
    },
    {
        'question': 'Can I laterally move to different departments after joining as a Bank PO?',
        'slug': 'bank-po-lateral-movement',
        'category': 'career',
        'answer': 'Yes, Bank POs have significant lateral movement opportunities. Within a bank, you can move from retail banking to corporate banking, treasury, international banking, IT department, or HR. Many banks have formal career tracks allowing specialization. After 10–15 years, senior POs transition into management roles (Manager, Senior Manager, AGM). Movement between banks is less common but possible.',
        'order': 2,
    },

    # Other
    {
        'question': 'Is there negative marking in government exams?',
        'slug': 'negative-marking-exams',
        'category': 'other',
        'answer': 'Yes, most government exams have negative marking for incorrect answers. SSC exams deduct 0.5 marks per wrong answer. Banking exams typically deduct 0.25 marks per error. UPSC Prelims deducts 1/3 of marks for each wrong answer. No marks are deducted for unanswered questions. This makes accuracy more important than speed.',
        'order': 1,
    },
    {
        'question': 'How many times can I attempt UPSC Civil Services?',
        'slug': 'upsc-attempts-limit',
        'category': 'other',
        'answer': 'General category candidates get 6 attempts or until age 32 (whichever comes first). OBC candidates get 9 attempts or until age 35. SC/ST candidates get unlimited attempts until age 37. Each attempt counts from the first Prelims exam you appear for, whether you clear it or not.',
        'order': 2,
    },
    {
        'question': 'What is the minimum qualifying score to pass in an exam?',
        'slug': 'minimum-qualifying-score',
        'category': 'other',
        'answer': 'Qualifying score depends on the exam. UPSC CSAT requires 33% (66 marks out of 200). SSC Tier I requires approximately 40–50% (varies annually). Banking exams have different cutoffs for general and reserved categories. Always check the official notification for the specific exam\'s cutoff and qualifying criteria.',
        'order': 3,
    },
]


class Command(BaseCommand):
    help = 'Populate FAQ section with common government job questions'

    def handle(self, *args, **options):
        created = 0
        for data in FAQS:
            obj, was_created = FAQ.objects.update_or_create(
                slug=data['slug'],
                defaults={
                    'question': data['question'],
                    'category': data['category'],
                    'answer': data['answer'],
                    'order': data['order'],
                },
            )
            if was_created:
                created += 1
                self.stdout.write(f'  Created: {obj.question[:50]}')
            else:
                self.stdout.write(f'  Updated: {obj.question[:50]}')

        self.stdout.write(self.style.SUCCESS(
            f'\nCompleted. {created} new FAQs created, {len(FAQS) - created} updated.'
        ))
