import os
import shutil
import zipfile

from utils.dotter     import Dotter
from utils.downloader import download_url
from config.config    import TEMP_FOLDER, ROOT_FOLDER

class BaseInstaller:
    def __init__(self,
                PACKAGE_SERVICE         : str ,  # The name of the service, the folder name. 
                PACKAGE_ZIP_URL         : str ,  # The url of the zip file.
                PACKAGE_VERSION_URL     : str ,  # The url of the version file.
                PACKAGE_EXECUTABLE_NAME : str ,  # The name of the executable file, it will under ~/ouai/{PACKAGE_SERVICE}/{PACKAGE_EXECUTABLE_NAME}/{PACKAGE_EXECUTABLE_NAME}.exe
                PACKAGE_COMMAND_NAME    : str ,  # The command name of the package.
                ):
        self.PACKAGE_ZIP_URL         = PACKAGE_ZIP_URL
        self.PACKAGE_SERVICE         = PACKAGE_SERVICE
        self.PACKAGE_VERSION_URL     = PACKAGE_VERSION_URL
        self.PACKAGE_COMMAND_NAME    = PACKAGE_COMMAND_NAME
        self.PACKAGE_EXECUTABLE_NAME = PACKAGE_EXECUTABLE_NAME
        self.__SERVICE__             = PACKAGE_SERVICE

        self.FOLDER_PATH             = os.path.join(ROOT_FOLDER, self.__SERVICE__)
        self.EXECUTABLE_PATH         = os.path.join(self.FOLDER_PATH, f"{PACKAGE_EXECUTABLE_NAME}/{PACKAGE_EXECUTABLE_NAME}.exe")
        
    def show_version(self):
        """
        Show the version of the package.
        """
        have_version, version = self.get_is_installed_version()
        if have_version:
            print(f"{self.__SERVICE__} version is {version}")
        else:
            print(f"{self.__SERVICE__} is not installed, run `ouai {self.PACKAGE_COMMAND_NAME} install` to install it.")
    
    def update(self):
        """
        update the package.
        """
        os.makedirs(self.FOLDER_PATH, exist_ok=True)
        have_version, version = self.get_is_installed_version()
        lastest_versions      = self.get_lastest_versions()
        if have_version:
            if version == lastest_versions:
                print(f"The package is up-to-date. version is {version}")
            else:
                userinput = input("The package is installed, but not up-to-date, do you want to update it? [Y/n] ")
                if userinput.lower() == "y":
                    self.__install()
        else:
            userinput = input("The package is not installed, do you want to install it? [Y/n] ")
            if userinput.lower() == "y":
                self.__install()
                print(f"The package is installed in {self.FOLDER_PATH}")

    def check(self):
        """
        Check is the package installed or a newer version is available.
        """
        # check if the package is installed or not
        have_version, version = self.get_is_installed_version()
        lastest_versions      = self.get_lastest_versions()

        # check if the package is up-to-date or not
        if have_version:
            if version == lastest_versions:
                print(f"The package is up-to-date. version is {version}")
            else:
                print(f"The package is not up-to-date. version is {version}, lastest version is {lastest_versions}")
                print(f"Run `ouai {self.PACKAGE_COMMAND_NAME} update` to update it.")
        else:
            print("The package is not installed.")
            print(f"Run `ouai {self.PACKAGE_COMMAND_NAME} install` to install it.")

    def uninstall(self):
        """
        uninstall the package.
        """
        if os.path.exists(self.FOLDER_PATH):
            userinput = input("Are you sure to uninstall the package ? [Y/n] ")
            if userinput.lower() == "y":
                with Dotter("[*] Uninstalling the package"):
                    shutil.rmtree(self.FOLDER_PATH)
                print("The package is uninstalled.")
        else:
            print("The package is not installed.")

    def install(self):
        """
        Install the package.
        """
        os.makedirs(self.FOLDER_PATH, exist_ok=True)
        have_version, version = self.get_is_installed_version()
        lastest_versions = self.get_lastest_versions()
        if have_version:
            if version == lastest_versions:
                print("The package is already up-to-date.")
            else:
                userinput = input("The package is installed, but not up-to-date, do you want to update it? [Y/n] ")
                if userinput.lower() == "y":
                    self.__install()
                    print("The package is updated.")
                else:
                    print("The package is not updated.")
        else:
            userinput = input(f"Do you want to install `{self.PACKAGE_COMMAND_NAME}` ? [Y/n] ")
            if userinput.lower() == "y":
                self.__install()
            print(f"The package is installed in {self.FOLDER_PATH}")

    def run(self):
        pass

    def __install(self,):
        """
        The internal function to install the package.
        """
        zip_file = os.path.join(TEMP_FOLDER, f"{self.__SERVICE__}.zip")
        download_url(self.PACKAGE_ZIP_URL,zip_file)
        with zipfile.ZipFile(zip_file, 'r') as zip_ref:
            zip_ref.extractall(self.FOLDER_PATH)
        print()

    def get_lastest_versions(self):
        """
        get the lastest version of the package.
        """
        download_url(self.PACKAGE_VERSION_URL, os.path.join(TEMP_FOLDER, ".temp"), show_progress=False)
        with open(os.path.join(TEMP_FOLDER, ".temp"), "r", encoding='utf-8') as f:
            return f.read()
        
    def get_is_installed_version(self):
        """
        get the installed version of the package.
        """
        if os.path.exists(self.FOLDER_PATH):
            version_file = os.path.join(self.FOLDER_PATH, f"{self.PACKAGE_EXECUTABLE_NAME}/_internal/version.txt")
            if os.path.exists(version_file):
                return True, open(version_file, "r").read()
            else:
                return False, None
        return False, None