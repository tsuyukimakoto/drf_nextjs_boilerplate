from .local import *

import os
from dotenv import load_dotenv

MYSQL_ENV_FILE = BASE_DIR.parent.parent / "mysql/.env"
if not MYSQL_ENV_FILE.exists():
  raise ValueError("need %s", MYSQL_ENV_FILE)

load_dotenv(MYSQL_ENV_FILE)

import pymysql
pymysql.install_as_MySQLdb()

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.environ["MYSQL_DATABASE"],
        'USER': os.environ["MYSQL_USER"],
        'PASSWORD': os.environ["MYSQL_PASSWORD"],
    }
}
