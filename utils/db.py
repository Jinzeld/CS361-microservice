users = []

def add_user(user):
    users.append(user)

def find_user(username):
    return next((user for user in users if user['username'] == username), None)
