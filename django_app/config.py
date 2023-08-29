import os
from dotenv import load_dotenv
load_dotenv()

BASE = os.getenv('BASE_DIR')
DEBUG = os.getenv('DEBUG', False) == 'True'
ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS')
POSTGRES_ENGINE=os.getenv('POSTGRES_ENGINE', 'django.db.backends.sqlite3')
POSTGRES_DB=os.getenv('POSTGRES_DB', os.path.join(BASE, 'db.sqlite3'))
POSTGRES_USER=os.getenv('POSTGRES_USER', 'user')
POSTGRES_PASSWORD=os.getenv('POSTGRES_PASSWORD', 'password')
POSTGRES_HOST=os.getenv('POSTGRES_HOST', 'localhost')
POSTGRES_PORT=os.getenv('POSTGRES_PORT', '5432')

