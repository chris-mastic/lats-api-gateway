from datetime import datetime
from mongoengine import Document, StringField, DateTimeField

class User(Document):
    token = StringField(required=True, unique=True)
    username = StringField(max_length=30)
    expirtation = DateTimeField(required=True)

def active_session(col, session_id: str) -> bool:

    user_session_data = {'token': session_id}

    try:
        user_profile = col.find_one(user_session_data)
        return True if user_profile.get("token") else False

    except:
        return False


def get_user_session_data(col, session_id: str) -> dict:
    user_session_data = {'token': session_id}
    print(f" user_session_datat is {user_session_data}")
    session_dict = {}
    try:
        user_profile = col.find_one(user_session_data)
        session_dict['token'] = user_profile.get("token")
        session_dict['token_expiration'] = user_profile.get("token_expiration")
        session_dict['username'] = user_profile.get("username")
        return (session_dict)

    except:
        return session_dict


def remove_user_session_from_mongodb(col, auth_token):
    user_session_data = {'token': auth_token}
    col.delete_one(user_session_data)


def insert_user_session_into_mongodb(col, auth_token, username, expiration):
    user_session_data = {'token': auth_token,
                         'username': username, 'date': datetime.now(),
                         'token_expiration': expiration}
    col.insert_one(user_session_data)

def insert_user_data_into_mongodb(col, req):
    print(f"insert_user_data_into_mongodb {req}")
    user_data = req
    col.insert_one(user_data)

def get_user_data(col, auth_token: str) -> dict:
    user_data = {'token': auth_token}
    session_dict = {}
    try:
        data = col.find_one(user_data)
        # delete _id, since it is not needed
        del data['_id']
        return (data)

    except:
        return create