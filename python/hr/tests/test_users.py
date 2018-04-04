import pytest
import subprocess
import pwd
from hr import users

password='$6$EWQzIWVDcuG9O/Dw$4j8mfWiIzR7HcH72bzXwvmfCzH0I1bemBpLJXyKirXokLQwG.tap4kHF5Uc4NdVjaI2yL.VW9OreS8J7bNkd/0'

user_dict = {
  'name': 'kevin',
  'groups': ['wheel', 'dev'],
  'password': password,
}

group_list=','.join(user_dict['groups'])
add_command=['useradd', '-m', '-U', '-G', group_list,
             '-p', user_dict['password'], user_dict['name']]
update_command=['usermod', '-G', group_list, '-p', user_dict['password'],
                user_dict['name']]
remove_command=['userdel', '-r', user_dict['name']]

def test_users_add(mocker):
    """
    users.add should run successfully if all requirements are met
    """
    mocker.patch('subprocess.run')
    assert users.add(user_dict)
    subprocess.run.assert_called_with(add_command, check=True)

def test_users_useradd_fails(mocker):
    """
    if useradd returns != 0 users.add should return False
    """
    mocker.patch('subprocess.run', side_effect=subprocess.CalledProcessError(add_command,'command failed'))
    assert users.add(user_dict) == False

def test_users_remove(mocker):
    """
    users.remove should call userdel with the right arguments
    """
    mocker.patch('subprocess.run')
    users.remove(user_dict['name'])
    subprocess.run.assert_called_with(remove_command, check=True)

def test_users_exists(mocker):
    """
    users.exists should return True if a user is found and False if not
    """
    mocker.patch('pwd.getpwnam')
    assert users.exists(user_dict['name'])
    pwd.getpwnam.assert_called_with(user_dict['name'])

    mocker.patch('pwd.getpwnam', side_effect=KeyError())
    assert users.exists(user_dict) == False

def test_users_update(mocker):
    """
    users.update should call usermod with the correct parameters
    """
    mocker.patch('subprocess.run')
    assert users.update(user_dict)
    subprocess.run.assert_called_with(update_command, check=True)

def test_users_sync(mocker):
    """
    users.sync should take a list of user dicts and apply the desired state on
    the current system. A list of user objects may be passed in or a default is used.
    """
    user_list = [
        {
            'name': 'bob',
            'groups': ['wheel'],
            'password': password,
        },
        {
            'name': 'kevin',
            'groups': ['dev','wheel'],
            'password': password,
        },
    ]

    existing_users=['jose', 'kevin']

    mocker.patch('subprocess.run')
    users.sync(user_list, existing_users)
    subprocess.run.assert_has_calls([
        mocker.call(['useradd', '-m', '-U', '-G', 'wheel',
             '-p', password, 'bob'], check=True),
        mocker.call(['usermod', '-G', 'dev,wheel', '-p', password,
                'kevin'], check=True),
        mocker.call(['userdel', '-r', 'jose'], check=True)
    ])

