def get_next_id(users):
    if not users:
        return 1
    return users[-1]["id"] + 1

def validate_name(name):
    return len(name.strip()) >= 2

def validate_age(age):
    try:
        age = int(age)
        return age > 0
    except:
        return False