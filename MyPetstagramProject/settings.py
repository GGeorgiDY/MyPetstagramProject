from pathlib import Path
from django.urls import reverse_lazy

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-8kzsiyxr-pz$+)#1jd5p(pv-zh2@a_d*42e((oku)eqbfb_ppn'

# ако е False, тогава ще ми се отворя 404.html файла, но ще ми се счупят статичните файлове. За това трябва да използвам nginx, който да се грижи за тях на даден сървър.
DEBUG = True

ALLOWED_HOSTS = []

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # My apps
    'MyPetstagramProject.photos',
    'MyPetstagramProject.pets',
    'MyPetstagramProject.accounts',
    'MyPetstagramProject.common',
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

ROOT_URLCONF = 'MyPetstagramProject.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates']
        ,
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

WSGI_APPLICATION = 'MyPetstagramProject.wsgi.application'

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "my_petstagram_db",
        "USER": "georgiadmin",
        "PASSWORD": "adminpass",
        "HOST": "127.0.0.1",
        "PORT": "5432",
    }
}

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

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

# статичните ми файлове ще бъдат достъпвани на static
STATIC_URL = '/static/'
# но ще се намират на директория staticfiles
STATICFILES_DIRS = (BASE_DIR / 'staticfiles',)

# медиафайловете ми файлове ще бъдат достъпвани на media
MEDIA_URL = '/media/'
# но ще се намират на директория media_files
MEDIA_ROOT = BASE_DIR / 'mediafiles'


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# това е нещо с което казваме на джанго, че искаме за юзъри вече да не използваш твой си build-in юзър, а да използва този accounts.AppUser
AUTH_USER_MODEL = 'accounts.AppUser'

# като натисна някакъв login бутон, да ме препраща на index страницата
LOGIN_REDIRECT_URL = reverse_lazy('index')
