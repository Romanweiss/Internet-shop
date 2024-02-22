from pathlib import Path

# from django.conf.global_settings import STATICFILES_DIRS  # импорт, тк в конце файла указана, он не нужен

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-jkkd5!v%y%_m%e*fqvj9uljp5-&9&ls)5q94wids#gtms_yw3l"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True  # показывает ошибки при разработке, на продакшене меняем значение на False

ALLOWED_HOSTS = ["*"]


# Application definition

INSTALLED_APPS = [  # здесь происходит регистрация приложений
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",  # приложение, которое обслуживает и ищет статические файлы
    "debug_toolbar",  # добавляем приложение дебагер
    "main",
    "goods",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "debug_toolbar.middleware.DebugToolbarMiddleware",  # добавляем слой дебагера
]

ROOT_URLCONF = "app.urls"

TEMPLATES = [  #
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",  # наименование подключенного шаблонизатора
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",  # слой отвечающий за дебаг шаблонов - проверяет теги - {}
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "app.wsgi.application"


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {  # указывает на используемую в приложении БД
    "default": {
        "ENGINE": "django.db.backends.sqlite3",  # используемый движок
        "NAME": BASE_DIR / "db.sqlite3",
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = "ru"  # язык проекта и админ панели

TIME_ZONE = "UTC"  # временная зона

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = "static/"  # префикс к url адресу для статики

STATICFILES_DIRS = [
    BASE_DIR / "static"
]  # пропишем новый путь для static папки, тк во всех приложениях
# будут использоваться одни и те же статические файлы (в противном случае можно не прописывать, а создавать отдельно
# в каждом приложении папку static).
# для специфической статики - создаём отдельно папки в приложениях - по аналогии с templates (static -> название приложения)

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

INTERNAL_IPS = [  # также для дебагера sql запросов
    # ...
    "127.0.0.1",
    # ...
]

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"  # для создания id от 1 в бд по порядковому номеру с автоматической инкрементацией
