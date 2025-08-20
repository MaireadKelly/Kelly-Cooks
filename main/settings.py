import os
from pathlib import Path

import dj_database_url
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False


ALLOWED_HOSTS = [
    "kellycookspp4-63d6db43ef5f.herokuapp.com",
    ".herokuapp.com",
    "127.0.0.1",
    "localhost",
]
# (Remove the old single-string assignment)


# os.getenv("ALLOWED_HOSTS", "").split(",")

# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.sites",
    "django_resized",
    "allauth",
    "allauth.account",
    "allauth.socialaccount",
    # APPS
    "home",
    "recipes",
    # OTHER
    "crispy_forms",
    "crispy_bootstrap5",
    "cloudinary",
    "cloudinary_storage",
    "djrichtextfield",
]

SITE_ID = 1

DJRICHTEXTFIELD_CONFIG = {
    "settings": {
        "toolbar": [
            ["Format", "Bold", "Italic", "Underline"],
            ["NumberedList", "BulletedList"],
            ["Undo", "Redo"],
            ["Maximize"],
        ],
        "format_tags": "p;h1;h2;h3",
    }
}

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "allauth.account.middleware.AccountMiddleware",
]

CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"
CRISPY_TEMPLATE_PACK = "bootstrap5"

ROOT_URLCONF = "main.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            BASE_DIR / "templates",
            BASE_DIR / "templates/account",
        ],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
            "builtins": [
                "crispy_forms.templatetags.crispy_forms_tags",
                "crispy_forms.templatetags.crispy_forms_field",
            ],
        },
    },
]

AUTHENTICATION_BACKENDS = [
    "django.contrib.auth.backends.ModelBackend",
    "allauth.account.auth_backends.AuthenticationBackend",
]

WSGI_APPLICATION = "main.wsgi.application"

# Database configuration

DATABASES = {
    "default": dj_database_url.parse(
        os.getenv("DATABASE_URL"), conn_max_age=600, ssl_require=True
    )
}

CSRF_TRUSTED_ORIGINS = [
    "https://kellycookspp4-63d6db43ef5f.herokuapp.com",
    "https://*.herokuapp.com",
    "https://*.codeinstitute-ide.net",
    "http://127.0.0.1:8000",  # for local dev
    "http://localhost:8000",
]


# Password validation

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": (
            "django.contrib.auth.password_validation."
            "UserAttributeSimilarityValidator"
        ),
    },
    {
        "NAME": ("django.contrib.auth.password_validation." "MinimumLengthValidator"),
    },
    {
        "NAME": ("django.contrib.auth.password_validation." "CommonPasswordValidator"),
    },
    {
        "NAME": ("django.contrib.auth.password_validation." "NumericPasswordValidator"),
    },
]

LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True

# Account setup

ACCOUNT_AUTHENTICATION_METHOD = "username_email"
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_USERNAME_REQUIRED = True
ACCOUNT_USERNAME_MIN_LENGTH = 4
ACCOUNT_UNIQUE_EMAIL = True  # (usually set by default)
LOGIN_URL = "/accounts/login/"
LOGIN_REDIRECT_URL = "/"

# Disable email verification for registration

ACCOUNT_EMAIL_VERIFICATION = "none"

# Static files and media

STATIC_URL = "/static/"
STATICFILES_DIRS = [BASE_DIR / "static"]
STATIC_ROOT = BASE_DIR / "staticfiles"

DEFAULT_FILE_STORAGE = "cloudinary_storage.storage.MediaCloudinaryStorage"
MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
