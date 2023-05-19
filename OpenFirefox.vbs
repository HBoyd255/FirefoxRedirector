Set WshShell = CreateObject("WScript.Shell")
Set objFSO = CreateObject("Scripting.FileSystemObject")

' Create an array to store the arguments.
Dim argumentsArray
ReDim argumentsArray(WScript.Arguments.Count-1)
For i = 0 To WScript.Arguments.Count-1
    ' Populate the array with the arguments given to this script.
    argumentsArray(i) = WScript.Arguments(i)
Next

' Join the arguments into one string.
argumentsString =  Join(argumentsArray)

' Get the full path of this scrips.
scriptPath = objFSO.GetParentFolderName(WScript.ScriptFullName)

' Create the command to exicute by combing the path of this script, "OpenFirefox.py" and the arguments given. Chr(34) is the character of "
command = "python " & Chr(34) & scriptPath & "\OpenFirefox.py" & Chr(34) & " " & argumentsString

' Run the command and wait for it to complete
WshShell.Run command, 0, True

' Clean up and release resources
Set WshShell = Nothing