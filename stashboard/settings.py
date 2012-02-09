import os

DEBUG = False

SITE_NAME = "8thBridge Status"
SITE_AUTHOR = "Colonel Mustache"
SITE_URL = "http://8thbridgestatus.appspot.com"
REPORT_URL = "mailto:admin@8thbridge.com"

# OAuth Consumer Credentials
CONSUMER_KEY = 'anonymous'
CONSUMER_SECRET = 'anonymous'

TEMPLATE_DIRS = (os.path.join(os.path.dirname(__file__), "templates"))
