import os
import random
import requests
import shutil

userprofile = os.getenv("%USERPROFILE%")
folder_id = ''.join(random.choices("abcdefghijklmnopqrstuwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789", k=8))
foldername = fr"{userprofile}\.{folder_id}"

os.makedirs(foldername)