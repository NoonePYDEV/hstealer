import pyautogui

try:
   screen_screenshot = pyautogui.screenshot()
   screen_screenshot.save(f"{foldername}/screenshot.png")
except:
   pass