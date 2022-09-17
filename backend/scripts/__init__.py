import os
from pathlib import Path
import sys

ROOT_DIR = Path(__file__).resolve().parent.parent

os.environ["DJANGO_SETTINGS_MODULE"] = "prj.settings.local"
os.environ["PYTHONPATH"] = "{ROOT_DIR}:{PYTHONPATH}".format(
    ROOT_DIR=ROOT_DIR,
    PYTHONPATH=":".join(sys.path),
)
