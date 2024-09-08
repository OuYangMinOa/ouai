import sys
import os

from utils.downloader import download_url
from .installer import CommitMsgInstaller

def action_executor(action):
    ins = CommitMsgInstaller()

    if ( action == "install" ):
        ins.install()
    elif ( action == "uninstall" ):
        ins.uninstall()
    elif ( action == "run" ):
        ins.run()
    elif ( action == "update" ):
        ins.update()
    elif ( action == "git-hook" ):
        ins.git_hook()
    elif ( action=="remove-git-hook" ):
        ins.remove_git_hook()
    elif ( action == "check" ):
        ins.check()

    elif ( action in ["-v","--version","version"] ):
        ins.show_version()