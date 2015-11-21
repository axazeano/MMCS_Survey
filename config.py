import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    MONGODB_SETTINGS = {'DB': "MMCS_survey"}
    SECRET_KEY = ""


    # SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    # SQLALCHEMY_RECORD_QUERIES = True
    # MAIL_SERVER = 'smtp.googlemail.com'
    # MAIL_PORT = 587
    # MAIL_USE_TLS = True
    # MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    # MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    # FLASKY_MAIL_SUBJECT_PREFIX = '[Flasky]'
    # FLASKY_MAIL_SENDER = 'Flasky Admin <flasky@example.com>'
    # FLASKY_ADMIN = os.environ.get('FLASKY_ADMIN')
    # FLASKY_POSTS_PER_PAGE = 20
    # FLASKY_FOLLOWERS_PER_PAGE = 50
    # FLASKY_COMMENTS_PER_PAGE = 30
    # FLASKY_SLOW_DB_QUERY_TIME=0.5