import os

from utils.dotter import Dotter
from utils.envsafer import generate_openai_env
from utils.downloader import download_url
from config.config import TEMP_FOLDER, ROOT_FOLDER
from core.base.base_installer import BaseInstaller

PACKAGE_SERVICE          = "commit_msg"
PACKAGE_ZIP_URL          = "https://github.com/OuYangMinOa/AI-analyse-commit-msg/releases/download/v1.0.11/check_commit_msg.zip"
PACKAGE_VERSION_URL      = "https://github.com/OuYangMinOa/AI-analyse-commit-msg/releases/download/v1.0.11/version.txt"
PACKAGE_EXECUTABLE_NAME  = "check_commit_msg"
PACKAGE_COMMAND_NAME     = "commit-msg"

class CommitMsgInstaller(BaseInstaller):
    def __init__(self):
        super().__init__(
            PACKAGE_SERVICE,
            PACKAGE_ZIP_URL, 
            PACKAGE_VERSION_URL, 
            PACKAGE_EXECUTABLE_NAME, 
            PACKAGE_COMMAND_NAME
            )
    
    def git_hook(self):
        # generate_openai_env()
        git_path = ".git/hooks"
        if os.path.exists(git_path):
            hook_path = os.path.join(git_path, "commit-msg")
            with open(hook_path, "w") as f:
                f.write(
                    "#!/bin/sh\n"
                    f"if [[ -f '{self.EXECUTABLE_PATH}' ]]; then\n"
                    "echo '[*] It takes times to open, plz wait ...'\n"
                    f"'{self.EXECUTABLE_PATH}'\n"
                    "fi"
                    )
            print("The git hook is installed.")
        else:
            print("The git repository is not initialized.")
            print("Please run `git init` to initialize the repository.")
            return
    
    def remove_git_hook(self):
        git_path = ".git/hooks"
        if os.path.exists(git_path):
            hook_path = os.path.join(git_path, "commit-msg")
            if os.path.exists(hook_path):
                os.remove(hook_path)
                print("The git hook is removed.")
            else:
                print("The git hook is not installed.")

        