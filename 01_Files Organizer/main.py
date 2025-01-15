import os
import shutil

directory = os.path.join(os.path.expanduser("~"), "Downloads")

extensions = {
    ".jpg": "Images/JPG",
    ".jpeg": "Images/JPG",
    ".png": "Images/PNG",
    ".svg": "Images/SVG",
    ".gif": "Images/GIF",
    ".avif": "Images/AVIF",
    ".webp": "Images/WEBP",
    ".ico": "Images/ICO",
    ".mp4": "Videos",
    ".mov": "Videos",
    ".mkv": "Videos/Movies",
    ".doc": "Documents/DOC",
    ".docx": "Documents/DOC",
    ".pdf": "Documents/PDF",
    ".txt": "Documents/TXT",
    ".pptx": "Documents/PPTX",
    ".mp3": "Music",
    ".wav": "Music",
    ".csv": "Data/CSV",
    ".json": "Data/JSON",
    ".ipynb": "Code/Python",
    ".html": "Code/HTML",
    ".zip": "Compressed Files"
}


for filename in os.listdir(directory):
    file_path = os.path.join(directory, filename)

    if os.path.isfile(file_path):
        extension = os.path.splitext(filename)[1].lower()

        if extension in extensions:
            folder_name = extensions[extension]

            folder_path = os.path.join(directory, folder_name)
            os.makedirs(folder_path, exist_ok=True)

            destination_path = os.path.join(folder_path, filename)
            shutil.move(file_path, destination_path)

            print(f"Moved {filename} to {folder_name} folder.")
        else:
            print(f"Skipped {filename}. Unknown file extension")
    else:
        print(f"Skipped {filename}. It is a directory.")

print("File organization completed.")
