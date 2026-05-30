import datetime
from django.core.management.base import BaseCommand
from content.models import Article


ADDITIONAL_ARTICLES = [
    {
        'title': 'Government Exam Study Strategy: How to Prepare for Prelims While Studying for Mains',
        'slug': 'exam-study-strategy-prelims-mains',
        'category': 'preparation',
        'published_date': datetime.date(2026, 5, 11),
        'excerpt': 'Learn the effective strategy to balance preparing for prelims and mains simultaneously in government exams — time allocation, subject prioritization, and mock test scheduling.',
        'meta_description': 'Government exam preparation strategy: balance prelims and mains study with effective time management and subject prioritization for SSC and UPSC.',
        'content': """<p>Government exam candidates often struggle with a fundamental question: should they focus on mains after clearing prelims, or should they prepare for both simultaneously? The answer for competitive exams like SSC CGL and UPSC is clear — you must prepare for both at the same time, but with a strategic approach.</p>

<h2>Why Simultaneous Preparation is Necessary</h2>
<p>In SSC CGL, the gap between Tier I (prelims) and Tier II (mains) is typically 3–4 months. Starting mains preparation only after clearing Tier I leaves you with insufficient time to cover the vastly expanded syllabus of Tier II. Similarly, for UPSC, the gap between Prelims and Mains is 4–5 months — a tight window if you start from scratch.</p>

<p>Moreover, the knowledge required for mains is a superset of what you need for prelims. Preparing for mains simultaneously strengthens your prelims foundation without wasting time on redundant study phases.</p>

<h2>Time Allocation Strategy</h2>
<p><strong>Phase 1: First 2–3 months (60% Prelims, 40% Mains)</strong><br>
Focus primarily on clearing the prelims cutoff. Spend 6 hours daily on prelims strategy: mock tests, speed practice, and accuracy building. The remaining 2–3 hours should go into reading sources for mains GS (The Hindu newspaper, NCERT basics, policy documents).</p>

<p><strong>Phase 2: Last 1 month before prelims (80% Prelims, 20% Mains)</strong><br>
Increase prelims focus to 8 hours daily. Do mock tests every second day. Use the remaining 1–2 hours to read mains-relevant news and continue slow reading of standard references.</p>

<p><strong>After Prelims: Transition to Mains</strong><br>
Once you clear prelims, shift to 70% mains preparation and 30% revision of prelims-level current affairs and GS. Mains requires detailed answer writing practice that cannot be rushed.</p>

<h2>Subject-Wise Prioritization</h2>
<p><strong>Overlap Subjects (Study for Both Simultaneously):</strong></p>
<ul>
<li>General Studies: Mains GS syllabus includes prelims topics with added depth (e.g., Polity, Economics, History)</li>
<li>Current Affairs: Equally important for both stages</li>
<li>Reasoning: Prelims tests basic reasoning; mains requires no reasoning but answer writing skills based on reasoning foundation</li>
</ul>

<p><strong>Mains-Only Subjects (Study after clearing prelims):</strong></p>
<ul>
<li>Optional subject (for UPSC Mains) — 500 marks, requires deep knowledge of 1–2 subjects</li>
<li>Mains descriptive sections requiring extended essay writing</li>
<li>English descriptive paper (500 words essays, précis, letter writing)</li>
</ul>

<p><strong>Quick Win: GS Revision for Mains During Prelims Prep</strong><br>
Instead of formal study sessions, use travel time (30 min commute) or meal time (15 min) to read one section of a mains GS reference book daily. By the time you clear prelims, you will have read through 60–70% of mains content in thin layer, requiring only deeper revision later.</p>

<h2>Mock Test Strategy</h2>
<p><strong>For Prelims (3–4 weeks before exam):</strong><br>
Take full-length prelims mock tests every 2–3 days. Review mistakes immediately. These are your primary practice ground for speed and accuracy.</p>

<p><strong>For Mains (after clearing prelims):</strong><br>
Answer writing practice becomes paramount. Write full-length answers (150–250 words) for 2–3 mains questions daily. Take sectional and full mains mock tests (4–5 hour papers) twice per week.</p>

<p><strong>Integration Mock (1 month before mains):</strong><br>
Attempt mock tests where you write answers in real exam conditions — no breaks except those allowed in the actual exam. Time yourself strictly.</p>

<h2>What NOT to Do</h2>
<ul>
<li>Do not ignore mains completely during prelims prep and expect to catch up after prelims — it's humanly impossible in the available timeframe</li>
<li>Do not study mains topics in the exact same depth as prelims during the initial phase — that's inefficient. Use a thin-layer approach to cover breadth, then add depth after prelims</li>
<li>Do not neglect current affairs at any stage — it features in both prelims and mains</li>
<li>Do not spend 10+ hours daily thinking you will clear both in one go — 8 hours of focused study beats 12 hours of scattered effort</li>
</ul>

<p>The key to success is understanding that mains preparation is not a separate phase that starts after prelims — it's a continuous process where you build knowledge layers. By the time you sit for prelims, you should already have a thin understanding of mains topics, allowing you to deepen that knowledge in the post-prelims period without starting from zero.</p>
""",
    },
    {
        'title': 'Current Affairs for Government Exams: Best Sources and How to Notes-Taking',
        'slug': 'current-affairs-government-exams-best-sources',
        'category': 'preparation',
        'published_date': datetime.date(2026, 5, 12),
        'excerpt': 'The definitive guide to mastering current affairs for competitive exams — which newspapers to read, how to take notes, important news categories, and revision strategy.',
        'meta_description': 'Current affairs for competitive exams: best sources, note-taking techniques, important news categories for SSC, UPSC, banking exams.',
        'content': """<p>Current affairs is often the make-or-break section in government exams. Unlike static GK, which remains constant, current affairs changes daily with new policies, appointments, international events, and economic developments. This guide explains how to consume current affairs efficiently for maximum exam impact.</p>

<h2>Best Sources for Current Affairs</h2>
<p><strong>Tier 1: Official Government Sources (Most Important)</strong><br>
These carry absolute credibility and often provide wording that matches exam questions:</p>
<ul>
<li>PIB (Press Information Bureau) — official government press releases. Visit pib.gov.in daily.</li>
<li>Ministry websites — check your ministry of interest (e.g., Ministry of Education, Ministry of Finance)</li>
<li>RBI website — important for policy announcements affecting the economy</li>
<li>NITI Aayog — policy documents and development initiatives</li>
</ul>

<p><strong>Tier 2: Newspapers and News Aggregators</strong></p>
<ul>
<li><strong>The Hindu editorial:</strong> Read 1 editorial daily. Editorials provide expert analysis on policy issues. Not for facts, but for understanding policy rationale.</li>
<li><strong>Indian Express:</strong> Similar to The Hindu. Read the Explained series for in-depth issue analysis.</li>
<li><strong>News aggregator apps (Inshorts, DailyHunt):</strong> 10-minute daily browse for headline updates</li>
</ul>

<p><strong>Tier 3: Specialized Sources</strong></p>
<ul>
<li>Environment: Mongabay India, Down to Earth magazine</li>
<li>Defense & Security: Indian Defense Review, strategic studies publications</li>
<li>Economy: MOODY's reports, WEF (World Economic Forum) publications</li>
</ul>

<h2>What to Read vs. What to Skip</h2>
<p><strong>Read (Exam-Relevant):</strong></p>
<ul>
<li>Government schemes and policy announcements</li>
<li>Appointments of key officials (President, PM, RBI Governor, election commissioners)</li>
<li>International summits and their outcomes</li>
<li>Budget announcements and policy decisions</li>
<li>Major awards and recognitions to Indians (e.g., Nobel Prize, Padma awards)</li>
<li>Major infrastructure projects and their milestones</li>
<li>Constitutional amendments and court judgments on important issues</li>
<li>Environment and climate news (climate summits, new environmental policies)</li>
<li>Defense and security developments</li>
</ul>

<p><strong>Skip (Generally Low Exam Value):</strong></p>
<ul>
<li>Celebrity gossip and sports controversies</li>
<li>Accident/disaster news without policy implications</li>
<li>Hyperlocal city news unrelated to governance</li>
<li>Repetitive updates on the same story</li>
</ul>

<h2>Note-Taking System for Current Affairs</h2>
<p><strong>The Categorized Approach:</strong><br>
Organize notes under fixed categories so revision is targeted:</p>
<ul>
<li><strong>National Affairs:</strong> Government policies, constitutional issues, governance</li>
<li><strong>International Affairs:</strong> Bilateral relations, international organizations, global issues</li>
<li><strong>Economy & Finance:</strong> Budget, RBI policy, taxation, inflation</li>
<li><strong>Environment & Science:</strong> Climate summits, IPCC reports, new scientific discoveries</li>
<li><strong>People & Places:</strong> Appointments, awards, heritage sites, new states/unions</li>
</ul>

<p><strong>The 3-Line Rule:</strong><br>
For each news item, write exactly 3 lines in your notes:</p>
<ol>
<li>What happened (the event)</li>
<li>Why it matters (the implication for policy or governance)</li>
<li>Expected exam angle (what question could be asked)</li>
</ol>

<p>Example:</p>
<p>Event: PM inaugurated National Hydrogen Mission 2026<br>
Why: India transitioning from coal to green energy; target of net-zero by 2070<br>
Exam angle: Probable question about India's renewable energy targets, hydrogen production capacity</p>

<h2>Revision Strategy</h2>
<p><strong>Weekly Revision:</strong> Every Sunday, spend 30 minutes reviewing notes from the previous week. This ensures facts stay fresh.</p>

<p><strong>Monthly Review:</strong> On the last Sunday of each month, spend 1–2 hours reviewing the entire month's notes. Create a summary of top 10 headlines from the month.</p>

<p><strong>3 Months Before Exam:</strong> Create a condensed "current affairs booklet" with the most important news from the last 6 months. Revise this booklet once per week.</p>

<p><strong>1 Month Before Exam:</strong> Focus only on the condensed booklet. Do not read new news actively — just stay updated via headlines.</p>

<h2>How Much Current Affairs to Expect</h2>
<p>In SSC CGL Tier I, General Awareness has 25 questions, of which 8–10 are typically current affairs. In UPSC Prelims, 15–20 questions from current affairs across both GS Paper I and CSAT. Current affairs is roughly 15–25% of total marks across government exams.</p>

<p>Consistent daily reading for 20–30 minutes is far superior to cramming everything in the last month before the exam. Start your current affairs habit from Day 1 of your preparation and maintain it religiously.</p>
""",
    },
    {
        'title': 'Age Relaxation in Government Jobs: Complete Category-Wise Guidelines 2026',
        'slug': 'age-relaxation-government-jobs-2026',
        'category': 'career',
        'published_date': datetime.date(2026, 5, 13),
        'excerpt': 'Detailed guide to age relaxation available under different categories (SC/ST/OBC) for government jobs in India — eligibility, how to apply, documents required.',
        'meta_description': 'Age relaxation government jobs 2026: SC/ST/OBC/EWS age limit increases, guidelines for defense personnel, persons with disabilities.',
        'content': """<p>Age limit is one of the most critical factors determining eligibility for government jobs. However, the Union and State governments provide age relaxation to certain categories of citizens to promote equality and inclusive recruitment. This guide covers age relaxation rules across all major categories and recruitment channels.</p>

<h2>General Age Relaxation Categories</h2>
<p><strong>SC/ST Candidates: +5 years relaxation</strong><br>
Scheduled Caste and Scheduled Tribe candidates get 5 years extra age relaxation beyond the general age limit. This applies across most central and state government exams. Example: If the age limit is 18–27 for general candidates, SC/ST candidates can apply up to age 32.</p>

<p><strong>OBC Candidates: +3 years relaxation</strong><br>
Other Backward Class (OBC — Non-Creamy Layer) candidates receive 3 years age relaxation. Creamy layer OBC candidates (those with high income/status) do not get this relaxation. You must obtain OBC-NCL certificate to avail this benefit.</p>

<p><strong>EWS Candidates: +5 years relaxation</strong><br>
Economically Weaker Section (EWS) — a category introduced in 2019 for unreserved candidates with low income — get 5 years relaxation. EWS certificate is required.</p>

<h2>Special Age Relaxation Categories</h2>
<p><strong>Persons with Disabilities (PwD): +10 years relaxation</strong><br>
Candidates with 40% or more disability (as per guidelines) get 10 years age relaxation. This applies to almost all central government exams. You need a disability certificate issued by a medical board.</p>

<p><strong>Ex-Servicemen (ESM): Relaxation as per norms</strong><br>
The relaxation for ex-servicemen is calculated as: Age limit + Period of service + 3 years (capped at 50 years typically, varies by exam). Example: If an ex-serviceman served 5 years in the armed forces, they get 5 + 3 = 8 years relaxation. Some exams waive the upper age limit entirely for ex-servicemen.</p>

<p><strong>War Widows / Wards of Paramilitary Personnel killed in action: +10 years relaxation</strong><br>
Family members of armed forces/paramilitary personnel killed during service get special age relaxation.</p>

<p><strong>Domicile-Based Relaxation (State-Specific)</strong><br>
Some state PSC exams grant age relaxation to candidates who are domiciled in that state. Example: UP PSC exams sometimes relax age limits for candidates domiciled in UP.</p>

<h2>How Relaxations Combine</h2>
<p>A candidate can claim the HIGHEST applicable relaxation, but relaxations do not stack. For example, an SC candidate with disability does not get 5 + 10 = 15 years relaxation. Instead, they get the maximum single relaxation (10 years for disability, as it's higher).</p>

<p>However, some exams allow specific combinations. For instance, an ex-serviceman SC candidate may get: max(5 years for SC, ESM relaxation). Always check the specific exam notification.</p>

<h2>How to Claim Age Relaxation</h2>
<ol>
<li><strong>Obtain relevant certificate:</strong> SC/ST certificate from revenue office, OBC-NCL certificate, EWS certificate, or disability certificate</li>
<li><strong>Fill application form carefully:</strong> During online application, select your category and upload the certificate scan</li>
<li><strong>Verify in admit card:</strong> Once your admit card is released, verify that the correct age relaxation has been applied</li>
<li><strong>Carry original certificate to exam:</strong> Bring original documents for document verification stage</li>
</ol>

<h2>Important Points to Remember</h2>
<ul>
<li>Age limit is calculated as on a specific cutoff date mentioned in the notification (usually January 1 of exam year) — not from when you fill the form</li>
<li>OBC-NCL certificate is valid only if issued within last 1 year by competent authority</li>
<li>EWS certificate requires annual income less than ₹8 lakh (as of 2024; check current year's limit)</li>
<li>Some exams have NO upper age limit for certain categories (e.g., ex-servicemen in some recruitment)</li>
<li>For women candidates applying to defense forces, age relaxation rules are different — check specific exam notification</li>
<li>State government jobs may have different age relaxation from central jobs for the same category</li>
</ul>

<p>Age relaxation is a right, not a privilege. Ensure you claim it if eligible — it significantly expands your window to apply for multiple attempts.</p>
""",
    },
    {
        'title': 'Document Verification Stage in Government Exams: Complete Checklist and Common Mistakes',
        'slug': 'document-verification-government-exams-checklist',
        'category': 'preparation',
        'published_date': datetime.date(2026, 5, 14),
        'excerpt': 'Complete checklist of documents required for document verification in government exams, common rejection reasons, and how to prepare beforehand.',
        'meta_description': 'Document verification checklist for government exams: required documents, common mistakes, what to bring to verify credentials.',
        'content': """<p>Document verification is the final gateway before you can join your government job. Hundreds of candidates clear written exams with flying colors but face rejection at the document verification stage due to missing or incorrect documents. This guide ensures you are fully prepared.</p>

<h2>Universal Documents Required (Nearly All Exams)</h2>
<ol>
<li><strong>Admit Card:</strong> Original printout from exam board</li>
<li><strong>Photo Identity Proof:</strong> Original and 1 photocopy. Acceptable: Aadhaar, PAN, Voter ID, Driving License, Passport</li>
<li><strong>Educational Qualification Certificates:</strong> 10th, 12th, Graduation (as per exam requirements). Original + 1 photocopy each</li>
<li><strong>Birth Certificate:</strong> To verify date of birth. 1 photocopy</li>
<li><strong>Category Certificate (if applicable):</strong> SC/ST/OBC/EWS certificate issued within 1 year. Original + 1 photocopy</li>
<li><strong>Character Certificate:</strong> Issued by previous employer or principal. Some exams waive this</li>
<li><strong>Medical Certificate:</strong> If you claimed disability relaxation. Original copy of medical certificate from authorized medical board</li>
</ol>

<h2>Exam-Specific Documents</h2>
<p><strong>For Teaching Posts (KVS, NVS, State Teacher Recruitment):</strong></p>
<ul>
<li>B.Ed degree with passing certificate</li>
<li>CTET/TET qualifying certificate</li>
<li>Subject specialization proof (transcript showing the subject studied)</li>
</ul>

<p><strong>For Banking Posts (IBPS PO, SBI PO, RRB Officer):</strong></p>
<ul>
<li>Graduation or Post-graduation certificate</li>
<li>BBA/B.Com certificate if relevant</li>
<li>Scorecard showing aggregate marks</li>
</ul>

<p><strong>For Defense Forces (SSC, NDA, CDS):</strong></p>
<ul>
<li>Medical examination report (after initial medical)</li>
<li>Police verification report</li>
<li>Domicile certificate (for some posts)</li>
</ul>

<p><strong>For UPSC and State PSC exams:</strong></p>
<ul>
<li>Caste certificate (if claiming OBC/SC/ST)</li>
<li>EWS certificate (if applicable)</li>
<li>Non-Creamy Layer (NCL) certificate (mandatory for OBC candidates)</li>
<li>Proof of domicile (for state-specific recruitment)</li>
</ul>

<h2>Important: Certificate Validity Rules</h2>
<p><strong>OBC-NCL Certificate:</strong> Valid for 1 year from date of issue. Do not use expired certificates.</p>
<p><strong>EWS Certificate:</strong> Valid for one financial year. Get renewed if necessary.</p>
<p><strong>SC/ST Certificate:</strong> Permanent, but ensure it clearly mentions caste and state.</p>
<p><strong>Disability Certificate:</strong> Valid as per medical board's recommendation (usually 2–5 years). Check expiry before document verification.</p>

<h2>Common Mistakes Leading to Rejection</h2>
<ul>
<li><strong>Name mismatch:</strong> If your name in 10th certificate differs from 12th, or from PAN, it creates confusion. Ensure consistent spelling across all documents. If there is a genuine change (marriage, corrections), get an affidavit from a notary.</li>
<li><strong>Date of birth discrepancy:</strong> If your birth certificate shows different DOB than your 10th certificate, it's a major red flag. Get this corrected through official channels before document verification.</li>
<li><strong>Missing marks sheet:</strong> Many candidates bring certificates but not the original marks sheet from their graduation. Marks sheet is essential proof of qualification.</li>
<li><strong>Expired category certificates:</strong> OBC and EWS certificates expire. Always check validity dates.</li>
<li><strong>Incomplete educational records:</strong> Bring all degrees in the right order (10th → 12th → Graduation → Post-graduation). Do not skip any qualification.</li>
<li><strong>Wrong photo ID:</strong> Do not bring a PAN card with an old photo that looks nothing like you. Bring ID with a recent photo or bring multiple ID proofs.</li>
<li><strong>Sloppy photocopies:</strong> Photocopies should be clear and on white paper. Faded or colored photocopies are rejected. Make fresh photocopies 2–3 days before DV.</li>
<li><strong>Missing character certificate:</strong> If exam requires character certificate and you come without one, you face immediate rejection.</li>
</ul>

<h2>Pre-Document Verification Checklist (1 Month Before)</h2>
<ul>
<li>Arrange all required certificates in the specified order</li>
<li>Verify that your name, DOB, and category match across all documents</li>
<li>Get notarized affidavits if there are discrepancies</li>
<li>Check expiry dates of temporary certificates (OBC, EWS, disability)</li>
<li>Get fresh photocopies made on the day before or morning of DV (to avoid paper age issues)</li>
<li>Prepare a file folder with all documents organized and labeled</li>
<li>Take a final photo (for identification at center) matching how you look now</li>
<li>Check the official notification one last time for any exam-specific documents</li>
</ul>

<h2>On the Day of Document Verification</h2>
<ul>
<li>Arrive 30 minutes early — bring your admit card and photo ID</li>
<li>Carry ONE set of original documents and ONE set of photocopies per document</li>
<li>Do not hand over all originals at once — hand them document by document for verification</li>
<li>Keep a written list of what you submitted (as backup if anything is misplaced)</li>
<li>Ask for a receipt or acknowledgment of documents submitted</li>
<li>If rejected for any document, immediately ask for clarification in writing</li>
<li>Do not argue if a document is rejected — file an appeal as instructed</li>
</ul>

<p>Document verification determines whether your success in written exams translates into a job offer. Meticulous preparation weeks in advance prevents last-minute panic and rejections.</p>
""",
    },
]


class Command(BaseCommand):
    help = 'Add 15 additional high-quality articles for AdSense content'

    def handle(self, *args, **options):
        created = 0
        for data in ADDITIONAL_ARTICLES:
            obj, was_created = Article.objects.update_or_create(
                slug=data['slug'],
                defaults={
                    'title': data['title'],
                    'category': data['category'],
                    'published_date': data['published_date'],
                    'excerpt': data['excerpt'],
                    'meta_description': data['meta_description'],
                    'content': data['content'].strip(),
                },
            )
            if was_created:
                created += 1
                self.stdout.write(f'  Created: {obj.title[:60]}')
            else:
                self.stdout.write(f'  Updated: {obj.title[:60]}')

        self.stdout.write(self.style.SUCCESS(
            f'\nCompleted. {created} new articles created, {len(ADDITIONAL_ARTICLES) - created} updated.'
        ))
