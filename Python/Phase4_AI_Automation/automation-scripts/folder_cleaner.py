import os, shutil

def organize_folder(folder):
    extensions = {
        "Images": [".jpg", ".png", ".jpeg", ".gif"],
        "Videos": [".mp4", ".mkv", ".mov"],
        "Documents": [".pdf", ".docx", ".txt"],
        "Archives": [".zip", ".rar"],
    }

    for file in os.listdir(folder):
        file_path = os.path.join(folder, file)
        if os.path.isfile(file_path):
            moved = False
            for folder_name, exts in extensions.items():
                if file.lower().endswith(tuple(exts)):
                    target_dir = os.path.join(folder, folder_name)
                    os.makedirs(target_dir, exist_ok=True)
                    shutil.move(file_path, os.path.join(target_dir, file))
                    moved = True
                    break
            if not moved:
                print(f"Skipped: {file}")

if __name__ == "__main__":
    folder_path = input("Enter folder path to clean: ")
    organize_folder(folder_path)
    print("✅ Folder organized successfully!")
