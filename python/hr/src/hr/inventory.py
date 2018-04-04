"""
Inventory related functions
"""
import json
import sys
import grp
import spwd
import pwd
from hr import helpers

def load(inventory):
    try:
        with open(inventory) as f:
            return json.load(f)
    except OSError as e:
        print(f'Error opening file: {e}')
        sys.exit(1)
    except json.decoder.JSONDecodeError as e:
        print(f'Failed to load JSON: {e}')
        sys.exit(1)

def dump(fname, user_list=None):
    if not user_list:
        user_list=helpers.get_users()
    users = []
    group_list = grp.getgrall()
    for user in user_list:
        password = spwd.getspnam(user).sp_pwd
        users.append(
            {
                'name': user,
                'groups': _groups_for_user(user),
                'password': password,
            }
        )
    with open(fname,'w') as f:
        json.dump(users,f)

def _groups_for_user(user):
    return [g.gr_name for g in grp.getgrall() if user in g.gr_mem]
