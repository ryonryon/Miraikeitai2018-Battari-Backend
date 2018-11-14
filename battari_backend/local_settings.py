import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'battari',
        'USER': 'root',
        # 'PASSWORD': db_passwd,
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
