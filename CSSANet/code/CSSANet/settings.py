"""
Django settings for CSSANet project.

Generated by 'django-admin startproject' using Django 2.1.3.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os
env_dist = os.environ

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE_DIR = os.path.dirname(PROJECT_DIR)

SITE_ID = 1


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: DevKey ONLY. Replace the secret key used in production secret!


# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = True
DEBUG = False
if DEBUG == False:
    SECRET_KEY = env_dist.get('DJANGOKEYPD')
    ALLOWED_HOSTS = ['cssanet','localhost','cssaunimelb.com','192.168.0.2', '0.0.0.0']
    CSRF_COOKIE_SECURE = True
#   SESSION_COOKIE_SECURE = True ## <- Activate in HTTPS envrioment only
    SECURE_CONTENT_TYPE_NOSNIFF = True
    SECURE_BROWSER_XSS_FILTER = True
    SECURE_SSL_REDIRECT = False
    X_FRAME_OPTIONS = 'DENY'
else:
    ALLOWED_HOSTS = ['*']
    SECRET_KEY = env_dist.get('DJANGOKEYDEV')

# Application definition
INSTALLED_APPS = [
    'EventAPI',
    'LegacyDataAPI',
    'RecruitAPI',
    'UserAuthAPI',
    'FinanceAPI',
    'OrganisationMgr',    
    'PublicSite',
    'myCSSAhub',
    'BlogAPI',
    'FlexForm',

    'rest_framework',
    'rest_framework.authtoken',

    'rest_auth',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',

    'django.contrib.contenttypes',
    'grappelli.dashboard',
    'grappelli',
    'filebrowser',
    'django.contrib.sites',
    'django.contrib.admin',
    'django.contrib.auth',

    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'gunicorn',
    'widget_tweaks',
    
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.cache.UpdateCacheMiddleware',
    'django.middleware.cache.FetchFromCacheMiddleware',
]

ROOT_URLCONF = 'CSSANet.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    )
}


AUTH_USER_MODEL = 'UserAuthAPI.User'
AUTH_PROFILE_MODULE = "UserAuthAPI.UserProfile"

AUTHENTICATION_BACKENDS = (
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',
#    'UserAuthAPI.auth.EmailOrUsernameModelBackend',

#    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',
)

REST_AUTH_SERIALIZERS = {
    'LOGIN_SERIALIZER': 'UserAuthAPI.serializers.APILoginSerializer',

}
REST_AUTH_REGISTER_SERIALIZERS = {
    "REGISTER_SERIALIZER": "UserAuthAPI.serializers.AcccountInitRegisterSerializer",
}

# Base URL to use when referring to full URLs within the Wagtail admin backend -
# e.g. in notification emails. Don't include '/admin' or a trailing slash
BASE_URL = 'http://cssaunimelb.com'

# Login Settings
ACCOUNT_USER_MODEL_USERNAME_FIELD = None
ACCOUNT_AUTHENTICATION_METHOD = None
ACCOUNT_EMAIL_VERIFICATION = 'none'

ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_USER_EMAIL_FIELD = 'email'
ACCOUNT_LOGOUT_ON_GET = True

WSGI_APPLICATION = 'CSSANet.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    #'default': {
    #    'ENGINE': 'django.db.backends.sqlite3',
    #    'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    #}
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'myCSSA',
        'USER': 'postgres',
        'PASSWORD': 'aiuh489ieu19vc*4',
        'HOST': 'db',
        'PORT': '5432'
    }
}

# CACHES = {
#  'default': {
#   'BACKEND': 'django.core.cache.backends.dummy.DummyCache',  # 缓存后台使用的引擎
#   'TIMEOUT': 0,            # 缓存超时时间（默认300秒，None表示永不过期，0表示立即过期）
#   'OPTIONS':{
#    'MAX_ENTRIES': 300,          # 最大缓存记录的数量（默认300）
#    'CULL_FREQUENCY': 3,          # 缓存到达最大个数之后，剔除缓存个数的比例，即：1/CULL_FREQUENCY（默认3）
#   },
#  }
# }

# # Cache time to live is 1 minutes.
# CACHE_TTL = 1 * 1
# # Cahce ENV Setup
# #SESSION_ENGINE = "django.contrib.sessions.backends.cache"
# #SESSION_CACHE_ALIAS = "default"


# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

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

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
]

#STATICFILES_DIRS = [
#   os.path.join(PROJECT_DIR, 'static'),
#]

# ManifestStaticFilesStorage is recommended in production, to prevent outdated
# Javascript / CSS assets being served from cache (e.g. after a Wagtail upgrade).
# See https://docs.djangoproject.com/en/2.1/ref/contrib/staticfiles/#manifeststaticfilesstorage

# Temporary Disabled due to conflicts in configuration
# STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.ManifestStaticFilesStorage'

STATIC_ROOT = os.path.join(PROJECT_DIR, 'static')
STATIC_URL = '/static/'

MEDIA_ROOT = os.path.join(PROJECT_DIR, 'media')
MEDIA_URL = '/media/'


# Internationalization
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'zh-cn'

TIME_ZONE = 'Australia/Melbourne'

USE_I18N = True

USE_L10N = True

USE_TZ = True



# myCSSAHub Settings
GRAPPELLI_ADMIN_TITLE = 'myCSSAHub'
GRAPPELLI_INDEX_DASHBOARD = 'CSSANet.dashboard.CustomIndexDashboard'

# File browswer settings
from filebrowser.sites import site
site.directory = ''

FILEBROWSER_DIRECTORY = ''
FILEBROWSER_VERSIONS_BASEDIR = '_versions/'
FILEBROWSER_EXTENSIONS = {
    'Image': ['.jpg','.jpeg'],
    'Document': ['.pdf','.doc','.xls'],

}
FILEBROWSER_VERSIONS = {
    'admin_thumbnail': {'verbose_name': 'Admin Thumbnail', 'width': 60, 'height': 60, 'opts': 'crop'},
    'thumbnail': {'verbose_name': 'Thumbnail (1 col)', 'width': 60, 'height': 60, 'opts': 'crop'},
    'small': {'verbose_name': 'Small (2 col)', 'width': 140, 'height': '', 'opts': ''},
    'medium': {'verbose_name': 'Medium (4col )', 'width': 300, 'height': '', 'opts': ''},
    'big': {'verbose_name': 'Big (6 col)', 'width': 460, 'height': '', 'opts': ''},
    'large': {'verbose_name': 'Large (8 col)', 'width': 680, 'height': '', 'opts': ''}
}

### Logging configuration
LOGGING = {
	'version': 1,
	'disable_existing_loggers': False,
	'filters': {
		'require_debug_false': {
			'()': 'django.utils.log.RequireDebugFalse',
		},
		'require_debug_true': {
			'()': 'django.utils.log.RequireDebugTrue',
		},
	},
	'formatters': {
		'django.server': {
			'()': 'django.utils.log.ServerFormatter',
			'format': '[%(server_time)s] %(message)s',
		}
	},
	'handlers': {
		'console': {
			'level': 'INFO',
			'filters': ['require_debug_true'],
			'class': 'logging.StreamHandler',
		},
		'console_debug_false': {
			'level': 'ERROR',
			'filters': ['require_debug_false'],
			'class': 'logging.StreamHandler',
		},
		'django.server': {
			'level': 'INFO',
			'class': 'logging.StreamHandler',
			'formatter': 'django.server',
		},
		'mail_admins': {
			'level': 'ERROR',
			'filters': ['require_debug_false'],
			'class': 'django.utils.log.AdminEmailHandler'
		}
	},
	'loggers': {
		'django': {
			'handlers': ['console', 'console_debug_false', 'mail_admins'],
			'level': 'INFO',
		},
		'django.server': {
			'handlers': ['django.server'],
			'level': 'INFO',
			'propagate': False,
		}
	}
}

### Email Configuration
# from myCSSAhub import configuration

# email_configuration = configuration.queryEmailConfiguration

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 0
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''
