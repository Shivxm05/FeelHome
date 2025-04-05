from django.conf import settings
from  property.models import BuildingType, SaleType


def site_details(request):
    context_data = dict()
    context_data['custom_site_name'] = "FEELHOME"
    context_data['custom_site_author'] = "Shivam"
    context_data['custom_site_keywords'] = "real estate, property, home, house, apartment"
    context_data['custom_site_telephone'] = '+91-82950xxxxxx'  # Replace with your phone number
    context_data['custom_site_email'] = 'shivam.kaushik1605@gmail.com'  # Replace with your email
    context_data['custom_site_address'] = 'kharar, mohali, punjab, india'

    # context_data['MEDIA_URL'] = settings.MEDIA_URL
    context_data['property_sale_type_list'] = SaleType.objects.all()
    context_data['property_building_type_list'] = BuildingType.objects.all()

    context_data['MEDIA_URL'] = settings.MEDIA_URL

    return context_data
