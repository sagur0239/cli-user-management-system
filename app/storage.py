import json
import os

FILE_PATH = "data/users.json"

def read_users():
    if not os.path.exists(FILE_PATH):
        return []
    try:
        with open(FILE_PATH, "r") as f:
            return json.load(f)
    except:
        return []

def write_users(users):
    with open(FILE_PATH, "w") as f:
        json.dump(users, f, indent=4)