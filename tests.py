import os
import glob
import shutil
import sys

def find_matching_directories(base_path, target_pattern):
    matching_directories = []
    for dir_path, dir_names, _file_names in os.walk(base_path):
        for dir_name in dir_names:
            full_path = os.path.join(dir_path, dir_name)
            if glob.fnmatch.fnmatch(full_path, target_pattern):
                matching_directories.append(full_path)
    return matching_directories


if __name__ == "__main__":
    base_path = input("Enter the base folder path: ")
    target_pattern = input("Enter the target glob pattern (**b. Watch List Notes\\2023**): ")
    source_file_path = input("Enter the source file path: ")

    matching_directories = find_matching_directories(base_path, target_pattern)

    print("Matching directories:")
    for directory in matching_directories:
        print(f"{source_file_path} copy -> {directory}")


    confirmation = input("Confirm (y/n): ")
    if confirmation.lower().replace(" ", "") != "y":
        print("Aborted.")
        sys.exit()


    for directory in matching_directories:
        destination_file_path = os.path.join(directory, os.path.basename(source_file_path))
        shutil.copy2(source_file_path, destination_file_path)
        print(f"Copied {source_file_path} to {destination_file_path}.")
