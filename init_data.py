import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'real_estate.settings')
django.setup()

from property.models import BuildingType, SaleType

# Create Building Types
building_types = [
    {
        'name': 'Apartment',
        'description': 'Multi-unit residential building'
    },
    {
        'name': 'House',
        'description': 'Single family residential house'
    },
    {
        'name': 'Villa',
        'description': 'Luxury residential property'
    },
    {
        'name': 'Commercial',
        'description': 'Property for business use'
    },
    {
        'name': 'Land',
        'description': 'Undeveloped property'
    }
]

# Create Sale Types
sale_types = [
    {
        'name': 'For Sale',
        'description': 'Properties available for purchase'
    },
    {
        'name': 'For Rent',
        'description': 'Properties available for rent'
    },
    {
        'name': 'Lease',
        'description': 'Properties available for long-term lease'
    }
]

# Add Building Types
for btype in building_types:
    BuildingType.objects.get_or_create(
        name=btype['name'],
        description=btype['description']
    )

# Add Sale Types
for stype in sale_types:
    SaleType.objects.get_or_create(
        name=stype['name'],
        description=stype['description']
    )

print("Initial data has been added successfully!") 