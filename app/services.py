from app.storage import read_users, write_users
from app.utils import get_next_id

def create_user(name, age):
    users = read_users()
    user_id = get_next_id(users)

    user = {
        "id": user_id,
        "name": name,
        "age": age
    }

    users.append(user)
    write_users(users)
    return user

def get_all_users():
    return read_users()

def update_user(user_id, name, age):
    users = read_users()

    for u in users:
        if u["id"] == user_id:
            u["name"] = name
            u["age"] = age
            write_users(users)
            return u
    return None

def delete_user(user_id):
    users = read_users()
    new_users = [u for u in users if u["id"] != user_id]

    if len(users) == len(new_users):
        return False

    write_users(new_users)
    return True

def search_user(name):
    users = read_users()
    return [u for u in users if name.lower() in u["name"].lower()]