import os
import shutil

path = input("Enter folder path: ")

file_types = {
    "Images": [".jpg", ".png", ".jpeg"],
    "Documents": [".pdf", ".txt", ".docx"],
    "Music": [".mp3", ".wav"]
}

for file in os.listdir(path):
    file_path = os.path.join(path, file)

    if os.path.isfile(file_path):
        ext = os.path.splitext(file)[1].lower()

        for folder, extensions in file_types.items():
            if ext in extensions:
                folder_path = os.path.join(path, folder)
                os.makedirs(folder_path, exist_ok=True)

                dest = os.path.join(folder_path, file)
                if os.path.exists(dest):
                    base, ext = os.path.splitext(file)
                    dest = os.path.join(folder_path, base + "_1" + ext)

                shutil.move(file_path, dest)
