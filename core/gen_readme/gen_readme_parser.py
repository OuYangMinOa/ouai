from .installer import ReadMeGeneratorInstaller


def action_executor(action):
    ins = ReadMeGeneratorInstaller()

    if ( action == "install" ):
        ins.install()
    elif ( action == "uninstall" ):
        ins.uninstall()
    elif ( action == "run" ):
        ins.run()
    elif ( action == "update" ):
        ins.update()
    elif ( action in ["-v","--version","version"] ):
        ins.show_version()