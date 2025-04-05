import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'real_estate.settings')
django.setup()

from django.contrib.auth.models import User
from agent.models import Agent

try:
    # Find the user with username or full name containing "Shiva"
    user = User.objects.filter(username__icontains='shiva').first() or \
           User.objects.filter(first_name__icontains='shiva').first() or \
           User.objects.filter(last_name__icontains='shiva').first()
    
    if user:
        # Delete the associated agent profile
        try:
            agent = Agent.objects.get(user=user)
            agent.delete()
            print(f"Agent profile for {user.get_full_name() or user.username} has been deleted")
        except Agent.DoesNotExist:
            print("No agent profile found")
        
        # Delete the user account
        user.delete()
        print(f"User account for {user.username} has been deleted")
    else:
        print("No user found with name containing 'Shiva'")

except Exception as e:
    print(f"An error occurred: {str(e)}") 