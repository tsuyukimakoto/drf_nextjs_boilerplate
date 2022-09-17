from .base import *

DEBUG = True

ALLOWED_HOSTS = ["localhost"]

INSTALLED_APPS = INSTALLED_APPS + [
    "rest_framework",
    "app1",
]
