# Firefox Redirector

This script is used to open firefox on the correct screen.

By default firefox will open new tabs in the most recent firefox instance,
even if they are on a different virtual desktop. 
This script will first check if there is an instance of firefox open on the current desktop, 
and if not add the "--new-window" argument to firefox.



Windows will only let you set a exe as a default browser, not a vbs or a py.
This is why the auto hotkey script exists, because it can easily be compiled as an exe.
The .vbs script is just so you can run the python script without it opening a terminal window.

The icon used if the firefox logo from 2005-2009, I wanted it to be distinguishable
from the current firefox logo, but still be firefox.
I also prefer it to the current logo.

## How to use
* Download this entire repository to its desired location, Decide on the final location of this repository before you proceed, because if you set an app as a default app, 
then move it, it leave ghosts, then you will need to rename Foxy.exe each time you move it.
* To compile yourself, delete Foxy.exe, right click "OpenFirefox.ahk" and select "Compile script (GUI)",
select the icon you want, then compile and rename the created .exe to Foxy.exe, or whatever name you want.
* Change the value of FIREFOX_LOCATION in OpenFirefox.py if firefox in installed
in a location different to "C:\\Program Files\\Mozilla Firefox".
* In windows settings, go to Apps > Default apps, in "Search apps" search for firefox, for each entry select "Choose an app on your PC" and select Foxy.exe.
* after compiling, Foxy.exe, OpenFirefox.VBSand and OpenFirefox.py are required to be kept in the same directory,
all other files can be removed.
* If you use Wox, the plugins "Browser Bookmarks", "URL" and "Web search" all work with Foxy.exe
To set this up, in Wox settings, select each of these plugins, next to "Please set your browser path:" press "Choose" and then find Foxy.exe. Make sure to set "Open bookmark in:" to "New tab" otherwise it will not work properly.

## Dependencies

To run the script you need python which can be downloaded from [Python.org](https://www.python.org/)  
The following Python libraries are required to run this script:
- `pyvda`
- `psutil`
- `win32process`

If you want to recompile Foxy.exe you will need autohotkey, which can be downloaded from [autohotkey.com](https://www.autohotkey.com/).




## Removing ghosts
If you decide to move Foxy.exe, you may need to do some steps to remove the ghosts left in the default apps menu, I used default programs editor, 
which can be downloaded at [defaultprogramseditor.com](http://defaultprogramseditor.com).