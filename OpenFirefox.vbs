Set WshShell = CreateObject("WScript.Shell")
Set objFSO = CreateObject("Scripting.FileSystemObject")


ReDim arr(WScript.Arguments.Count-1)
For i = 0 To WScript.Arguments.Count-1
  arr(i) = WScript.Arguments(i)
Next

Arguments =  Join(arr)

strScriptDir = objFSO.GetParentFolderName(WScript.ScriptFullName)

cmds=WshShell.RUN("python3 "+strScriptDir+"\OpenFirefox.py " + Arguments,0, True)

Set WshShell = Nothing