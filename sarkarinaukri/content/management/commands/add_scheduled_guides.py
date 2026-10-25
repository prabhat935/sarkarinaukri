"""
Guides written for steady publication. Each has a future published_date and
stays hidden (Article.published) until that date arrives, so new guides appear
on the site every few days without a deploy.
"""
import datetime
from django.core.management.base import BaseCommand
from content.models import Article


SCHEDULED_GUIDES = [
    {
        'title': 'Group A, B, C and D Posts Explained: What the Classification Means for Pay, Promotion and Selection',
        'slug': 'group-a-b-c-d-posts-explained',
        'category': 'career',
        'published_date': datetime.date(2026, 10, 27),
        'excerpt': 'Every central government post is classified as Group A, B or C. Here is how the groups map to pay levels, what "gazetted" means, who recruits for each group, and why Group D no longer exists.',
        'meta_description': 'Group A, B, C and D government posts explained: pay levels, gazetted vs non-gazetted, recruiting bodies, interviews and promotion under MACP.',
        'content': """<p>Notifications describe posts as "Group B, Non-Gazetted" or "Group C, Non-Ministerial", and aspirants often treat these labels as jargon. They are not. The group decides who recruits for the post, whether there is an interview, how senior the post is, and how your career is likely to progress. This guide explains the classification used by the central government.</p>

<h2>How Posts Are Classified</h2>
<p>Since the Sixth Pay Commission, central government posts are classified by their pay. Under the 7th CPC pay matrix the mapping is:</p>
<table>
<thead><tr><th>Group</th><th>Pay levels</th><th>Typical examples</th></tr></thead>
<tbody>
<tr><td>Group A</td><td>Level 10 and above</td><td>IAS, IPS, IRS and other civil services officers; Assistant Commandant; Assistant Professor in central institutions</td></tr>
<tr><td>Group B</td><td>Levels 6 to 9</td><td>Assistant Section Officer, Inspector (Income Tax / CGST), Junior Statistical Officer, Section Officer</td></tr>
<tr><td>Group C</td><td>Levels 1 to 5</td><td>Multi-Tasking Staff, Lower and Upper Division Clerk, Tax Assistant, Postal Assistant, Auditor</td></tr>
</tbody>
</table>
<p>Departments sometimes classify an individual post differently, so the notification is always the final word. But the pay level is a reliable first guide to the group.</p>

<h2>What Happened to Group D?</h2>
<p>Group D used to cover posts such as peon, chowkidar and safaiwala. Following the Sixth Pay Commission, these posts were upgraded and merged into Group C, mostly as <strong>Multi-Tasking Staff (MTS)</strong> at Pay Level 1. No new recruitment happens to "Group D" in the central government today, although some state governments and older documents still use the term.</p>

<h2>Gazetted and Non-Gazetted</h2>
<p>A <strong>gazetted</strong> post is one whose appointments are published in the Gazette of India. All Group A posts and senior Group B posts (broadly Levels 8 and 9) are gazetted. Junior Group B posts and all Group C posts are <strong>non-gazetted</strong>.</p>
<p>In practice, gazetted officers have more administrative authority, including the power to attest documents. Note that most government applications now accept <strong>self-attested</strong> copies, so you rarely need a gazetted officer's signature for recruitment forms.</p>

<h2>Who Recruits for Each Group</h2>
<ul>
<li><strong>Group A:</strong> mostly the UPSC, through the Civil Services, Engineering Services, CAPF and other examinations, or through direct recruitment with interview.</li>
<li><strong>Group B gazetted:</strong> often the UPSC, or promotion from lower grades.</li>
<li><strong>Group B non-gazetted and Group C:</strong> mostly the Staff Selection Commission (SSC) for central ministries and departments, and the Railway Recruitment Boards for railways. Banks, PSUs and state governments run their own systems.</li>
</ul>

<h2>Is There an Interview?</h2>
<p>Since 1 January 2016, the central government has <strong>discontinued interviews</strong> for recruitment to Group C and non-gazetted Group B posts. Selection for these is based on written tests, plus skill or physical tests where the post needs them. Interviews remain for most Group A and gazetted Group B posts. If you are weak in interviews, posts like ASO, Inspector and Auditor are decided entirely on your written performance.</p>

<h2>How Careers Progress</h2>
<p>Promotion depends on vacancies in the higher grade, so it can be slow in some cadres. To protect employees from stagnation, the <strong>Modified Assured Career Progression (MACP)</strong> scheme gives a financial upgrade to the next pay level after 10, 20 and 30 years of continuous service if you have not been promoted in that time. MACP raises your pay, not your post or responsibilities.</p>
<p>Movement between groups is possible. Group C employees can reach Group B through departmental promotion or limited departmental competitive examinations, and Group B officers can be promoted into Group A in many services. Many senior officers began their careers in Group C.</p>

<h2>Which Group Should You Aim For?</h2>
<p>There is no single right answer. Group A posts offer the most responsibility and pay, but the competition is intense and preparation can take years. Group B and Group C posts through SSC exams are more achievable, offer job security from the start, and still allow progress through promotions. A common and sensible path is to secure a Group B or C post first and continue preparing for higher exams while employed. Our guide to preparing while working full-time explains how to manage that.</p>

<p><em>Classifications can differ between departments and between central and state governments. Always check the group and pay level printed in the official notification.</em></p>
""",
    },
    {
        'title': 'Negative Marking in Government Exams: When Guessing Helps and When It Hurts',
        'slug': 'negative-marking-when-to-guess',
        'category': 'preparation',
        'published_date': datetime.date(2026, 10, 30),
        'excerpt': 'A simple calculation shows when an educated guess raises your expected score in SSC, banking, railway and UPSC exams, and when it does not.',
        'meta_description': 'Negative marking explained with expected-score maths: when to guess in SSC, IBPS, RRB and UPSC exams, and how eliminating options changes the odds.',
        'content': """<p>"Should I attempt a question I am not sure about?" is one of the most common questions before an objective exam. Coaching advice ranges from "never guess" to "attempt everything". The honest answer depends on the exam's marking scheme, and you can work it out yourself with a little arithmetic.</p>

<h2>The Basic Idea: Expected Score</h2>
<p>For any guess, multiply the chance of being right by the marks you gain, and the chance of being wrong by the marks you lose. If the result is positive, guessing raises your score on average; if it is negative, it lowers it.</p>
<p><strong>Expected score = (chance right × marks for correct) − (chance wrong × marks deducted)</strong></p>

<h2>Common Marking Schemes</h2>
<p>Most objective government exams have four options and deduct either one-quarter or one-third of the marks for a wrong answer. Typical examples from recent notifications:</p>
<ul>
<li><strong>SSC exams</strong> such as CGL Tier I: 2 marks per question, 0.5 deducted for a wrong answer (one-quarter).</li>
<li><strong>Banking prelims</strong> (IBPS, SBI): one-quarter of the marks deducted.</li>
<li><strong>Railway (RRB) exams</strong> and <strong>UPSC Prelims</strong>: one-third of the marks deducted.</li>
</ul>
<p>Patterns change, so check the scheme in your own exam's notification before relying on the numbers below.</p>

<h2>Case 1: A Pure Random Guess</h2>
<p>With no idea at all, each of the four options has a 25% chance.</p>
<ul>
<li><strong>One-quarter penalty</strong> (SSC: +2 / −0.5): 0.25 × 2 − 0.75 × 0.5 = 0.5 − 0.375 = <strong>+0.125</strong> marks per question. Slightly positive.</li>
<li><strong>One-third penalty</strong> (UPSC: +2 / −0.66): 0.25 × 2 − 0.75 × 0.66 ≈ 0.5 − 0.5 = <strong>0</strong>. Pure guessing gains nothing on average.</li>
</ul>
<p>So even blind guessing is not harmful under a one-quarter penalty, and is neutral under one-third. But "on average" hides a lot of risk: on a single paper, a run of wrong guesses can cost you several marks.</p>

<h2>Case 2: You Can Eliminate One Option</h2>
<p>Now each of the remaining three options has a one-in-three chance.</p>
<ul>
<li><strong>One-quarter penalty:</strong> 0.33 × 2 − 0.67 × 0.5 ≈ 0.67 − 0.33 = <strong>+0.33</strong> per question.</li>
<li><strong>One-third penalty:</strong> 0.33 × 2 − 0.67 × 0.66 ≈ 0.67 − 0.44 = <strong>+0.22</strong> per question.</li>
</ul>

<h2>Case 3: You Can Eliminate Two Options</h2>
<p>A 50-50 guess.</p>
<ul>
<li><strong>One-quarter penalty:</strong> 0.5 × 2 − 0.5 × 0.5 = <strong>+0.75</strong> per question.</li>
<li><strong>One-third penalty:</strong> 0.5 × 2 − 0.5 × 0.66 ≈ <strong>+0.67</strong> per question.</li>
</ul>
<p>This is the key lesson: <strong>every option you can confidently rule out makes a guess much more valuable.</strong> A 50-50 guess is worth roughly a third of a correct answer.</p>

<h2>A Practical Rule</h2>
<ol>
<li><strong>Know it:</strong> answer.</li>
<li><strong>Can eliminate two options:</strong> almost always attempt.</li>
<li><strong>Can eliminate one option:</strong> usually attempt, especially in exams with a one-quarter penalty.</li>
<li><strong>No idea at all:</strong> skip in exams with a one-third penalty. In one-quarter exams it is a small positive bet, but only worth it if your score is near the cut-off and you need every mark.</li>
</ol>

<h2>The Hidden Costs of Guessing</h2>
<ul>
<li><strong>Time.</strong> Time spent agonising over a question you cannot solve is time taken from questions you can. Decide quickly, mark it, and move on.</li>
<li><strong>False confidence.</strong> The maths assumes your elimination is correct. If you "eliminate" the right answer, your odds get worse, not better. Only eliminate options you are genuinely sure are wrong.</li>
<li><strong>Sectional cut-offs.</strong> Some exams require a minimum score in each section. A few wrong guesses in a weak section can push you below that line even if your total is fine.</li>
</ul>

<h2>Use Your Mock Tests</h2>
<p>Track two numbers in every mock: how many guesses you made, and how many were right. Guessing breaks even at 20% accuracy under a one-quarter penalty and 25% under a one-third penalty; below that, your guesses are costing you marks. If your guessing accuracy is comfortably higher, say 40% or more, your elimination is working and educated guesses are worth taking. If it is close to the break-even point, improve your elimination before relying on it in the real exam.</p>
""",
    },
    {
        'title': 'EWS Certificate for Central Government Jobs: Who Qualifies, Income Rules and Common Mistakes',
        'slug': 'ews-certificate-central-government-jobs',
        'category': 'exam-guide',
        'published_date': datetime.date(2026, 11, 3),
        'excerpt': 'The EWS quota needs a certificate in the central government format, issued for the right financial year. Here is who qualifies, what counts as family income and assets, and the mistakes that lead to rejection.',
        'meta_description': 'EWS certificate for central government jobs: eligibility, ₹8 lakh income limit, property limits, family definition, issuing authority and common mistakes.',
        'content': """<p>The 10% reservation for Economically Weaker Sections (EWS) applies to central government jobs and admissions for candidates who are not covered by SC, ST or OBC reservation. Many eligible candidates either do not claim it, or claim it with a certificate that is rejected at document verification. This guide explains the central government rules.</p>

<h2>Who Can Claim EWS</h2>
<p>You may be eligible if you are <strong>not</strong> covered by the SC, ST or OBC reservation schemes and your family meets both of these conditions:</p>
<ol>
<li><strong>Income:</strong> gross annual family income is <strong>below ₹8 lakh</strong>. This includes income from <strong>all sources</strong>: salary, agriculture, business and profession. Unlike the OBC creamy layer test, salary and agricultural income are counted.</li>
<li><strong>Assets:</strong> the family does <strong>not</strong> own any of the following:
<ul>
<li>5 acres of agricultural land or more</li>
<li>A residential flat of 1,000 sq ft or more</li>
<li>A residential plot of 100 sq yards or more in a notified municipality</li>
<li>A residential plot of 200 sq yards or more outside notified municipalities</li>
</ul>
</li>
</ol>
<p>The income is assessed for the <strong>financial year before</strong> the year of application.</p>

<h2>Who Counts as "Family"</h2>
<p>For EWS purposes, family means you, your parents, your siblings below 18, your spouse and your children below 18. Property held by this family in different places is added together when applying the asset limits.</p>

<h2>Who Issues the Certificate</h2>
<p>The income and asset certificate is issued by a revenue authority, typically the Tehsildar or an officer above that rank, such as the Sub-Divisional Magistrate, Additional District Magistrate or District Magistrate. The exact authority varies by state. Many states let you apply online through their e-district or service portal.</p>

<h2>Central Format Versus State Format</h2>
<p>This is the most common mistake. The central government prescribes its own format, the <strong>Income and Asset Certificate</strong>. Some states issue EWS certificates under their own rules and formats, which are valid for state jobs but may <strong>not</strong> be accepted for central recruitment such as SSC, RRB, banking or UPSC. When applying for a central job, ask the issuing office specifically for the certificate in the central government format, and compare it with the format attached to your notification.</p>

<h2>Validity and Dates</h2>
<p>Because the income test is tied to a financial year, an EWS certificate is effectively valid for one year. Recruitment notifications usually state which financial year's certificate is required, or the date by which it must have been issued. A certificate from an earlier year, or one issued after the cut-off date, can lead to rejection even if you are genuinely eligible. If your recruitment takes longer than a year, keep your certificate renewed.</p>

<h2>What EWS Does and Does Not Give You</h2>
<ul>
<li><strong>Reserved vacancies:</strong> yes, EWS seats are shown separately in the vacancy table.</li>
<li><strong>Separate cut-off:</strong> yes, merit lists are prepared category-wise, so the EWS cut-off can differ from the general cut-off.</li>
<li><strong>Age relaxation:</strong> no. In central government recruitment, EWS candidates follow the same age limits as unreserved candidates.</li>
<li><strong>Fee exemption:</strong> generally no. Most central recruitment bodies exempt women, SC, ST, PwBD and ex-servicemen candidates, but not EWS candidates. Check the fee section of your notification.</li>
</ul>

<h2>Common Mistakes That Lead to Rejection</h2>
<ul>
<li>Submitting a state-format EWS certificate for a central job</li>
<li>Using a certificate for the wrong financial year</li>
<li>Calculating income without salary or agricultural income</li>
<li>Ignoring property owned by parents in another town or village</li>
<li>Claiming EWS in the application without having the certificate, assuming you can get it later</li>
</ul>

<h2>A Quick Checklist</h2>
<ul>
<li>Not covered by SC, ST or OBC reservation</li>
<li>Family income from all sources below ₹8 lakh for the relevant year</li>
<li>Family property within all four limits</li>
<li>Certificate in the central government format, for the year the notification requires</li>
<li>Name, father's name and address exactly matching your other documents</li>
</ul>

<p><em>Rules can be revised by government orders. Always follow the EWS clause and certificate format printed in your recruitment notification.</em></p>
""",
    },
    {
        'title': 'How to Prepare for Government Exams While Working a Full-Time Job',
        'slug': 'prepare-government-exams-while-working',
        'category': 'preparation',
        'published_date': datetime.date(2026, 11, 6),
        'excerpt': 'A realistic weekly plan for aspirants with a full-time job: how many hours actually matter, how to use weekdays versus weekends, and how to avoid burning out.',
        'meta_description': 'Preparing for SSC, banking or state exams with a full-time job: a realistic weekly study plan, time-saving habits, and how to avoid burnout.',
        'content': """<p>Many successful candidates prepared while working, whether in a private job, a contract post or a lower government position. It is harder than full-time preparation, but it has real advantages: financial security, less pressure on each attempt, and the discipline that a job builds. The key is a plan that fits around your work rather than one copied from full-time aspirants.</p>

<h2>Be Realistic About Hours</h2>
<p>Full-time aspirants often study 8 to 10 hours a day. With a job, that is impossible, and trying to match it leads to exhaustion within weeks. A sustainable target is:</p>
<ul>
<li><strong>Weekdays:</strong> 1.5 to 2 hours a day</li>
<li><strong>Weekends:</strong> 5 to 6 hours a day</li>
</ul>
<p>That adds up to roughly 18 to 22 focused hours a week. Kept up for 8 to 10 months, it is enough for exams like SSC CGL, CHSL or banking prelims for most candidates, provided the hours are focused.</p>

<h2>Use Weekdays for Short, Repeatable Work</h2>
<p>After a working day, deep learning of new topics is hard. Weekday sessions work best for tasks that need consistency more than concentration:</p>
<ul>
<li>A 30-minute sectional quiz in quantitative aptitude or reasoning</li>
<li>Vocabulary and grammar practice for English</li>
<li>Current affairs revision from short notes</li>
<li>Reviewing mistakes from your last mock test</li>
</ul>
<p>Morning sessions before work often work better than late nights. Even 45 minutes before work, when your mind is fresh, can be more productive than two tired hours at night.</p>

<h2>Use Weekends for Deep Work</h2>
<p>Save the hard tasks for weekends:</p>
<ul>
<li><strong>Saturday:</strong> learn new concepts in your weakest subject, in two blocks of about two hours with a break between them.</li>
<li><strong>Sunday:</strong> take one full-length mock test in exam conditions, then spend at least an hour analysing it. The analysis matters more than the score.</li>
</ul>

<h2>A Sample Week</h2>
<table>
<thead><tr><th>Day</th><th>Focus</th><th>Time</th></tr></thead>
<tbody>
<tr><td>Monday</td><td>Quant practice + mock mistakes</td><td>1.5 hours</td></tr>
<tr><td>Tuesday</td><td>Reasoning practice + current affairs</td><td>1.5 hours</td></tr>
<tr><td>Wednesday</td><td>English + current affairs</td><td>1.5 hours</td></tr>
<tr><td>Thursday</td><td>Quant practice</td><td>1.5 hours</td></tr>
<tr><td>Friday</td><td>Light revision or rest</td><td>0–1 hour</td></tr>
<tr><td>Saturday</td><td>New concepts in weakest subject</td><td>5 hours</td></tr>
<tr><td>Sunday</td><td>Full mock test + analysis</td><td>4–5 hours</td></tr>
</tbody>
</table>

<h2>Habits That Save Time</h2>
<ul>
<li><strong>Use your commute.</strong> Current affairs, vocabulary and static GK can be revised on a phone during travel.</li>
<li><strong>Keep one set of books per subject.</strong> With limited time, switching between many sources wastes hours. Pick one standard book and one question bank per subject and finish them.</li>
<li><strong>Make short notes as you go.</strong> You will not have time to re-read whole books before the exam. Your own one-page summaries will be your revision material.</li>
<li><strong>Plan the week on Sunday night.</strong> Deciding in advance what you will study each day removes the daily "what should I do" delay.</li>
</ul>

<h2>Protect Your Health and Your Job</h2>
<p>Sleep is not optional. Studying until 2 AM every night will hurt both your work and your exam performance. Aim for at least 6 to 7 hours of sleep. Take one evening a week completely off. Do not neglect your job: it is your safety net, and losing it adds pressure that makes preparation harder.</p>

<h2>Use Your Leave Wisely</h2>
<p>Save your annual leave for the final two to three weeks before the exam. That is when full-day revision and daily mock tests give the biggest return. A week of leave just before the exam is worth far more than the same days taken randomly earlier in the year.</p>

<h2>Stay Patient</h2>
<p>Working candidates often feel they are falling behind full-time aspirants. Comparisons are not useful. Your preparation may take one extra attempt, but you are doing it without financial stress, and many working candidates clear their exams precisely because they can afford to stay consistent over a longer period.</p>
""",
    },
    {
        'title': 'OBC Non-Creamy Layer Certificate for Central Government Jobs: Rules, Income Test and Common Mistakes',
        'slug': 'obc-non-creamy-layer-certificate-central-jobs',
        'category': 'exam-guide',
        'published_date': datetime.date(2026, 11, 10),
        'excerpt': 'OBC reservation in central jobs needs a Non-Creamy Layer certificate in the central format, and your caste must be on the central list. Here is how the creamy layer is decided and the mistakes that cost candidates their seat.',
        'meta_description': 'OBC NCL certificate for central government jobs: creamy layer rules, ₹8 lakh income test, central vs state list, certificate format and validity.',
        'content': """<p>OBC candidates in central government recruitment get 27% reservation and age relaxation, but only if they hold a valid <strong>Non-Creamy Layer (NCL)</strong> certificate in the central government format. Every year, selected candidates lose their seats at document verification because of the wrong certificate. This guide explains the rules that matter.</p>

<h2>Rule 1: Your Caste Must Be on the Central List</h2>
<p>There are two OBC lists: the state list, maintained by each state, and the <strong>Central List</strong>, maintained for central government purposes. A caste can be on a state's list but not on the Central List for that state. For central jobs such as SSC, RRB, banking and UPSC, only the Central List counts. You can check the Central List for your state on the National Commission for Backward Classes (NCBC) website.</p>

<h2>Rule 2: You Must Not Be in the Creamy Layer</h2>
<p>The creamy layer is decided by your <strong>parents'</strong> status and income, not your own. Your own income and your spouse's income are not considered. The two main tests are:</p>

<h3>The status test</h3>
<p>You fall in the creamy layer if, broadly, either parent is a directly recruited Group A officer, or both parents are directly recruited Group B officers, or a parent holds certain constitutional or senior posts. Equivalent rules apply to parents in PSUs, banks and the armed forces. If your parents are in government service, their post and its group largely decide the question.</p>

<h3>The income and wealth test</h3>
<p>For families not covered by the status test, you fall in the creamy layer if the parents' gross annual income is <strong>₹8 lakh or more for three consecutive years</strong>. Importantly, <strong>income from salary and from agricultural land is not counted</strong> in this test. Only income from other sources, such as business, profession or property, is added up.</p>
<p>This is very different from the EWS test, where income from all sources counts. Many candidates wrongly assume they are in the creamy layer because their parents' salary exceeds ₹8 lakh.</p>

<h2>Rule 3: The Certificate Must Be in the Central Format</h2>
<p>State governments issue OBC certificates in their own formats for state purposes. For central jobs, you need the certificate in the format prescribed by the central government, usually titled "Form of Certificate to be Produced by Other Backward Classes Applying for Appointment to Posts under the Government of India". Recruitment notifications usually attach this format. Show it to the issuing office when you apply.</p>

<h2>Rule 4: Check the Date Requirement</h2>
<p>Because creamy layer status can change, recruitment bodies specify when the certificate must have been issued, often relative to the closing date of applications. A certificate that is too old may not be accepted. Read the certificate clause of your notification, and if your recruitment runs over a long period, keep the certificate updated.</p>

<h2>What OBC NCL Status Gives You</h2>
<ul>
<li><strong>Reserved vacancies:</strong> OBC seats are shown separately in the vacancy table.</li>
<li><strong>Age relaxation:</strong> 3 years over the upper age limit in most central recruitment.</li>
<li><strong>Separate cut-off:</strong> merit lists are drawn up category-wise.</li>
<li><strong>Fee exemption:</strong> generally not. Most central recruitment bodies do not exempt OBC candidates from fees, unless they also fall in another exempt group such as women.</li>
</ul>

<h2>Common Mistakes</h2>
<ul>
<li>Using a state-format OBC certificate for a central job</li>
<li>Caste on the state list but not the Central List</li>
<li>Counting parents' salary or agricultural income in the ₹8 lakh test</li>
<li>A certificate issued outside the date window in the notification</li>
<li>Applying as OBC and only arranging the certificate after selection</li>
</ul>

<h2>If You Are Unsure</h2>
<p>If your family situation is unusual, for example one parent in government service and one in business, read the detailed creamy layer rules issued by the Department of Personnel and Training, or ask at the office that issues certificates. If you cannot get a valid NCL certificate in time, it is safer to apply in the unreserved category than to claim OBC status you cannot prove.</p>

<p><em>Creamy layer rules and certificate formats are set by government orders and can be revised. Always follow the clause and format in your recruitment notification.</em></p>
""",
    },
    {
        'title': 'Answer Keys Explained: How to Calculate Your Score and Challenge a Wrong Answer',
        'slug': 'answer-key-calculate-score-raise-objection',
        'category': 'exam-guide',
        'published_date': datetime.date(2026, 11, 13),
        'excerpt': 'When a provisional answer key is released, you have a few days to check your score and challenge mistakes. Here is how to calculate your marks correctly and write an objection that gets accepted.',
        'meta_description': 'How to use a government exam answer key: calculate your score with negative marking, understand normalisation, and file an objection that gets accepted.',
        'content': """<p>Most objective government exams release a <strong>provisional answer key</strong> a few weeks after the exam, along with each candidate's response sheet. This is a short window that many candidates waste. Used properly, it tells you roughly where you stand and gives you a chance to correct the commission's mistakes, which do happen.</p>

<h2>Provisional and Final Answer Keys</h2>
<ul>
<li>The <strong>provisional answer key</strong> is published first, with a window of a few days for objections.</li>
<li>Experts review the objections, and the commission then publishes the <strong>final answer key</strong>, usually with or after the result.</li>
<li>Your marks are calculated using the final key. Questions found to be wrong may be corrected, or dropped with marks given to everyone.</li>
</ul>

<h2>Step 1: Download Your Response Sheet</h2>
<p>Log in with your registration details on the official website. Your response sheet shows each question, the option you chose, and the provisional correct answer. Save a copy or print it. The link is usually only available while the objection window is open.</p>

<h2>Step 2: Calculate Your Raw Score</h2>
<p>Count your correct, wrong and unattempted questions, section by section. Then apply the marking scheme from your notification:</p>
<p><strong>Raw score = (correct × marks per question) − (wrong × marks deducted)</strong></p>
<p>Example for an exam with 2 marks per question and 0.5 deducted for each wrong answer: 70 correct, 18 wrong and 12 unattempted gives 70 × 2 − 18 × 0.5 = 140 − 9 = <strong>131</strong>.</p>
<p>Also calculate each section separately if your exam has sectional cut-offs.</p>

<h2>Step 3: Understand Normalisation</h2>
<p>When an exam is held in many shifts, the papers differ in difficulty. Commissions such as the SSC <strong>normalise</strong> scores so candidates in harder shifts are not disadvantaged. Your final normalised score can therefore be a few marks higher or lower than your raw score. Raw scores are still useful for judging where you stand, but compare them with cut-offs carefully. Previous cut-offs are usually published as normalised marks.</p>

<h2>Step 4: Check the Key for Errors</h2>
<p>Go through every question you got "wrong", and every one you were unsure about. For each, ask:</p>
<ul>
<li>Is the official answer actually correct?</li>
<li>Is more than one option correct?</li>
<li>Is the question itself wrongly framed, or missing information?</li>
<li>Is there a difference between the English and Hindi versions?</li>
</ul>

<h2>Step 5: File an Objection That Gets Accepted</h2>
<p>Objections are submitted online during the window, usually with a fee per question challenged; the SSC, for example, has charged ₹100 per question. The fee is often refunded if your challenge is accepted. To give your objection the best chance:</p>
<ul>
<li><strong>Be specific.</strong> State the question number, the official answer, and the answer you believe is correct.</li>
<li><strong>Cite an authoritative source.</strong> Standard textbooks, NCERT books, government websites and official documents carry weight. Coaching notes, YouTube videos and unsourced websites generally do not.</li>
<li><strong>Explain briefly.</strong> Two or three clear sentences are better than a long argument.</li>
<li><strong>Challenge only real errors.</strong> Objections are reviewed by subject experts. Challenging every question you got wrong wastes your money.</li>
</ul>

<h2>Step 6: Decide What to Do Next</h2>
<p>Compare your estimated score with the previous year's cut-off for your category. Remember that cut-offs change with the number of vacancies and the paper's difficulty, so treat this as a rough guide.</p>
<ul>
<li><strong>Comfortably above the previous cut-off:</strong> start preparing for the next stage immediately. Do not wait for the result.</li>
<li><strong>Close to the cut-off:</strong> prepare for the next stage anyway, while also continuing preparation for upcoming exams.</li>
<li><strong>Clearly below:</strong> analyse which sections cost you marks and use that to plan your next attempt.</li>
</ul>

<h2>Keep Your Records</h2>
<p>Save your response sheet, your score calculation and any objection receipts until the final result is declared. If there is a discrepancy later, these are your evidence.</p>
""",
    },
    {
        'title': 'Age Relaxation for Ex-Servicemen in Government Jobs: How the Calculation Works',
        'slug': 'ex-servicemen-age-relaxation-calculation',
        'category': 'exam-guide',
        'published_date': datetime.date(2026, 11, 17),
        'excerpt': 'Ex-servicemen do not simply get "3 extra years". Their military service is first deducted from their age. Here is how the calculation works for SSC-type exams, with worked examples.',
        'meta_description': 'Ex-servicemen age relaxation explained: how military service is deducted from age, worked examples for SSC exams, and conditions to check in the notification.',
        'content': """<p>Ex-servicemen (ESM) are among the most experienced candidates in civil recruitment, but the age rules that apply to them are widely misunderstood. Many retiring personnel assume they are too old to apply, when in fact the rules may allow them. This guide explains how the calculation works in central recruitment such as SSC exams.</p>

<h2>The Rule in One Line</h2>
<p>For most central Group C and non-gazetted Group B recruitment, an ex-serviceman's age is calculated by <strong>deducting the period of military service from their actual age</strong>. The resulting age may exceed the post's upper age limit by up to <strong>3 years</strong>. SSC notifications express this as relaxation of "3 years after deduction of the military service rendered from the actual age as on the closing date".</p>

<h2>Worked Examples</h2>
<p>Suppose a post has an upper age limit of 27 years for unreserved candidates. With the ESM relaxation, the effective limit after deduction is 27 + 3 = <strong>30 years</strong>.</p>

<h3>Example 1</h3>
<ul>
<li>Actual age on the relevant date: 38 years</li>
<li>Military service: 17 years</li>
<li>Age after deduction: 38 − 17 = <strong>21 years</strong></li>
<li>21 is within 30, so the candidate is <strong>eligible</strong>.</li>
</ul>

<h3>Example 2</h3>
<ul>
<li>Actual age: 42 years</li>
<li>Military service: 10 years</li>
<li>Age after deduction: 42 − 10 = <strong>32 years</strong></li>
<li>32 exceeds 30, so the candidate is <strong>not eligible</strong> for this post.</li>
</ul>

<h3>Example 3: a post with a higher age limit</h3>
<ul>
<li>Upper age limit: 32 years, so the ESM limit is 35</li>
<li>Actual age 45, military service 15 years: 45 − 15 = <strong>30 years</strong></li>
<li>30 is within 35, so <strong>eligible</strong>.</li>
</ul>
<p>Count military service in years, months and days, and use the exact "as on" date given in the notification. Rounding can make the difference at the margin.</p>

<h2>Who Counts as an Ex-Serviceman</h2>
<p>The definition is set by government rules and broadly covers personnel of the Army, Navy and Air Force who have retired or been released after earning a pension, or released on completing their specified term of engagement, or released on medical grounds or for other reasons beyond their control. Personnel who leave at their own request before completing their term, or who are dismissed, are generally not covered. If your discharge circumstances are unusual, check the precise definition in the notification.</p>

<h2>Applying Before Release</h2>
<p>Recruitment notifications commonly allow serving personnel who will complete their specified term within one year of the closing date to apply as ex-servicemen, on producing a certificate from their competent authority. Check whether your notification allows this and which certificate it requires.</p>

<h2>Using ESM Status More Than Once</h2>
<p>Under central rules, an ex-serviceman who has already joined a civil post on a regular basis after claiming ESM benefits generally cannot use ESM reservation again for another civil post. There are exceptions, for example for those who apply for a new post before joining the first one and declare this properly. If you already hold a civil job, read the notification's ESM clause carefully, and be honest in your declarations: wrong claims can lead to cancellation of selection.</p>

<h2>Combining With Other Relaxations</h2>
<p>Ex-servicemen who also belong to the SC, ST or OBC categories may be entitled to additional relaxation, and disabled ex-servicemen have separate provisions. The notification's age relaxation table lists each combination. Do not assume relaxations can simply be added together; follow the table.</p>

<h2>Documents to Keep Ready</h2>
<ul>
<li>Discharge book, release order or pension payment order (PPO) showing your dates of service</li>
<li>Undertaking or certificate from the competent authority, if applying before release</li>
<li>Category certificate in the central format, if claiming SC, ST or OBC status too</li>
<li>A declaration about any previous civil employment obtained using ESM benefits</li>
</ul>

<p><em>Age relaxation rules differ between central, state and PSU recruitment, and between posts. The ESM clause and age relaxation table in your notification are the final authority.</em></p>
""",
    },
    {
        'title': 'Typing and Skill Tests in SSC Exams: Speed Requirements and How to Prepare',
        'slug': 'ssc-typing-skill-test-preparation',
        'category': 'preparation',
        'published_date': datetime.date(2026, 11, 19),
        'excerpt': 'Several SSC posts need a typing or data entry test after the written exam. It is qualifying only, but failing it ends your selection. Here are the usual speed requirements and a 6-week practice plan.',
        'meta_description': 'SSC typing test and data entry skill test explained: speed requirements for CHSL and CGL posts, how the test works, and a 6-week practice plan.',
        'content': """<p>After clearing the written exam, many candidates for posts like Lower Division Clerk, Data Entry Operator or Tax Assistant face one more hurdle: a typing or data entry skill test. It is <strong>qualifying only</strong>, so it does not add to your marks, but if you fail it you are out, regardless of your written score. Every cycle, some high scorers lose their selection here because they started practising too late.</p>

<h2>Which Posts Need a Skill Test</h2>
<p>Requirements vary between notifications, but in recent SSC exams:</p>
<ul>
<li><strong>CHSL, Lower Division Clerk / Junior Secretariat Assistant:</strong> a typing test.</li>
<li><strong>CHSL, Data Entry Operator:</strong> a data entry skill test.</li>
<li><strong>CGL, Tax Assistant:</strong> a Data Entry Speed Test (DEST).</li>
<li><strong>CGL, Assistant Section Officer and some other posts:</strong> a Computer Proficiency Test (CPT) covering word processing, spreadsheets and presentations.</li>
</ul>
<p>Check your own notification: the posts, tests and standards are listed in the scheme of examination.</p>

<h2>Usual Speed Requirements</h2>
<table>
<thead><tr><th>Test</th><th>Typical standard in recent notifications</th></tr></thead>
<tbody>
<tr><td>Typing test (English)</td><td>35 words per minute (about 10,500 key depressions per hour)</td></tr>
<tr><td>Typing test (Hindi)</td><td>30 words per minute (about 9,000 key depressions per hour)</td></tr>
<tr><td>Data entry skill test / DEST</td><td>8,000 key depressions per hour on a computer</td></tr>
</tbody>
</table>
<p>Tests usually last 10 to 15 minutes, and you type a given passage. Accuracy matters as well as speed: errors are counted, and too many mistakes mean failure even if your speed is high. Candidates with certain disabilities may get extra time or exemption under the rules in the notification.</p>

<h2>Choosing English or Hindi</h2>
<p>You usually choose the typing test language when you apply, and you cannot change it later. Choose the one you can type faster and more accurately, not the one you think is easier. For Hindi typing, check which keyboard layouts the notification permits and practise on that layout from the start, because switching layouts later is very difficult.</p>

<h2>A 6-Week Practice Plan</h2>
<p>Start this plan as soon as your written exam is over. Do not wait for the result.</p>
<ul>
<li><strong>Weeks 1–2: correct technique.</strong> Learn touch typing with all ten fingers, using the home row. Speed will drop at first; that is normal. Practise 30 to 45 minutes a day and do not look at the keyboard.</li>
<li><strong>Weeks 3–4: build speed.</strong> Type passages similar to exam passages, from newspapers or government reports, for 45 to 60 minutes a day. Measure your speed and accuracy each session.</li>
<li><strong>Weeks 5–6: exam conditions.</strong> Do timed 10 or 15 minute tests on unfamiliar passages, exactly like the real test. Aim for a comfortable margin, about 20% above the required speed, so nerves on the day do not push you below it.</li>
</ul>

<h2>Practical Tips</h2>
<ul>
<li><strong>Practise on a standard desktop keyboard</strong>, not only a laptop. Exam centres use desktop keyboards, and the key spacing feels different.</li>
<li><strong>Accuracy first.</strong> Correcting mistakes costs time, and uncorrected ones count as errors. A steady, accurate pace beats a fast, error-filled one.</li>
<li><strong>Don't stop for one mistake.</strong> Under exam rules, it is often better to continue than to go back several words. Know how errors are counted in your test.</li>
<li><strong>Learn basic editing keys</strong> such as Shift, Backspace and the arrow keys, and avoid relying on the mouse.</li>
<li><strong>Check your posture.</strong> Sit straight with your wrists level. Discomfort slows you down over a 15-minute test.</li>
</ul>

<h2>On the Day</h2>
<p>Arrive early, check that your keyboard and chair are comfortable, and tell the invigilator immediately if any key is faulty, before the test starts. Read the instructions on screen carefully: some tests do not allow backspace, or count errors in a particular way. Stay calm, keep a steady rhythm, and remember that you only need to qualify, not to top the test.</p>
""",
    },
]


class Command(BaseCommand):
    help = 'Add scheduled guides; each appears on the site on its published_date'

    def handle(self, *args, **options):
        created = 0
        for data in SCHEDULED_GUIDES:
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
                self.stdout.write(f'  Created: {obj.title[:60]} ({obj.published_date})')
            else:
                self.stdout.write(f'  Updated: {obj.title[:60]} ({obj.published_date})')

        self.stdout.write(self.style.SUCCESS(
            f'\nCompleted. {created} new guides created, {len(SCHEDULED_GUIDES) - created} updated.'
        ))
