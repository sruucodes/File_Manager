import os
import shutil
from datetime import datetime

def list_files(directory):
    try:
        files = os.listdir(directory)
        return files
    except FileNotFoundError:
        print("Directory not found.")
        return []

def sort_files(files, directory, criterion):
    if criterion == 'name':
        sorted_files = sorted(files)
    elif criterion == 'date':
        sorted_files = sorted(files, key=lambda x: os.path.getmtime(os.path.join(directory, x)))
    elif criterion == 'type':
        sorted_files = sorted(files, key=lambda x: os.path.splitext(x)[1])
    elif criterion == 'size':
        sorted_files = sorted(files, key=lambda x: os.path.getsize(os.path.join(directory, x)))
    else:
        print("Unknown sorting criterion.")
        return []

    return sorted_files

def rename_files(files, directory, pattern):
    for i, file in enumerate(files):
        file_extension = os.path.splitext(file)[1]  # Get the file extension
        new_name = pattern.replace("###", str(i).zfill(3)) + file_extension
        old_path = os.path.join(directory, file)
        new_path = os.path.join(directory, new_name)
        os.rename(old_path, new_path)
        print(f"Renamed {file} to {new_name}")

def organize_files_by_type(files, directory):
    for file in files:
        file_type = os.path.splitext(file)[1][1:]  # Get file extension without dot
        if file_type:  # Only create a folder if the file has an extension
            new_dir = os.path.join(directory, file_type)
            os.makedirs(new_dir, exist_ok=True)
            shutil.move(os.path.join(directory, file), os.path.join(new_dir, file))
            print(f"Moved {file} to {new_dir}")
