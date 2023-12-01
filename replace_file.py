import shutil
import os

def move_and_replace_file(source_file, target_directory):
    # Ensure the target directory exists
    os.makedirs(target_directory, exist_ok=True)

    # Construct the full path for the target file
    target_file = os.path.join(target_directory, os.path.basename(source_file))

    # Move the file
    shutil.move(source_file, target_file)
    print(f"File {source_file} has been moved to {target_file}")

# Full path to the file to be moved
source_file = "/home/mastercion/kodi_tv/grabber/kodi_tv_test.m3u"

# Target directory
target_directory = "/home/mastercion/kodi_tv/kodi_tv_custom/"

# Move and replace the file
move_and_replace_file(source_file, target_directory)

