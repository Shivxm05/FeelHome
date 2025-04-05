# FeelHome
Welcome to FeelHome, your real estate management platform. This project is designed to help agencies efficiently manage properties, agents, bookings, and client interactions using a streamlined web interface.

By default, this project includes a Django backend, basic frontend templates, and a SQLite database to get you up and running quickly. You are encouraged to customize and expand the features to meet your agency’s specific needs.

To get started, explore the project directory, review the Django settings, and begin working in your preferred development environment. This setup is fully local and does not affect any production environment.

---
Navigate into the root folder and run the following commands
1. pip install -r requirement.txt
2. python manage.py collectstatic
3. python manage.py makemigrations
4. python manage.py migrate
5. python manage.py shell
---

If you want to test your FeelHome project locally, follow these steps:
```bash
# Activate the virtual environment
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
# Apply database migrations
python manage.py migrate
# Start the development server
python manage.py runserver
http://localhost:8000/
http://localhost:8000/admin/
python manage.py createsuperuser
```
---
You can tailor FeelHome to fit your business requirements by:
- Adding custom fields or models (e.g., property reviews, pricing history)
- Extending the admin dashboard for better control
- Improving UI using modern frontend frameworks or design libraries
- Integrating external services like email, maps, or payment gateways
