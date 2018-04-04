import subprocess
import pwd
from hr import helpers

def add(user):
    try:
        print(f"Creating user {user['name']}")
        subprocess.run(['useradd', '-m', '-U', '-G', ','.join(user['groups']),
                        '-p', user['password'], user['name']], check=True)
        return True
    except subprocess.CalledProcessError:
        print(f'Failed to create user:')
        return False

def remove(user):
    print(f'Removing user {user}')
    subprocess.run(['userdel', '-r', user], check=True)

def exists(user):
    try:
        pwd.getpwnam(user)
        return True
    except KeyError:
        return False

def update(user):
    try:
        print(f"Updating user {user['name']}")
        subprocess.run(['usermod', '-G', ','.join(user['groups']),
                        '-p', user['password'], user['name']], check=True)
        return True
    except subprocess.CalledProcessError:
        print(f'Failed to modify user')
        return False


def sync(users, existing_users=None):
    user_names = [user['name'] for user in users]
    if not existing_users:
        existing_users = helpers.get_users()
    for user in users:
        if user['name'] in existing_users:
            update(user)
        if user['name'] not in existing_users:
            add(user)
    for user in existing_users:
        if user not in user_names:
            remove(user)

