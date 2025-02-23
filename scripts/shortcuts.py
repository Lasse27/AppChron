#######################################################################
# Script for creating file links on desktop, startmenu and autostart
########################################################################
import os
import win32com.client as com
import shutil


def main () -> None:
    init = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'appchron', '__init__.py')
    init_silent = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'appchron', '__init__.pyw')
    shutil.copyfile(init, init_silent)
    
    desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop', 'AppChron-Recording.lnk') 
    startmenu = os.path.join(os.environ['APPDATA'], 'Microsoft', 'Windows', 'Start Menu', 'Programs', 'AppChron-Recording.lnk')
    autostart = os.path.join(os.environ['APPDATA'], 'Microsoft', 'Windows', 'Start Menu', 'Programs', 'StartUp', 'AppChron-Recording.lnk')

    shell = com.Dispatch("WScript.Shell")
    shortcut = shell.CreateShortcut(desktop)
    shortcut.TargetPath = r"C:\Python313\pythonw.exe"
    shortcut.Arguments = init_silent + " --mode gui"
    shortcut.Save()
    
    shell = com.Dispatch("WScript.Shell")
    shortcut = shell.CreateShortcut(startmenu)
    shortcut.TargetPath = r"C:\Python313\pythonw.exe"
    shortcut.Arguments = init_silent + " --mode gui"
    shortcut.Save()

    shell = com.Dispatch("WScript.Shell")
    shortcut = shell.CreateShortcut(autostart)
    shortcut.TargetPath = r"C:\Python313\pythonw.exe"
    shortcut.Arguments = init_silent + " --mode recording"
    shortcut.Save()



if __name__ == "__main__":
    main()