'''
This module defines the DefaultConfig the app expects.
The TestConfig class is used for unit test.  I'm not sure
it belongs here.

For production, a production config should be created outside
of the app source code in a file, pointed to by FLASK_CONFIG
env var.

# https://flask.palletsprojects.com/en/1.1.x/config/
'''
class DefaultConfig:
    ''' Default config settings that can be overridden '''
    APP_NAME = "NGS360"
    TESTING = False

    # For production, define these env vars:
    # FLASK_LOG_FILE = /path/to/log/file
    # FLASK_LOG_LEVEL = INFO

    # Email error log settings
    # MAIL_SERVER = mailserver
    # MAIL_PORT
    # MAIL_USERNAME = set to mail server login, if needed
    # MAIL_PASSWORD =
    # MAIL_USE_TLS = True
    # ADMINS = comma separate list of who should get emailed

class TestConfig(DefaultConfig):
    ''' Config settings for unit testing '''
    TESTING = True
