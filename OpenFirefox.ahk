#NoEnv  ; Recommended for performance and compatibility with future AutoHotkey releases.
#Warn  ; Enable warnings to assist with detecting common errors.
SendMode Input  ; Recommended for new scripts due to its superior speed and reliability.
SetWorkingDir %A_ScriptDir%  ; Ensures a consistent starting directory.

;This script just exists so i can create create an EXE file that just calls a VBS script that calls a python script.

run "%A_ScriptDir%\OpenFirefox.vbs" %1%