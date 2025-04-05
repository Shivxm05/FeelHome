import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'real_estate.settings')
django.setup()

from django.contrib.auth.models import User

def create_superuser():
    try:
        # Check if superuser exists
        if User.objects.filter(is_superuser=True).exists():
            print("Superuser already exists!")
            return
        
        # Create superuser
        User.objects.create_superuser(
            username='admin',
            email='admin@feelhome.com',
            password='admin123'  # Make sure to change this password
        )
        print("Superuser created successfully!")
        print("Username: admin")
        print("Password: admin123")
        print("Please change this password after first login!")
        
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == '__main__':
    create_superuser() 