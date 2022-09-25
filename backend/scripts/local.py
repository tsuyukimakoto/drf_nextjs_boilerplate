from audioop import add
from dotenv import load_dotenv
import os
from pathlib import Path
import subprocess
import sys

BASE_COMMAND = [
    "python",
    "prj/manage.py",
]
ROOT_DIR = Path(__file__).resolve().parent.parent

load_dotenv()
os.environ["PYTHONPATH"] = "{ROOT_DIR}:{PYTHONPATH}".format(
    ROOT_DIR=ROOT_DIR,
    PYTHONPATH=":".join(sys.path),
)


def __run(additional_command):
    subprocess.run(BASE_COMMAND + additional_command)


def shell():
    __run(["shell"])


def server():
    __run(["runserver"])


def make_migrations():
    __run(["makemigrations"])


def migrate():
    __run(["migrate"])


def createsuperuser():
    __run(["createsuperuser"])
