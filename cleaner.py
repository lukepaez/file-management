import os
import shutil

def create_subfolder(folder_path: str, subfolder: str):
    subfolder_path = os.path.join(folder_path, subfolder)

    if not os.path.exists(subfolder_path):
        os.makedirs(subfolder_path)
    
    return subfolder_path

def clean_folder(folder_path: str):
    try:
        print(f"Folder Path: {folder_path}")
        print(f"Starting cleanup...\n")

        if not os.path.isdir(folder_path):
            raise Exception("Invalid folder path!")
        
        for file in os.listdir(folder_path):
            if not os.path.isfile(os.path.join(folder_path, file)):
                print(f"Skipped: '{os.path.join(folder_path, file)}' not a file!")
                continue

            file_extension = file.split(".")[-1].lower()

            if file_extension:
                subfolder = f"{file_extension.upper()}_Files"
                subfolder_path = create_subfolder(folder_path, subfolder)
                file_to_be_moved_path = os.path.join(folder_path, file)
                file_moved_to_path = os.path.join(subfolder_path, file)

                if not os.path.exists(file_moved_to_path):
                    shutil.move(file_to_be_moved_path, subfolder_path)
                    print(f"\nMoved: {file} -> {subfolder_path}/")
                else:
                    print(f"Skipped: {file} already exists in {subfolder_path}/")    
    except Exception as e:
        print(e)
