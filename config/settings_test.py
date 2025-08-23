import os
import environ
from config.settings import BASE_DIR

env = environ.Env(
    DEBUG=(bool, False),
    SECRET_KEY=(str, "test-secret-key"),
    DATABASE_URL=(str, "sqlite:///:memory:"),
)

environ.Env.read_env(os.path.join(BASE_DIR, ".env.test"))

DEBUG = env("DEBUG")
SECRET_KEY = env("SECRET_KEY")
ALLOWED_HOSTS = ["*"]

INSTALLED_APPS = [
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "rest_framework",
    "drf_spectacular",
    "productos",  
]


DATABASES = {
    "default": env.db(),  
}

EMAIL_BACKEND = "django.core.mail.backends.locmem.EmailBackend"

AUDITLOG_INCLUDE_ALL_MODELS = True
AUDITLOG_DISABLE_ON_TEST = False

MEDIA_ROOT = env("MEDIA_ROOT", default=os.path.join(BASE_DIR, "test_media"))
MEDIA_URL = "/media/"

TEST_CSV_PATH = env("TEST_CSV_PATH", default=os.path.join(BASE_DIR, "tests", "mocks", "productos.csv"))
TEST_IMAGE_PATH = env("TEST_IMAGE_PATH", default=os.path.join(BASE_DIR, "tests", "mocks", "img"))

LANGUAGE_CODE = "es-cl"
TIME_ZONE = "America/Santiago"
USE_I18N = True
USE_TZ = True

CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.dummy.DummyCache",
    }
}

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {
        "console": {"class": "logging.StreamHandler"},
    },
    "root": {
        "handlers": ["console"],
        "level": "WARNING",
    },
}

TEST_RUNNER = "django.test.runner.DiscoverRunner"
