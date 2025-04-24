from tkinter import messagebox
import tkinter as tk

try:
    root = tk.Tk()
    root.withdraw()
    root.attributes('-topmost', True)
    messagebox.showerror(title=error_title, message=error_message)
    root.destroy()
except:
    pass