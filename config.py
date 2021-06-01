import os


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'testsecretkey'

    WTF_CSRF_ENABLED = True

    LOG_TO_STDOUT = os.environ.get('LOG_TO_STDOUT')

    CELERY_BROKER_URL = 'redis://localhost:6379/0'
    CELERY_BACKEND_URL = 'redis://localhost:6379/0'
