# content/management/commands/add_latest_jobs.py

from django.core.management.base import BaseCommand
from django.utils.text import slugify
from content.models import Organization, ExamCategory, State, JobPosting
import datetime

TODAY = datetime.date(2026, 5, 10)


def d(day, month, year=2026):
    return datetime.date(year, month, day)


def status(end_date):
    if end_date is None:
        return 'Active'
    return 'Active' if end_date >= TODAY else 'Closed'


def safe_slug(title, year):
    base = slugify(f"{title} {year}")[:48]
    if not JobPosting.objects.filter(slug=base).exists():
        return base
    for i in range(2, 200):
        candidate = slugify(title)[:44] + f'-{i}'
        if not JobPosting.objects.filter(slug=candidate).exists():
            return candidate
    return base + '-x'


class Command(BaseCommand):
    help = 'Add latest SarkariResult.com job listings with correct last dates'

    def handle(self, *args, **options):
        self.stdout.write('Adding latest jobs...')
        self._add_orgs()
        count = self._add_jobs()
        self.stdout.write(self.style.SUCCESS(f'\nDone. {count} jobs added/updated.'))

    # ------------------------------------------------------------------
    def _add_orgs(self):
        new_orgs = [
            {'name': 'SSB', 'slug': 'ssb', 'website': 'https://ssbrectt.gov.in'},
            {'name': 'ITBP', 'slug': 'itbp', 'website': 'https://itbpolice.nic.in'},
            {'name': 'LIC HFL', 'slug': 'lic-hfl', 'website': 'https://lichousing.com'},
            {'name': 'BTSC Bihar', 'slug': 'btsc-bihar', 'website': 'https://btsc.bih.nic.in'},
            {'name': 'ICSIL', 'slug': 'icsil', 'website': 'https://icsil.in'},
            {'name': 'NPCIL', 'slug': 'npcil', 'website': 'https://npcil.nic.in'},
            {'name': 'NCL', 'slug': 'ncl', 'website': 'https://nclcil.in'},
            {'name': 'Indian Bank', 'slug': 'indian-bank', 'website': 'https://www.indianbank.in'},
            {'name': 'Indian Air Force', 'slug': 'indian-airforce', 'website': 'https://indianairforce.nic.in'},
            {'name': 'SECL', 'slug': 'secl', 'website': 'https://seclrecruit.com'},
            {'name': 'RPSC', 'slug': 'rpsc', 'website': 'https://rpsc.rajasthan.gov.in'},
            {'name': 'Supreme Court of India', 'slug': 'supreme-court', 'website': 'https://main.sci.gov.in'},
            {'name': 'BSNL', 'slug': 'bsnl', 'website': 'https://www.bsnl.co.in'},
            {'name': 'PNB', 'slug': 'pnb', 'website': 'https://www.pnbindia.in'},
            {'name': 'HSSC', 'slug': 'hssc', 'website': 'https://hssc.gov.in'},
            {'name': 'Chandigarh Administration', 'slug': 'chandigarh-admin', 'website': 'https://chandigarh.gov.in'},
            {'name': 'UPSRTC', 'slug': 'upsrtc', 'website': 'https://upsrtc.com'},
            {'name': 'AIIMS', 'slug': 'aiims', 'website': 'https://aiimsexams.ac.in'},
            {'name': 'Bank of Maharashtra', 'slug': 'bank-of-maharashtra', 'website': 'https://bankofmaharashtra.in'},
            {'name': 'Exim Bank', 'slug': 'exim-bank', 'website': 'https://eximbankindia.in'},
            {'name': 'India Post', 'slug': 'india-post', 'website': 'https://indiapost.gov.in'},
            {'name': 'Allahabad High Court', 'slug': 'allahabad-high-court', 'website': 'https://allahabadhighcourt.in'},
            {'name': 'Delhi High Court', 'slug': 'delhi-high-court', 'website': 'https://delhihighcourt.nic.in'},
            {'name': 'IFFCO', 'slug': 'iffco', 'website': 'https://iffco.in'},
            {'name': 'Yantra India Ltd', 'slug': 'yantra-india', 'website': 'https://yantraindia.com'},
            {'name': 'Central Silk Board', 'slug': 'central-silk-board', 'website': 'https://silkboard.gov.in'},
            {'name': 'South Indian Bank', 'slug': 'south-indian-bank', 'website': 'https://southindianbank.com'},
            {'name': 'RRC', 'slug': 'rrc', 'website': 'https://indianrailways.gov.in'},
            {'name': 'UP Police (UPPRB)', 'slug': 'upprb', 'website': 'https://uppbpb.gov.in'},
            {'name': 'Indian Coast Guard', 'slug': 'coast-guard', 'website': 'https://joinindiancoastguard.cdac.in'},
            {'name': 'SBI', 'slug': 'sbi', 'website': 'https://www.sbi.co.in/careers', 'is_featured': True},
        ]
        for data in new_orgs:
            data.setdefault('is_featured', False)
            _, created = Organization.objects.get_or_create(
                slug=data['slug'],
                defaults=data,
            )
            if created:
                self.stdout.write(f'  + Org: {data["name"]}')

    # ------------------------------------------------------------------
    def _org(self, slug):
        return Organization.objects.filter(slug=slug).first()

    def _cat(self, slug):
        return ExamCategory.objects.filter(slug=slug).first()

    def _state(self, code):
        return State.objects.filter(code=code).first()

    # ------------------------------------------------------------------
    def _add_jobs(self):
        ssc = self._org('ssc')
        upsc = self._org('upsc')
        rrb = self._org('rrb')
        rrc = self._org('rrc')
        rbi = self._org('rbi')
        sbi = self._org('sbi')
        nta = self._org('nta')
        bpsc = self._org('bpsc')
        upsssc = self._org('upsssc')
        uppsc = self._org('uppsc')
        mppsc = self._org('mppsc')
        mpesb = self._org('mpesb')
        bpssc = self._org('bpssc')
        crpf = self._org('crpf')
        navy = self._org('indian-navy')
        army = self._org('indian-army')
        iaf = self._org('indian-airforce')
        ntpc = self._org('ntpc')
        pgcil = self._org('pgcil')
        rssb = self._org('rssb')
        ubank = self._org('union-bank')
        dsssb = self._org('dsssb')
        jpsc = self._org('jpsc')
        nabard = self._org('nabard')
        csbc = self._org('csbc-bihar')
        uphesc = self._org('uphesc')
        bssc = self._org('bssc')
        phc = self._org('patna-high-court')
        nielit = self._org('nielit')
        upcoop = self._org('up-cooperative-bank')
        upsrtc = self._org('upsrtc')
        hpsc = self._org('hpsc')
        idbi = self._org('idbi-bank')
        coal = self._org('coal-india')
        secl = self._org('secl')
        ncl = self._org('ncl')
        npcil = self._org('npcil')
        itbp = self._org('itbp')
        ssb = self._org('ssb')
        btsc = self._org('btsc-bihar')
        icsil = self._org('icsil')
        ibank = self._org('indian-bank')
        rpsc = self._org('rpsc')
        sci = self._org('supreme-court')
        bsnl = self._org('bsnl')
        pnb = self._org('pnb')
        hssc = self._org('hssc')
        chd = self._org('chandigarh-admin')
        aiims = self._org('aiims')
        bom = self._org('bank-of-maharashtra')
        eximb = self._org('exim-bank')
        ipost = self._org('india-post')
        ahc = self._org('allahabad-high-court')
        dhc = self._org('delhi-high-court')
        iffco = self._org('iffco')
        yil = self._org('yantra-india')
        csb = self._org('central-silk-board')
        sib = self._org('south-indian-bank')
        licfl = self._org('lic-hfl')
        cg = self._org('coast-guard')

        pol = self._cat('police')
        rlw = self._cat('railway')
        bnk = self._cat('bank')
        tch = self._cat('teaching')
        dfc = self._cat('defence')
        psc = self._cat('state-psc')
        eng = self._cat('engineering')
        med = self._cat('medical')
        cen = self._cat('ssc-central')

        UP = self._state('UP')
        BR = self._state('BR')
        MP = self._state('MP')
        RJ = self._state('RJ')
        HR = self._state('HR')
        DL = self._state('DL')
        JH = self._state('JH')

        jobs = [
            # ---- ACTIVE (last date >= today) ----
            ('MPPSC Scientific Officer Biology Online Form 2026', mppsc, psc, MP, 2026, 70, 'B', d(20,5), 'Active'),
            ('UPSSSC Assistant Statistical Officer Online Form 2026', upsssc, psc, UP, 2026, 400, 'C', d(15,5), 'Active'),
            ('MP Guest Teacher Online Form 2026', mpesb, tch, MP, 2026, 5000, 'C', d(11,5), 'Active'),
            ('UPPSC APO 2025 Mains Online Form', uppsc, psc, UP, 2025, 52, 'B', d(22,5), 'Active'),
            ('Coal India CIL Management Trainee Online Form 2026', coal, eng, None, 2026, 640, 'A', d(11,6), 'Active'),
            ('Railway SECR Raipur Apprentices Online Form 2026', rrb, rlw, None, 2026, 432, 'D', d(4,6), 'Active'),
            ('Navy SSC Executive IT Online Form 2026', navy, dfc, None, 2026, 50, 'A', d(1,6), 'Active'),
            ('Bihar BPSC 72nd CCE Pre Online Form 2026', bpsc, psc, BR, 2026, 1500, 'B', d(31,5), 'Active'),
            ('UP Cooperative Bank UPCISB Various Post Online Form 2026', upcoop, bnk, UP, 2026, 694, 'C', d(15,5), 'Active'),
            ('RSSB Contractual Teaching Associate Online Form 2026', rssb, tch, RJ, 2026, 9000, 'C', d(3,6), 'Active'),
            ('MPESB Hospital Assistant Online Form 2026', mpesb, med, MP, 2026, 800, 'C', d(21,5), 'Active'),
            ('NTA UGC NET June 2026 Online Form', nta, tch, None, 2026, 0, 'A', d(20,5), 'Active'),
            ('UPESSC Assistant Professor BEd Online Form 2026', uphesc, tch, UP, 2026, 2504, 'B', d(27,5), 'Active'),
            ('BPSSC Havildar Instructor Online Form 2026', bpssc, pol, BR, 2026, 1669, 'C', d(1,6), 'Active'),
            ('Union Bank UBI Apprentices Online Form 2026', ubank, bnk, None, 2026, 500, 'D', d(19,5), 'Active'),
            ('RBI Officer Grade B Online Form 2026', rbi, bnk, None, 2026, 95, 'B', d(20,5), 'Active'),
            ('UP Anganwadi Worker Online Form 2026 Updated', uppsc, psc, UP, 2026, 23753, 'D', None, 'Active'),
            ('SSC Stenographer Online Form 2026', ssc, cen, None, 2026, 2006, 'C', d(15,5), 'Active'),
            ('SSC Combined Hindi Translators Online Form 2026', ssc, cen, None, 2026, 312, 'B', d(14,5), 'Active'),
            ('UPSSSC Forest Guard Online Form 2026', upsssc, psc, UP, 2026, 2000, 'C', d(20,7), 'Active'),
            ('PGCIL Diploma Trainee Online Form 2026', pgcil, eng, None, 2026, 200, 'C', d(11,5), 'Active'),
            ('UPSSSC Havaldar Instructor Online Form 2026', upsssc, pol, UP, 2026, 209, 'C', d(9,7), 'Active'),
            ('ITBP Assistant Commandant Engineer Online Form 2026', itbp, dfc, None, 2026, 48, 'A', d(20,5), 'Active'),
            ('Patna High Court Computer Operator Cum Typist Online Form 2026', phc, psc, BR, 2026, 82, 'C', d(16,5), 'Active'),
            ('Patna High Court District Judge Online Form 2026', phc, psc, BR, 2026, 49, 'A', d(15,5), 'Active'),
            ('SECL Grade C Various Post Online Form 2026', secl, eng, None, 2026, 411, 'C', d(14,5), 'Active'),
            ('UPSSSC Platoon Commander Block Organizer Online Form 2026', upsssc, psc, UP, 2026, 513, 'C', d(6,7), 'Active'),
            ('Bihar BTSC Instructor Online Form 2026', btsc, tch, BR, 2026, 3200, 'C', d(15,5), 'Active'),
            ('UPSSSC UP Vidhan Bhawan Guard Fireman Online Form 2026', upsssc, psc, UP, 2026, 320, 'D', d(29,6), 'Active'),
            ('CRPF Constable Tradesman Online Form 2026', crpf, pol, None, 2026, 9212, 'D', d(19,5), 'Active'),
            ('UPSSSC Excise Constable Online Form 2026', upsssc, pol, UP, 2026, 2000, 'D', d(24,6), 'Active'),
            ('UPPSC LT Grade Assistant Teacher Mains Online Form 2026', uppsc, tch, UP, 2026, 2899, 'C', None, 'Active'),
            ('UPSSSC Lower PCS Graduate Level Online Form 2026', upsssc, psc, UP, 2026, 2702, 'C', d(18,6), 'Active'),
            ('Jharkhand Teacher Eligibility Test JHTET Online Form 2026', jpsc, tch, JH, 2026, 0, 'C', d(21,5), 'Active'),
            ('UPSSSC Technical Assistant Group C Online Form 2026', upsssc, eng, UP, 2026, 2500, 'C', d(11,6), 'Active'),
            ('UPSRTC Female Bus Conductor Recruitment 2026', upsrtc, psc, UP, 2026, 1500, 'D', None, 'Active'),
            ('SSB Constable HC ASI SI Online Form 2026', ssb, pol, None, 2026, 900, 'D', None, 'Active'),
            ('Army SSC RVC Veterinary Graduates Online Form 2026', army, dfc, None, 2026, 30, 'A', None, 'Active'),
            ('UPSSSC Various Post Online Form Through PET 2025', upsssc, psc, UP, 2025, 0, 'C', None, 'Active'),
            ('UPSSSC Junior Engineer JE 2024 Mains Exam Fee Payment', upsssc, eng, UP, 2024, 0, 'C', None, 'Active'),
            ('UPSSSC Gram Panchayat Adhikari VDO 2023 Online Document Upload', upsssc, psc, UP, 2023, 0, 'C', None, 'Active'),
            ('UPSRTC Bus Conductor Online Form 2026', upsrtc, psc, UP, 2026, 2000, 'D', None, 'Active'),
            ('SSC CGL 2025 Option Preferences Form 2026', ssc, cen, None, 2025, 0, 'C', None, 'Active'),
            ('RBI Assistant Correction Edit Form 2026', rbi, bnk, None, 2026, 0, 'C', None, 'Active'),
            ('BPSC School Teacher TRE 4.0 OTR Registration 2026', bpsc, tch, BR, 2026, 0, 'C', None, 'Active'),
            ('NIELIT CCC Online Form 2026', nielit, cen, None, 2026, 0, 'C', None, 'Active'),
            ('UP Police Constable Edit Correction Form 2026', upsssc, pol, UP, 2026, 0, 'C', None, 'Active'),
            ('SSC Delhi Police Constable Executive Revised Vacancy 2026', ssc, pol, DL, 2026, 0, 'D', None, 'Active'),
            ('SSC Delhi Police Constable Driver Revised Vacancy 2026', ssc, pol, DL, 2026, 0, 'D', None, 'Active'),
            ('SSC Delhi Police HC AWO TPO Revised Vacancy 2026', ssc, pol, DL, 2026, 0, 'C', None, 'Active'),
            ('SSC Delhi Police HC Ministerial Revised Vacancy 2026', ssc, pol, DL, 2026, 0, 'C', None, 'Active'),
            ('Railway RRB Assistant Loco Pilot ALP CEN 01/2026 Online Form', rrb, rlw, None, 2026, 9970, 'D', d(14,6), 'Active'),

            # ---- CLOSED (last date < today) ----
            ('SSC Stenographer 2025 Option Cum Preference Form', ssc, cen, None, 2025, 0, 'C', d(8,5), 'Closed'),
            ('MPPSC ADPO Online Form 2026', mppsc, psc, MP, 2026, 75, 'B', d(8,5), 'Closed'),
            ('UPTET 2026 Online Form', uppsc, tch, UP, 2026, 0, 'C', d(3,5), 'Closed'),
            ('RRB Ministerial Isolated Post CEN 07/2024 Update Qualification', rrb, rlw, None, 2024, 0, 'C', d(29,4), 'Closed'),
            ('NTPC Assistant Executive Operation Online Form 2026', ntpc, eng, None, 2026, 160, 'B', d(7,5), 'Closed'),
            ('UPSSSC UP Pollution Control Board Various Post Online Form 2026', upsssc, eng, UP, 2026, 150, 'C', d(29,4), 'Closed'),
            ('SSB Constable HC ASI SI Edit Online Form 2026', ssb, pol, None, 2026, 0, 'C', d(4,5), 'Closed'),
            ('LIC HFL Junior Assistant Online Form 2026', licfl, bnk, None, 2026, 180, 'D', d(30,4), 'Closed'),
            ('RBI JE Junior Engineer Online Form 2026', rbi, eng, None, 2026, 31, 'B', d(6,5), 'Closed'),
            ('UPSSSC Assistant Boring Technician Online Form 2026', upsssc, eng, UP, 2026, 585, 'C', d(5,5), 'Closed'),
            ('SSC Selection Post Phase 14 Online Form 2026', ssc, cen, None, 2026, 2000, 'C', d(4,5), 'Closed'),
            ('Chandigarh Clerk Steno Online Form 2026', chd, cen, None, 2026, 270, 'C', d(26,4), 'Closed'),
            ('SSC GD Constable 2025 Choose Exam Week Preferences', ssc, pol, None, 2025, 0, 'D', d(15,4), 'Closed'),
            ('ICSIL DEO MTS Online Form 2026', icsil, cen, DL, 2026, 200, 'D', d(13,4), 'Closed'),
            ('NPCIL Executive Trainee ET Online Form 2026', npcil, eng, None, 2026, 225, 'B', d(30,4), 'Closed'),
            ('NCL HEMM Operator Staff Nurse Overseer Civil Online Form 2026', ncl, eng, None, 2026, 300, 'C', d(1,5), 'Closed'),
            ('BTSC Laboratory Assistant Online Form 2026', btsc, med, BR, 2026, 1500, 'C', d(6,5), 'Closed'),
            ('Indian Bank Specialist Officer SO Online Form 2026', ibank, bnk, None, 2026, 417, 'B', d(28,4), 'Closed'),
            ('UPSSSC Teacher Cadre JTC Online Form 2026', upsssc, tch, UP, 2026, 7000, 'C', d(27,4), 'Closed'),
            ('SSB Head Constable Online Form 2026', ssb, pol, None, 2026, 115, 'C', d(20,4), 'Closed'),
            ('MPESB Nursing Officer Sister Tutor Online Form 2026', mpesb, med, MP, 2026, 1600, 'C', d(20,4), 'Closed'),
            ('UPSSSC Various Post Online Form 2026', upsssc, psc, UP, 2026, 0, 'C', d(22,4), 'Closed'),
            ('Patna High Court Technical Assistant Online Form 2026', phc, eng, BR, 2026, 50, 'C', d(30,4), 'Closed'),
            ('Indian Navy MR Musician 02/2026 Batch Online Form', navy, dfc, None, 2026, 20, 'D', d(26,4), 'Closed'),
            ('Indian Army Agniveer Rally Recruitment Online Form 2026', army, dfc, None, 2026, 0, 'D', d(10,4), 'Closed'),
            ('ITBP Constable Barber Washerman Online Form 2026', itbp, pol, None, 2026, 218, 'D', d(28,4), 'Closed'),
            ('MPESB MP Police Sub Inspector SI Subedar 2nd Phase Fee Payment 2026', mpesb, pol, MP, 2026, 0, 'C', d(8,4), 'Closed'),
            ('UPCISB UP Cooperative Bank Various Post Online Form 2026', upcoop, bnk, UP, 2026, 694, 'C', d(15,4), 'Closed'),
            ('BPSC 33 Civil Judge PCS J Online Form 2026', bpsc, psc, BR, 2026, 90, 'A', d(30,4), 'Closed'),
            ('UPPSC GIC Lecturer Edit Modify Form 2026', uppsc, tch, UP, 2026, 0, 'B', d(27,3), 'Closed'),
            ('Haryana HSSC Stenographer Online Form 2026', hssc, cen, HR, 2026, 384, 'C', d(19,3), 'Closed'),
            ('Haryana HSSC Constable Online Form 2026', hssc, pol, HR, 2026, 1000, 'D', d(19,3), 'Closed'),
            ('UPSSSC Technical Assistant Group C 2024 Online Document Upload', upsssc, eng, UP, 2024, 0, 'C', d(5,4), 'Closed'),
            ('Railway RRC SCR Apprentices Online Form 2026', rrc, rlw, None, 2026, 4500, 'D', d(11,4), 'Closed'),
            ('MPESB Van Rakshak Jail Prahari Online Form 2026', mpesb, pol, MP, 2026, 2000, 'D', d(30,4), 'Closed'),
            ('MPESB Group 5 Various Post Online Form 2026', mpesb, psc, MP, 2026, 1500, 'C', d(27,3), 'Closed'),
            ('Allahabad High Court Private Secretary Online Form 2026', ahc, psc, UP, 2026, 21, 'B', d(1,4), 'Closed'),
            ('RRC CR Apprentices Online Form 2026', rrc, rlw, None, 2026, 2300, 'D', d(9,4), 'Closed'),
            ('UPSC Combined Medical Services CMS Online Form 2026', upsc, med, None, 2026, 827, 'A', d(31,3), 'Closed'),
            ('Indian Navy SSR Medical Online Form 2026', navy, dfc, None, 2026, 300, 'D', d(6,4), 'Closed'),
            ('Indian Navy SSR MR INET 2026 Online Form', navy, dfc, None, 2026, 400, 'D', d(6,4), 'Closed'),
            ('UP Pollution Control Board UPPCB AEE ASO Online Form 2026', upsssc, eng, UP, 2026, 218, 'B', d(28,3), 'Closed'),
            ('BSNL Senior Executive Trainee SET Online Form 2026', bsnl, eng, None, 2026, 300, 'B', d(31,3), 'Closed'),
            ('IDBI Bank JAM Assistant Manager Online Form 2026', idbi, bnk, None, 2026, 800, 'B', d(19,3), 'Closed'),
            ('Railway RRB Group D Online Form 2026', rrb, rlw, None, 2026, 32438, 'D', d(9,3), 'Closed'),
            ('UPSC Civil Services IAS IFS Pre Edit Correction Form 2026', upsc, psc, None, 2026, 0, 'A', d(3,3), 'Closed'),
            ('UPSSSC Pharmacist Online Form 2026', upsssc, med, UP, 2026, 2800, 'C', d(29,3), 'Closed'),
            ('Jharkhand JPSC Pre Online Form 2026', jpsc, psc, JH, 2026, 342, 'B', d(9,3), 'Closed'),
            ('Delhi DSSSB Various Post Advt No 02/2026 Online Form', dsssb, cen, DL, 2026, 600, 'C', d(28,3), 'Closed'),
            ('BPSC Prosecution Officer Online Form 2026', bpsc, psc, BR, 2026, 59, 'B', d(20,3), 'Closed'),
            ('Indian Airforce Agniveervayu 01/2027 Online Form', iaf, dfc, None, 2026, 0, 'D', d(10,3), 'Closed'),
            ('UPSC Civil Services IAS IFS Pre Online Form 2026', upsc, psc, None, 2026, 1056, 'A', d(27,2), 'Closed'),
            ('CSBC Bihar Police Constable Operator Online Form 2026', csbc, pol, BR, 2026, 1669, 'D', d(31,3), 'Closed'),
            ('South Indian Bank SIB Junior Officer Online Form 2026', sib, bnk, None, 2026, 500, 'C', d(2,3), 'Closed'),
            ('UPSC CPF Assistant Commandant CAPF Online Form 2026', upsc, dfc, None, 2026, 506, 'A', d(12,3), 'Closed'),
            ('Delhi DSSSB AE JE ASO Legal Assistant Online Form 2026', dsssb, eng, DL, 2026, 1000, 'C', d(24,3), 'Closed'),
            ('RRC WR Apprentice Online Form 2026', rrc, rlw, None, 2026, 3624, 'D', d(23,3), 'Closed'),
            ('India Post GDS Correction Edit Form 2026', ipost, cen, None, 2026, 0, 'D', d(19,2), 'Closed'),
            ('HPSC PGT Computer Science Online Form 2026', hpsc, tch, HR, 2026, 200, 'B', d(9,3), 'Closed'),
            ('RBI Assistant Online Form 2026', rbi, bnk, None, 2026, 926, 'C', d(8,3), 'Closed'),
            ('BTSC Dairy Field Officer Technical Officer Online Form 2026', btsc, med, BR, 2026, 300, 'B', d(13,3), 'Closed'),
            ('Jharkhand JPSC Civil Services Pre Online Form 2026', jpsc, psc, JH, 2026, 342, 'A', d(20,2), 'Closed'),
            ('AIIMS NORCET 10th Online Form 2026', aiims, med, None, 2026, 2000, 'B', d(16,3), 'Closed'),
            ('Army NCC Special Entry 124 Course Online Form 2026', army, dfc, None, 2026, 90, 'A', d(16,3), 'Closed'),
            ('UPSC IES ISS Online Form 2026', upsc, eng, None, 2026, 48, 'A', d(3,3), 'Closed'),
            ('MPESB Primary Teacher PSTST 2025 Update Qualification', mpesb, tch, MP, 2025, 0, 'C', d(11,2), 'Closed'),
            ('Haryana HPSC HCS Online Form 2026', hpsc, psc, HR, 2026, 150, 'A', d(26,2), 'Closed'),
            ('HSSC Stenographer Online Form 2026', hssc, cen, HR, 2026, 384, 'C', d(20,2), 'Closed'),
            ('PNB Apprentices Online Form 2026', pnb, bnk, None, 2026, 2000, 'D', d(24,2), 'Closed'),
            ('RBI Non CSG Various Post Online Form 2026', rbi, bnk, None, 2026, 200, 'B', d(26,2), 'Closed'),
            ('MPPSC Pre 2026 Online Form', mppsc, psc, MP, 2026, 227, 'B', d(9,2), 'Closed'),
            ('RSSB Forester Online Form 2026', rssb, psc, RJ, 2026, 2399, 'C', d(11,2), 'Closed'),
            ('Rajasthan RSSB Women Supervisor Online Form 2026', rssb, psc, RJ, 2026, 1564, 'C', d(11,2), 'Closed'),
            ('MPESB MP Police ASI HC Computer Online Form 2026', mpesb, pol, MP, 2026, 800, 'C', d(19,2), 'Closed'),
            ('BTSC Work Inspector Mechanical Online Form 2026', btsc, eng, BR, 2026, 200, 'C', d(8,2), 'Closed'),
            ('Bihar Police BPSSC ASI Operation Online Form 2026', bpssc, pol, BR, 2026, 200, 'C', d(4,3), 'Closed'),
            ('Indian Airforce Agniveervayu Intake 01/2027 Online Form', iaf, dfc, None, 2026, 0, 'D', d(8,2), 'Closed'),
            ('Delhi High Court Junior Judicial Assistant JJA Online Form 2026', dhc, cen, DL, 2026, 39, 'C', d(23,2), 'Closed'),
            ('India Post GDS Online Form 2026', ipost, cen, None, 2026, 21413, 'D', d(14,2), 'Closed'),
            ('UP Police Constable Online Form 2026', upsssc, pol, UP, 2026, 60244, 'D', d(31,1), 'Closed'),
            ('BPSC Professor Online Form 2026', bpsc, tch, BR, 2026, 1200, 'A', d(12,3), 'Closed'),
            ('CSBC Bihar Police Constable Special Branch Online Form 2026', csbc, pol, BR, 2026, 300, 'D', d(5,3), 'Closed'),
            ('Bihar BSSC 10+2 Inter Level Online Form 2026', bssc, cen, BR, 2026, 11098, 'D', d(13,2), 'Closed'),
            ('Railway RRB Isolated Various Post Online Form 2026', rrb, rlw, None, 2026, 2506, 'C', d(29,1), 'Closed'),
            ('UPSSSC Lekhpal Correction Edit Form 2026', upsssc, psc, UP, 2026, 0, 'C', d(4,2), 'Closed'),
            ('JPSC Drug Inspector Online Form 2026', jpsc, med, JH, 2026, 29, 'B', d(18,2), 'Closed'),
            ('Bihar BPSC Auditor Online Form 2026', bpsc, psc, BR, 2026, 281, 'B', d(26,2), 'Closed'),
            ('SBI Circle Based Officer CBO Online Form 2026', sbi, bnk, None, 2026, 1000, 'B', d(18,2), 'Closed'),
            ('Indian Airforce Airmen Medical Assistant Intake 01/2027 Online Form', iaf, dfc, None, 2026, 0, 'D', d(1,2), 'Closed'),
            ('Central Silk Board CSB Scientist B Online Form 2026', csb, eng, None, 2026, 51, 'B', d(18,2), 'Closed'),
            ('Yantra India Ordnance Factory Apprentices Online Form 2026', yil, eng, None, 2026, 300, 'D', d(3,3), 'Closed'),
            ('Bihar BTSC Junior Engineer JE Online Form 2026', btsc, eng, BR, 2026, 583, 'C', d(30,1), 'Closed'),
            ('BTSC Pump Operator Online Form 2026 Re Open', btsc, eng, BR, 2026, 200, 'D', d(8,2), 'Closed'),
            ('Indian Navy SSC Officers Various Post ST 2027 Online Form', navy, dfc, None, 2026, 50, 'A', d(24,2), 'Closed'),
            ('Exim Bank Deputy Managers Online Form 2026', eximb, bnk, None, 2026, 35, 'A', d(15,2), 'Closed'),
            ('Army JAG 124 Entry Online Form 2026', army, dfc, None, 2026, 14, 'A', d(27,2), 'Closed'),
            ('Rajasthan RSSB Lab Assistant Online Form 2026', rssb, med, RJ, 2026, 1200, 'C', d(25,2), 'Closed'),
            ('HSSC Haryana Police Constable Online Form 2026', hssc, pol, HR, 2026, 7000, 'D', d(31,1), 'Closed'),
            ('Bihar Police BPSSC Sub Inspector Prohibition Online Form 2026', bpssc, pol, BR, 2026, 200, 'C', d(27,2), 'Closed'),
            ('UPPSC Medical Officer Online Form 2026', uppsc, med, UP, 2026, 2500, 'B', d(22,1), 'Closed'),
            ('RSSB Agriculture Supervisor Online Form 2026', rssb, psc, RJ, 2026, 430, 'C', d(11,2), 'Closed'),
            ('Bihar Police BPSSC Havildar Clerk Home Guard Online Form 2026', bpssc, pol, BR, 2026, 500, 'D', d(5,2), 'Closed'),
            ('Rajasthan RSSB LDC Jr Assistant Online Form 2026', rssb, cen, RJ, 2026, 2100, 'D', d(13,2), 'Closed'),
            ('RPSC Protection Officer Online Form 2026', rpsc, psc, RJ, 2026, 39, 'B', d(22,1), 'Closed'),
            ('Supreme Court SCI Law Clerk Online Form 2026', sci, psc, None, 2026, 50, 'A', d(7,2), 'Closed'),
            ('RBI Office Attendant Online Form 2026', rbi, bnk, None, 2026, 510, 'D', d(4,2), 'Closed'),
            ('Bank of Maharashtra Apprentices Online Form 2026', bom, bnk, None, 2026, 600, 'D', d(25,1), 'Closed'),
            ('Exim Bank Management Trainee MT Online Form 2026', eximb, bnk, None, 2026, 70, 'A', d(1,2), 'Closed'),
            ('MPESB ITI Training Officer Online Form 2026', mpesb, tch, MP, 2026, 300, 'C', d(31,1), 'Closed'),
            ('IFFCO Phulpur Apprentices Online Form 2026', iffco, eng, None, 2026, 200, 'D', d(29,1), 'Closed'),
            ('UP Police Constable Online Form 2026 Last Date 31 Jan', upsssc, pol, UP, 2026, 60244, 'D', d(31,1), 'Closed'),
            ('Nabard Development Assistant Online Form 2026', nabard, bnk, None, 2026, 152, 'C', d(3,2), 'Closed'),
            ('UPSSSC Lekhpal Online Form 2026', upsssc, psc, UP, 2026, 7882, 'C', d(28,1), 'Closed'),
            ('Indian Coast Guard Navik Yantrik CGEPT 01/2026 02/2026 Online Form', cg, dfc, None, 2026, 320, 'D', d(25,6,2025), 'Closed'),
        ]

        count = 0
        for row in jobs:
            title, org, cat, state, year, vac, level, end_date, forced_status = row
            if org is None:
                self.stdout.write(self.style.WARNING(f'  SKIP (no org): {title}'))
                continue

            final_status = forced_status if forced_status else status(end_date)

            obj, created = JobPosting.objects.update_or_create(
                title=title,
                year=year,
                defaults=dict(
                    organization=org,
                    exam_category=cat,
                    state=state,
                    vacancies=vac,
                    job_level=level,
                    application_end_date=end_date,
                    status=final_status,
                    description=f'{title}. Apply online before the last date.',
                    slug=safe_slug(title, year) if not JobPosting.objects.filter(title=title, year=year).exists() else JobPosting.objects.filter(title=title, year=year).first().slug,
                ),
            )
            if created:
                count += 1
                self.stdout.write(f'  + {title}')
            else:
                self.stdout.write(f'  ~ updated: {title}')

        return count
