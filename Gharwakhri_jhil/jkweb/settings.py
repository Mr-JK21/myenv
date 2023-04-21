"""   ₹
Django settings for jkweb project.
 
Generated by 'django-admin startproject' using Django 4.1.5.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-k@3!^@btb3**(4yz%o3$li_60g#xz+*jn*+e-y^fl_85n&y+o+'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    # 'django.db',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'accounts',
    'catalog',
    # 'cartapp',
    # 'feedback',

    
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'jkweb.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'jkweb.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'dj',
        'USER': 'root',
        'PASSWORD': 'jk108912',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]



# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

# STATIC_URL = 'static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
    os.path.join(BASE_DIR, 'backendstatic'),
]

STATIC_URL = '/static/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'storable-media')

LOGIN_URL = '/loginin/'



# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field


# CATEGORIES = {
#     'General Store': 'General Store',
#     'Snacks': 'Snacks',
#     'Sweets': 'Sweets',
#     'Electronics': 'Electronics',
#     'Fruits': 'Fruits',
#     'Vegetables': 'Vegetables',
#     'Dairy': 'Dairy',
#     'Paan Parlour': 'Paan Parlour',
#     'Stationary': 'Stationary',
#     'Toys': 'Toys',
#     'Gifts': 'Gifts',
#     'Watch': 'Watch',
#     'Mobile': 'Mobile',
#     'Women Clothes': 'Women Clothes',
#     'Men Clothes': 'Men Clothes',
#     'Children Wear': 'Children Wear',
#     'Summer Wear': 'Summer Wear',
#     'Winter Wear': 'Winter Wear',
# }


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# STATICFILES_DIRS = [
#     BASE_DIR,"static"
# ]