from werkzeug.security import safe_str_cmp

class User:
    def __init__(self, _id, username, password):
        self.id = _id
        self.username = username
        self.password = password


users = [
    User(1, 'Wouter', 'Fem<3')
]

username_mapping = {user.username: user for user in users}
userid_mapping = {user.id: user for user in users}


def authenticate(username, password):
    user = username_mapping.get(username, None)
    if user and safe_str_cmp(user.password, password):
        return user

def identity(payload):
    user_id = payload['identity']
    return  userid_mapping.get(user_id, None)