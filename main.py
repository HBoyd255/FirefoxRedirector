import sys
import os

# TODO Fix the desktop detection function.
# Without the function, the script is just a shell, that executes firefox with 
# the arguments passed to it, and provides no functionality to the user.

# from pyvda import get_apps_by_z_order
# import win32process

import psutil

FIREFOX_LOCATION = "C:\\Program Files\\Mozilla Firefox"

# As pyvda vision 0.3.2 does not currently work with the most recent windows
# update, bypass its function.
BYPASS_PYVDA = True

# This script takes arguments and passes them to firefox,
# if an instance of firefox does not exist on the current virtual desktop, it opens a new window.


# # Tests if an app with a specific name is open in this virtual desktop.
def app_exists_on_current_desktop(target_application_name):
    # Gets a list of the open windows on the current virtual desktop.
    open_windows = get_apps_by_z_order()

    # Iterates through each window.
    for window in open_windows:
        # Get the handle of the window.
        window_handle = window.hwnd

        # Get the process id of the window handle.
        process_id = win32process.GetWindowThreadProcessId(window_handle)[1]

        # Gets the process associated with the process id.
        process = psutil.Process(process_id)

        # Gets the name of the process.
        process_name = process.name()

        # If the name was found, return 1.
        if target_application_name in process_name:
            return 1
    # IF the name was not found, return 0.
    return 0


def main():
    # Change the current directory to the location of firefox.
    os.chdir(FIREFOX_LOCATION)

    # Combine the arguments received  by this script into one string.
    arguments = " ".join(sys.argv[1:])

    # If the bypass flag is enabled, directly call firefox to open in a new tab.
    if BYPASS_PYVDA:
        os.system(f'firefox.exe "{arguments}"')
        return

    # If there is no instance of firefox on this virtual desktop, open firefox as a new window.
    if app_exists_on_current_desktop("firefox") == 0:
        os.system(f'firefox.exe --new-window "{arguments}"')
    # If firefox is already open on this desktop, open as a new tab.
    else:
        os.system(f'firefox.exe "{arguments}"')


if __name__ == "__main__":
    main()
