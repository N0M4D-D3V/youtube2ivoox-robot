import os
import json

from setup import HISTORY_PATH

def load_history():
    print('[Y2I Robot] Loading history ...')
    if os.path.exists(HISTORY_PATH):
        with open(HISTORY_PATH, 'r') as file:
            return json.load(file)
    return []

def save_history(history):
    print('[Y2I Robot] Saving history ...')
    with open(HISTORY_PATH, 'w', encoding='utf-8') as file:
        json.dump(history, file, ensure_ascii=False, indent=4)