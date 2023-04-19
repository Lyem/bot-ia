import shutil
import os


def remove_cache_folders():
    current_dir = os.getcwd()

    for root, dirs, files in os.walk(current_dir):
        for folder in dirs:
            if folder == "__pycache__" or folder == ".pytest_cache":
                folder_path = os.path.join(root, folder)
                print(f"Remove folder: {folder_path}")
                shutil.rmtree(folder_path)


if __name__ == "__main__":
    remove_cache_folders()
