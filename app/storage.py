import json

FILE_PATH = "data/users.json"

def load_users():
    try:
        with open(FILE_PATH, "r") as file:
            return json.load(file)
    except:
        return []

def save_users(users):
    with open(FILE_PATH, "w") as file:
        json.dump(users, file, indent=4)