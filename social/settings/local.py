from .base import *
from .db import POSTGRESQL
DEBUG = True

ALLOWED_HOSTS = []

DATABASES = POSTGRESQL

STATIC_URL = '/static/'