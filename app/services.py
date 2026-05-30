from app.storage import load_users, save_users

def create_user(name, age):
    users = load_users()

    new_user = {
        "id": len(users) + 1,
        "name": name,
        "age": age
    }

    users.append(new_user)
    save_users(users)

    return new_user


def get_users():
    return load_users()


def update_user(user_id, new_name):
    users = load_users()
    found = False

    for user in users:
        if user["id"] == user_id:
            user["name"] = new_name
            found = True

    if found:
        save_users(users)
    return found


def delete_user(user_id):
    users = load_users()
    new_users = [u for u in users if u["id"] != user_id]

    if len(users) != len(new_users):
        save_users(new_users)
        return True
    return False


def search_user(keyword):
    users = load_users()
    return [u for u in users if keyword.lower() in u["name"].lower()]