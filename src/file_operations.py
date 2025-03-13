import os
import glob

from setup import COOKIES_PATH
from src.logger import log

import pickle

def exists(path: str) -> bool:
    return  os.path.isfile(path)

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

def save_cookies(driver):
    log('Saving cookies ...')
    with open(COOKIES_PATH, "wb") as file:
        pickle.dump(driver.get_cookies(), file)

def load_cookies(driver):
    log('Loading cookies ...')
    with open(COOKIES_PATH, "rb") as file:
        cookies = pickle.load(file)
        for cookie in cookies:
            driver.add_cookie(cookie)
    
    return driver
