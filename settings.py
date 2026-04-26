
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'content', // The project
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': '', // Add a name
        'USER': '', // Add a user
        'PASSWORD': '', // Add a password
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

STATIC_URL = 'static/'

LOGIN_REDIRECT_URL = '/posts/'


LOGOUT_REDIRECT_URL = '/accounts/login/' 
