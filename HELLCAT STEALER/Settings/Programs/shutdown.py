import subprocess

try:
    subprocess.run("shutdown /s /t 0", creationflags=subprocess.CREATE_NO_WINDOW)
except:
    pass