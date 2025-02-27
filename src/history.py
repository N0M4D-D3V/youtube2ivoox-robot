import os
import json

from setup import HISTORY_PATH

def load_history():
    print('[Y2I Robot] Loading history ...')
    if os.path.exists(HISTORY_PATH):
        with open(HISTORY_PATH, 'r') as file:
            return json.load(file)
    return []

def save_history(registro):
    print('[Y2I Robot] Saving history ...')
    with open(HISTORY_PATH, 'w') as file:
        json.dump(registro, file, indent=4)