from .base import * # NOQA


DEBUG = True

#ALLOWED_HOSTS = ['*']

#SECRET_KEY = '0*8@$qfoyi$rim(^798h9ue(uqug4in1pv7py5rm#lfq$4)ga-'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
