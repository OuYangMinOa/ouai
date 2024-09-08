# Handler.py
from .commit_msg.commit_msg_parser import action_executor as commit_msg_action_executor
from .gen_readme.gen_readme_parser import action_executor as gen_readme_action_executor

from config.config import __VERSION__, ROOT_FOLDER

import sys
import os

SERVICE_DICT = {
    "commit-msg" : "Use AI to analyse the commit log.",
    "gen-readme" : "Use AI to generate readme.",
}

OPTIONS_DICT = {
    "-v --version" : "Show the version of ouai package manager.",
    "-h --help" : "Show the help message.",
}

SERVICE_ACTION_CHOICES = {
    "commit-msg": {
        'install'        :'Install the package',
        'uninstall'      :'Uninstall the package',
        'update'         :'Update the package',
        'check'          :'Check is the package installed or a newer version is available',
        'git-hook'       :'Install the git hook',
        'remove-git-hook':'Remove the git hook',
        'version'        :'Show the version of the package',
        # 'run'            :'Run the git hook',
    },
    "gen-readme" : {
        'install'        :'Install the package',
        'uninstall'      :'Uninstall the package',
        'update'         :'Update the package',
        'check'          :'Check is the package installed or a newer version is available',
        'run'            :'Run the package',
        'version'        :'Show the version of the package',
    }
}

SERVICE_FUNCTION = {
    "commit-msg" : commit_msg_action_executor,
    "gen-readme" : gen_readme_action_executor,
}

def show_full_help():
    print("Usage: ouai [service] [action] [options]\n")
    print("Options:")
    for key in OPTIONS_DICT:
        print(f"    {key:<15}  {OPTIONS_DICT[key]}")

    print()
    print("Services:")
    for key in SERVICE_DICT:
        print(f"    {key:<15}  {SERVICE_DICT[key]}")
    print()
    show_services_action()

def show_services_action():
    print("Actions:")
    for each_action_key in SERVICE_ACTION_CHOICES:
        print(f"  - {each_action_key} :")
        for key in SERVICE_ACTION_CHOICES[each_action_key]:
            print(f"        {key:<15}  {SERVICE_ACTION_CHOICES[each_action_key][key]}")
        print()
        
def parser(main_file):
    args = sys.argv[1:]
    if (len(args)==0):
        show_full_help()
        return

    if ( args[0] in SERVICE_DICT ):
        if ( len(args) < 2 ):
            print(f"Usage: python main.py {args[0]} [action] [options]")
            print()
            print(f"Actions:")
            print(f"  - {args[0]}")
            for key in SERVICE_ACTION_CHOICES[args[0]]:
                print(f"        {key:<15}  {SERVICE_ACTION_CHOICES[args[0]][key]}")
            return
        
        if ( args[1] in SERVICE_ACTION_CHOICES[args[0]] or args[1].lower() in ["-v","--version"]):
            SERVICE_FUNCTION[args[0]](args[1].lower())

        else:
            print(f"Invalid action '{args[1]}'")
            print()
            show_services_action()

    
    elif ( "-h" in args or "--help" in args):
        show_full_help()
        return

    elif ("-V" in args or "-v" in args or "--version" in args):
        print(f"ouai {__VERSION__} from {os.path.abspath(main_file)}")
        return
    
    else:
        show_full_help()
        