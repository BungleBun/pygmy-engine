import json
import os

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def load_json(path):
    with open(path, 'r') as f:
        return json.load(f)