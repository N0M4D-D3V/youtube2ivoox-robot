import os
import glob

from src.logger import log

# Usage
# path = "/path/to/directory"
# count = remove_mp3_files(path)
# print(f"Removed {count} MP3 files")
def remove_files(directory, regex):
    log(f'Removig {regex} files from {directory}...')
    mp3_files = glob.glob(os.path.join(directory, regex))
    for file in mp3_files:
        os.remove(file)
        
    return len(mp3_files)