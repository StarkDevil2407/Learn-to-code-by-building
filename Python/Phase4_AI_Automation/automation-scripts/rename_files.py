import os

def rename_files(folder_path, prefix="file"):
    files = os.listdir(folder_path)
    for count, filename in enumerate(files):
        file_extension = os.path.splitext(filename)[1]
        new_name = f"{prefix}_{count + 1}{file_extension}"
        src = os.path.join(folder_path, filename)
        dst = os.path.join(folder_path, new_name)
        os.rename(src, dst)
        print(f"Renamed: {filename} → {new_name}")

if __name__ == "__main__":
    folder = input("Enter folder path: ").strip()
    rename_files(folder)
