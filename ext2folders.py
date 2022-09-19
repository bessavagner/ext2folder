import os
import shutil
import pathlib

folder = {
    "jpg": "images",
    "png": "images",
    "ico": "images",
    "gif": "images",
    "svg": "images",
    "sql": "sql",
    "deb": "programs",
    "exe": "programs",
    "msi": "programs",
    "pdf": "texts",
    "xlsx": "excel",
    "csv": "excel",
    "rar": "archive",
    "zip": "archive",
    "gz": "archive",
    "tar": "archive",
    "docx": "texts",
    "torrent": "torrent",
    "txt": "texts",
    "ipynb": "python",
    "py": "python",
    "pptx": "powerpoint",
    "ppt": "powerpoint",
    "mp3": "audio",
    "wav": "audio",
    "mp4": "video",
    "m3u8": "video",
    "webm": "video",
    "ts": "video",
    "json": "json",
    "css": "web",
    "js": "web",
    "html": "web",
    "apk": "apk",
    "sqlite3": "sqlite3",
}

# Target folder path, relative to 'home' directory
target_folder = "Downloads"

# You can run this from any location, except target folder
LOCATION = str(pathlib.Path.home() / target_folder)
files = []
for (dirpath, dirnames, filenames) in os.walk(LOCATION):
    files.extend(filenames)
    break  # Walk throught only LOCATION files, not subfiles
for file in files:
    ext = file.split(".")[-1]  # extracts extensions
    ext_data = folder.keys()
    # check if it has a category. If not, receives 'no_category'
    folder_name = folder[ext] if ext in ext_data else "no_category"
    path = os.path.join(LOCATION, folder_name)
    if not os.path.exists(path):  # creates folder if it doesn't exist
        os.mkdir(path)
    shutil.move(os.path.join(LOCATION,file), path)  # the move
