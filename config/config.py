import os

__NAME__    = "ouai"
__VERSION__ = "0.1.0"
__AUTHOR__  = "ouyangminwei"

USER_FOLDER = os.path.expanduser(r"~")
ROOT_FOLDER = os.path.join(USER_FOLDER, f"{__NAME__}")
TEMP_FOLDER = os.path.join(ROOT_FOLDER, ".temp")

os.makedirs(TEMP_FOLDER, exist_ok=True)
os.makedirs(ROOT_FOLDER, exist_ok=True)
