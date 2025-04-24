import subprocess
import socket
import uuid
import os
import platform

hostname = socket.gethostname()
user = os.getlogin()

if not os.path.exists(fr"{foldername}\System"):
   os.makedirs(fr"{foldername}\system")

try:
   os_name = platform.system()
except:
   os_name = "None : error"
try:
   os_version = platform.version()
except:
   os_version = "None : error"
try:
   os_release = platform.release()
except:
   os_release = "None : error"
try:
   os_architecture = platform.architecture()[0]
except:
   os_architecture = "None : error"
try:
   pc_ip = socket.gethostbyname(hostname)
except Exception:
   pc_ip = "None : Error"
try:
   pc_gpu = subprocess.run("wmic path win32_VideoController get name", capture_output=True, shell=True).stdout.decode(errors='ignore').splitlines()[2].strip()
except:
   pc_gpu = "None : Error"
try:
   pc_cpu = subprocess.run(["wmic", "cpu", "get", "Name"], capture_output=True, text=True).stdout.strip().split('\n')[2]
except:
   pc_cpu = "None : Error"
try:
   pc_ram = str(round(int(subprocess.run('wmic computersystem get totalphysicalmemory', capture_output=True, shell=True).stdout.decode(errors='ignore').strip().split()[1]) / (1024 ** 3)))
except:
   pc_ram = "None : Error"
try:
   mac_address = ':'.join(['{:02x}'.format((uuid.getnode() >> elements) & 0xff) for elements in range(0,2*6,2)][::-1])
except:
   mac_address = "None : Error"
try:
   pc_uuid = subprocess.check_output(r'C:\\Windows\\System32\\wbem\\WMIC.exe csproduct get uuid', shell=True, stdin=subprocess.PIPE, stderr=subprocess.PIPE).decode('utf-8').split('\n')[1].strip()
except:
   pc_uuid = "None : Error"

with open(f"{foldername}/System/system.txt", "w", encoding='utf-8') as file:
   file.write(f"""<==============================[ SYSTEM INFOS ]==============================>

[ SOFTWARE ]

OS : {os_name}
RELEASE : {os_release}
ARCHITECTURE : {os_architecture}
VERSION : {os_version}

IP ADRESS : {pc_ip}
MAC ADRESS : {mac_address}
UUID : {pc_uuid}

[ HARDWARE ]

GPU : {pc_gpu}
CPU : {pc_cpu}
RAM : {pc_ram} Gb

""")