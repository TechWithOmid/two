from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent.parent

# SECRET_KEY SETTINGS
SECRET_KEY = "django-insecure-3*j%!n*4#@y7#f3533w5&o*5n7i1hp(#^qcm#$9t956#igcik&"

DEBUG = False

# Application definition
SITE_ID = 1

INSTALLED_APPS = [
    # default apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
	'django.contrib.sitemaps',

    # third party apps
    'ckeditor',
    'django_comments_xtd',
    'django_comments',

    # custom apps
    'blog',
    'comments',
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

ROOT_URLCONF = 'two.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates')
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'blog.context_processors.writer_info'
            ],
        },
    },
]

WSGI_APPLICATION = 'two.wsgi.application'


# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'blogDB',
    }
}

# Password validation
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
LANGUAGE_CODE = 'fa-ir'

TIME_ZONE = 'Asia/Tehran'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files
STATICFILES_DIRS = [os.path.join(BASE_DIR, "assets")]
STATIC_ROOT = 'static'
STATIC_URL = '/static/'

# Media Files Settings
MEDIA_ROOT = 'media'
MEDIA_URL = '/media/'

# CKEditor settings
CKEDITOR_BASEPATH = "/static/ckeditor/ckeditor/"
CKEDITOR_CONFIGS = {
'default': {

        'toolbar_YourCustomToolbarConfig': [
            {'name': 'document', 'items': [
                'Source', '-', 'Save', 'Preview', 'Print', '-', 'Templates', '-', 'CodeSnippet',
            ]},
            '/',
            {'name': 'basicstyles',
             'items': [
                 'Bold', 'Italic', 'Underline', 'Strike', 'Subscript',
                 'Superscript', '-', 'RemoveFormat'
             ]},
            {'name': 'paragraph',
             'items': [
                 'NumberedList', 'BulletedList', '-', 'Outdent', 'Indent',
                 '-', 'Blockquote', 'CreateDiv', '-', 'JustifyLeft',
                 'JustifyCenter', 'JustifyRight', 'JustifyBlock', '-',
                 'BidiLtr', 'BidiRtl', 'Language'
             ]},
            {'name': 'links', 'items': ['Link', 'Unlink', 'Anchor']},
            {'name': 'insert',
             'items': [
                 'Image', 'Table', 'HorizontalRule',
                 'Smiley', 'SpecialChar', 'PageBreak', 'Iframe'
             ]},
            '/',
            {'name': 'styles', 'items': ['Styles', 'Format', 'Font', 'FontSize']},
            {'name': 'colors', 'items': ['TextColor', 'BGColor']},
            {'name': 'tools', 'items': ['Maximize', 'ShowBlocks']},
            '/',  # put this to force next toolbar on new line
            {'name': 'yourcustomtools', 'items': [
                # put the name of your editor.ui.addButton here
                'Preview',
                'Maximize',

            ]},
        ],

        'codeSnippet_theme': 'monokai',
        'codeSnippet_languages': {
            'python': 'Python',
            'javascript': 'Javascript',
        },

        'toolbar': 'YourCustomToolbarConfig',  # put selected toolbar config here
        'tabSpaces': 4,
        'width': 'auto',
        'extraPlugins': ','.join([
            'codesnippet',
        ]),
    },
}



# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Comment Settings
COMMENTS_APP = 'django_comments_xtd'
COMMENTS_XTD_MAX_THREAD_LEVEL = 2
COMMENTS_XTD_LIST_ORDER = ('-thread_id', 'order')
COMMENTS_XTD_CONFIRM_EMAIL = False
COMMENTS_XTD_FORM_CLASS = 'comments.forms.CommentForm'
