import os
import json

from setup import HISTORY_PATH
from src.logger import log

def load_history():
    log('Loading history...')
    if os.path.exists(HISTORY_PATH):
        with open(HISTORY_PATH, 'r') as file:
            return json.load(file)
    return []

def save_history(history):
    log('Saving history...')
    with open(HISTORY_PATH, 'w', encoding='utf-8') as file:
        json.dump(history, file, ensure_ascii=False, indent=4)