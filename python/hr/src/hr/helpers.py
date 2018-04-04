import pwd

def get_users():
    return [user.pw_name for user in pwd.getpwall()
            if user.pw_uid >=1000 and 'home' in user.pw_dir]
