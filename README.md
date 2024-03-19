# Firefox Redirector

WARNING - Script is currently broken until pyvda updates.

This script is used to open firefox on the correct screen.

By default firefox will open new tabs in the most recent firefox instance, even
if they are on a different virtual desktop. This script will first check if
there is an instance of firefox open on the current desktop, and if not add the
"--new-window" argument to firefox.

Windows will only allow you to test an executable file as the default browser,
so this script is compiled into an exe using pyinstaller.

The icon used if the firefox logo from 2005-2009, I wanted it to be
distinguishable from the current firefox logo, but still be firefox. I also
prefer it to the current logo.

## How to build and use

- Install the dependencies
- Run `build.bat`
- Set the default browser to Foxy.exe
- If you use Wox, the plugins "Browser Bookmarks", "URL" and "Web search" all
  work with Foxy.exe To set this up, in Wox settings, select each of these
  plugins, next to "Please set your browser path:" press "Choose" and then find
  Foxy.exe. Make sure to set "Open bookmark in:" to "New tab" otherwise it will
  not work properly.

## Dependencies

To build the script you need [python](https://www.python.org/) and the following
packages installed via pip:

- `pyvda`
- `psutil`
- `win32process`
- `pyinstaller`

## Removing ghosts

If you decide to move Foxy.exe, you may need to do some steps to remove the
ghosts left in the default apps menu, I used default programs editor, which can
be downloaded at [defaultprogramseditor.com](http://defaultprogramseditor.com).
