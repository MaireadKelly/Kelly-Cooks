from pathlib import Path
import os

import dj_database_url
from dotenv import load_dotenv
import cloudinary

load_dotenv()

# -----------------------------------------------------
# Core
# -----------------------------------------------------
BASE_DIR = Path(__file__).resolve().parent.parent

# Read DEBUG from env: True locally, False on Heroku
DEBUG = os.getenv("DEBUG", "False").strip().lower() == "true"

# Secret key from env
SECRET_KEY = os.getenv("SECRET_KEY", "change-me-in-env")

# Hosts
ALLOWED_HOSTS = [
    "kellycookspp4-63d6db43ef5f.herokuapp.com",
    "localhost",
    "127.0.0.1",
]
# Allow lvh.me for local dev (resolves to 127.0.0.1)
if DEBUG:
    ALLOWED_HOSTS += ["lvh.me", ".lvh.me"]

# CSRF trusted origins (Django 5 requires scheme + host [+ port])
CSRF_TRUSTED_ORIGINS = [
    "https://kellycookspp4-63d6db43ef5f.herokuapp.com",
    "https://*.herokuapp.com",
    "https://*.codeinstitute-ide.net",
    "http://127.0.0.1:8000",
    "http://localhost:8000",
]
if DEBUG:
    CSRF_TRUSTED_ORIGINS += [
        "http://127.0.0.1:8001",
        "http://localhost:8001",
        "http://lvh.me:8000",
        "http://lvh.me:8001",
    ]

# Optional env override for extra hosts without code changes
_env_hosts = os.getenv("ALLOWED_HOSTS")
if _env_hosts:
    ALLOWED_HOSTS += [h.strip() for h in _env_hosts.split(",") if h.strip()]

# Locale
LANGUAGE_CODE = "en-us"
TIME_ZONE = "Europe/Dublin"
USE_I18N = True
USE_TZ = True

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# -----------------------------------------------------
# Applications
# -----------------------------------------------------
INSTALLED_APPS = [
    # Django
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.sites",
    # Third-party
    "cloudinary",
    "cloudinary_storage",
    "crispy_forms",
    "crispy_bootstrap5",
    "allauth",
    "allauth.account",
    "allauth.socialaccount",
    "django_resized",
    "djrichtextfield",
    # APPS
    "home",
    "recipes",
]

SITE_ID = 1

# djrichtextfield toolbar (keep minimal)
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

CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"
CRISPY_TEMPLATE_PACK = "bootstrap5"

AUTHENTICATION_BACKENDS = [
    "django.contrib.auth.backends.ModelBackend",
    "allauth.account.auth_backends.AuthenticationBackend",
]

# Allauth basics
ACCOUNT_AUTHENTICATION_METHOD = "username_email"
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_USERNAME_REQUIRED = True
ACCOUNT_USERNAME_MIN_LENGTH = 4
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_EMAIL_VERIFICATION = "none"  # adjust if you enable emails
LOGIN_URL = "/accounts/login/"
LOGIN_REDIRECT_URL = "/"
ACCOUNT_LOGOUT_REDIRECT_URL = "/"

# -----------------------------------------------------
# Middleware
# -----------------------------------------------------
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",  # serve static in prod
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "allauth.account.middleware.AccountMiddleware",
]

# -----------------------------------------------------
# Templates
# -----------------------------------------------------
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
                "django.template.context_processors.request",  # allauth needs this
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

ROOT_URLCONF = "main.urls"
WSGI_APPLICATION = "main.wsgi.application"

# -----------------------------------------------------
# Database (Heroku Postgres via DATABASE_URL, else local sqlite)
# -----------------------------------------------------
if os.getenv("DATABASE_URL"):
    DATABASES = {
        "default": dj_database_url.parse(
            os.getenv("DATABASE_URL"),
            conn_max_age=600,
            ssl_require=not DEBUG,
        )
    }
else:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": BASE_DIR / "db.sqlite3",
        }
    }

# -----------------------------------------------------
# Password validation
# -----------------------------------------------------
AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

# -----------------------------------------------------
# Static & Media
# -----------------------------------------------------
STATIC_URL = "/static/"
STATICFILES_DIRS = [BASE_DIR / "static"]
STATIC_ROOT = BASE_DIR / "staticfiles"

# WhiteNoise compressed/hashed static files
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

# Cloudinary media storage (HTTPS enforced)
DEFAULT_FILE_STORAGE = "cloudinary_storage.storage.MediaCloudinaryStorage"
cloudinary.config(secure=True)
CLOUDINARY_SECURE = True

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

# -----------------------------------------------------
# Security – production only
# -----------------------------------------------------
if not DEBUG:
    SECURE_SSL_REDIRECT = True
    SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True
    SECURE_HSTS_SECONDS = 31536000
    SECURE_HSTS_INCLUDE_SUBDOMAINS = True
    SECURE_HSTS_PRELOAD = True
    # Optional hardening
    SECURE_CONTENT_TYPE_NOSNIFF = True
    SECURE_REFERRER_POLICY = "strict-origin-when-cross-origin"
