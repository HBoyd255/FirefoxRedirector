import sys
import os
from pyvda import get_apps_by_z_order
import psutil
import win32process, win32gui

print(sys.argv)

def appExists(TargetApp):

    WindwosOpenOnThisDesktop = get_apps_by_z_order()
    for X in range(len(WindwosOpenOnThisDesktop)):
        currentWindowHWND = WindwosOpenOnThisDesktop[X].hwnd
        _,pid = win32process.GetWindowThreadProcessId(currentWindowHWND)
        process = psutil.Process(pid)
        process_name = process.name()
        if TargetApp in process_name:
            return 1
    return 0

FFLocation = "C:\Program Files\Mozilla Firefox"
os.chdir(FFLocation)

arguments = ' '.join(sys.argv[1:])

if(appExists("firefox") == 0):
    os.system("firefox.exe " + "--new-window " + "\"" + arguments + "\"")
else:
    os.system("firefox.exe " + "\""+ arguments + "\"")





