SECRET_KEY = 'django-insecure-avz#214a*_i1+^+w$5&5@o=z9ihwjk*jp5b4u2gy+in_pq8b#f'
DEBUG = True
ALLOWED_HOSTS = []
from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent.parent
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
