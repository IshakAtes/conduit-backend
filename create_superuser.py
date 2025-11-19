# create_superuser.py
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'conduit.settings')
django.setup()

from django.contrib.auth import get_user_model

User = get_user_model()

username = os.environ.get('SUPER_USER_NAME', 'admin')
email = os.environ.get('SUPER_USER_EMAIL', 'admin@example.com')
password = os.environ.get('SUPER_USER_PASSWORD', 'securepass')

if not User.objects.filter(username=username).exists():
    print(f'Creating superuser "{username}"...')
    User.objects.create_superuser(username=username, email=email, password=password)
    print('Superuser created successfully.')
else:
    print('Superuser already exists — skipping creation.')
