import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'real_estate.settings')
django.setup()

from django.contrib.auth.models import User
from agent.models import Agent
from django.utils import timezone

def create_agent(username, password, first_name, last_name, email, phone, address, description):
    try:
        # Create user account
        user = User.objects.create_user(
            username=username,
            password=password,
            first_name=first_name,
            last_name=last_name,
            email=email
        )
        
        # Create agent profile
        agent = Agent.objects.create(
            user=user,
            telephone=phone,
            address=address,
            description=description,
            date_added=timezone.now()
        )
        
        print(f"Agent {first_name} {last_name} created successfully!")
        return True
        
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return False

# Example usage - you can modify these details
agent_details = {
    'username': 'newagent',
    'password': 'agent123',  # Make sure to use a strong password
    'first_name': 'New',
    'last_name': 'Agent',
    'email': 'newagent@feelhome.com',
    'phone': '1234567890',
    'address': 'Near Chandigarh University, Punjab',
    'description': 'Experienced real estate agent specializing in student housing near Chandigarh University.'
}

# Create the agent
create_agent(**agent_details) 