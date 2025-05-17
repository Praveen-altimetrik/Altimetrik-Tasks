# module is python .py file
# this module contains the User functions, class and its methods and variables


user_info = {}

def get_all_user_info():

    return user_info

def add_user_info(user_id, user_name, user_email):

    user_info[user_id] = {
        'user_name': user_name,
        'user_email': user_email
    }





