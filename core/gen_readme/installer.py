import os
import shutil
import zipfile

from utils.dotter import Dotter
from utils.downloader import download_url
from config.config import TEMP_FOLDER, ROOT_FOLDER
from core.base.base_installer import BaseInstaller


PACKAGE_SERVICE          = "gen_readme"
PACKAGE_ZIP_URL          = None
PACKAGE_VERSION_URL      = None
PACKAGE_COMMAND_NAME     = "gen-readme"
PACKAGE_EXECUTABLE_NAME  = "gen_readme"


class ReadMeGeneratorInstaller(BaseInstaller):
    def __init__(self):
        super().__init__(
            PACKAGE_SERVICE,
            PACKAGE_ZIP_URL, 
            PACKAGE_VERSION_URL, 
            PACKAGE_EXECUTABLE_NAME, 
            PACKAGE_COMMAND_NAME
            )
    
    def run(self):
        __is_installed, version = self.get_is_installed_version()
        if __is_installed:
            os.system(self.EXECUTABLE_PATH)
        else:
            print(f"The package is not installed, run `ouai {self.PACKAGE_COMMAND_NAME} install` to install it.")
        