# content/management/commands/import_initial_data.py

from django.core.management.base import BaseCommand
from content.models import Organization, ExamCategory, State, QualificationLevel


class Command(BaseCommand):
    help = 'Import initial reference data (organizations, categories, states)'

    def handle(self, *args, **options):
        self.stdout.write('Starting initial data import...')
        
        # Organizations
        organizations_data = [
            {'name': 'Staff Selection Commission', 'slug': 'ssc', 'website': 'https://www.ssc.nic.in', 'is_featured': True},
            {'name': 'Union Public Service Commission', 'slug': 'upsc', 'website': 'https://www.upsc.gov.in', 'is_featured': True},
            {'name': 'Railway Board', 'slug': 'rrb', 'website': 'https://www.rrbcdg.gov.in', 'is_featured': True},
            {'name': 'IBPS', 'slug': 'ibps', 'website': 'https://www.ibps.in', 'is_featured': True},
            {'name': 'SBI', 'slug': 'sbi', 'website': 'https://www.sbi.co.in/careers', 'is_featured': True},
            {'name': 'RBI', 'slug': 'rbi', 'website': 'https://www.rbi.org.in', 'is_featured': False},
            {'name': 'GATE', 'slug': 'gate', 'website': 'https://gate.iitm.ac.in', 'is_featured': False},
        ]
        
        for org_data in organizations_data:
            org, created = Organization.objects.get_or_create(
                slug=org_data['slug'],
                defaults=org_data
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f'✓ Created organization: {org.name}'))
        
        # Exam Categories
        categories_data = [
            {'name': 'Bank', 'slug': 'bank', 'icon': 'fas fa-university', 'is_featured': True},
            {'name': 'Railway', 'slug': 'railway', 'icon': 'fas fa-train', 'is_featured': True},
            {'name': 'Police', 'slug': 'police', 'icon': 'fas fa-shield-alt', 'is_featured': True},
            {'name': 'Teaching', 'slug': 'teaching', 'icon': 'fas fa-chalkboard-user', 'is_featured': True},
            {'name': 'GATE', 'slug': 'gate', 'icon': 'fas fa-graduation-cap', 'is_featured': True},
            {'name': 'Civil Service', 'slug': 'civil-service', 'icon': 'fas fa-briefcase', 'is_featured': False},
            {'name': 'Defence', 'slug': 'defence', 'icon': 'fas fa-shield', 'is_featured': False},
            {'name': 'Insurance', 'slug': 'insurance', 'icon': 'fas fa-heart', 'is_featured': False},
        ]
        
        for cat_data in categories_data:
            cat, created = ExamCategory.objects.get_or_create(
                slug=cat_data['slug'],
                defaults=cat_data
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f'✓ Created category: {cat.name}'))
        
        # States
        states_data = [
            {'name': 'Uttar Pradesh', 'code': 'UP', 'is_featured': True},
            {'name': 'Bihar', 'code': 'BR', 'is_featured': True},
            {'name': 'Madhya Pradesh', 'code': 'MP', 'is_featured': True},
            {'name': 'Rajasthan', 'code': 'RJ', 'is_featured': True},
            {'name': 'Haryana', 'code': 'HR', 'is_featured': True},
            {'name': 'West Bengal', 'code': 'WB', 'is_featured': False},
            {'name': 'Tamil Nadu', 'code': 'TN', 'is_featured': False},
            {'name': 'Karnataka', 'code': 'KA', 'is_featured': False},
            {'name': 'Andhra Pradesh', 'code': 'AP', 'is_featured': False},
            {'name': 'Gujarat', 'code': 'GJ', 'is_featured': False},
            {'name': 'Punjab', 'code': 'PB', 'is_featured': False},
            {'name': 'Assam', 'code': 'AS', 'is_featured': False},
            {'name': 'Odisha', 'code': 'OD', 'is_featured': False},
            {'name': 'Telangana', 'code': 'TS', 'is_featured': False},
            {'name': 'Maharashtra', 'code': 'MH', 'is_featured': False},
        ]
        
        for state_data in states_data:
            state, created = State.objects.get_or_create(
                code=state_data['code'],
                defaults=state_data
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f'✓ Created state: {state.name}'))
        
        self.stdout.write(self.style.SUCCESS('\n✓ Initial data import completed successfully!'))
