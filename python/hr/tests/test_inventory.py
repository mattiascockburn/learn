import pytest
import tempfile
from hr import inventory

test_json = b'''[
  {
    "name": "kevin",
    "groups": ["wheel", "dev"],
    "password": "$6$HXdlMJqcV8LZ1DIF$LCXVxmaI/ySqNtLI6b64LszjM0V5AfD.ABaUcf4j9aJWse2t3Jr2AoB1zZxUfCr8SOG0XiMODVj2ajcQbZ4H4/"
  },
  {
    "name": "lisa",
    "groups": ["wheel"],
    "password": "$6$HXdlMJqcV8LZ1DIF$LCXVxmaI/ySqNtLI6b64LszjM0V5AfD.ABaUcf4j9aJWse2t3Jr2AoB1zZxUfCr8SOG0XiMODVj2ajcQbZ4H4/"
  },
  {
    "name": "jim",
    "groups": [],
    "password": "$6$HXdlMJqcV8LZ1DIF$LCXVxmaI/ySqNtLI6b64LszjM0V5AfD.ABaUcf4j9aJWse2t3Jr2AoB1zZxUfCr8SOG0XiMODVj2ajcQbZ4H4/"
  }
]'''
test_struct = [
    {'groups': ['wheel', 'dev'],
     'name': 'kevin',
     'password': '$6$HXdlMJqcV8LZ1DIF$LCXVxmaI/ySqNtLI6b64LszjM0V5AfD.ABaUcf4j9aJWse2t3Jr2AoB1zZxUfCr8SOG0XiMODVj2ajcQbZ4H4/'},
    {'groups': ['wheel'],
     'name': 'lisa',
     'password': '$6$HXdlMJqcV8LZ1DIF$LCXVxmaI/ySqNtLI6b64LszjM0V5AfD.ABaUcf4j9aJWse2t3Jr2AoB1zZxUfCr8SOG0XiMODVj2ajcQbZ4H4/'},
    {'groups': [],
     'name': 'jim',
     'password': '$6$HXdlMJqcV8LZ1DIF$LCXVxmaI/ySqNtLI6b64LszjM0V5AfD.ABaUcf4j9aJWse2t3Jr2AoB1zZxUfCr8SOG0XiMODVj2ajcQbZ4H4/'}
]

invalid_json = b'''[
  {
    "name": foo,
  },
  {
    "name: blah
  }
]'''

test_users=['kevin','lisa','jim']

def test_inventory_creation(mocker):
    pass

def test_inventory_load_fails_with_unknown_path(mocker):
    """
    inventory.load needs to fail when the file could not be opened
    """
    mocker.patch('builtins.open', side_effect=OSError('no such file'))
    with pytest.raises(SystemExit):
        inventory.load('/some/file')

def test_inventory_load(mocker):
    """
    Given a valid path to valid json,
    inventory.load should return a data structure
    """
    t = tempfile.NamedTemporaryFile(delete=False)
    t.write(test_json)
    t.seek(0)

    j = inventory.load(t.name)
    for user in j:
        assert user['name'] in test_users
        #assert user['password'] == test_struct[user['name']]['password']

def test_inventory_load_with_invalid_json():
    """
    inventory.load should exit with an error if the user
    tries to load invalid JSON
    """
    t = tempfile.NamedTemporaryFile(delete=False)
    t.write(invalid_json)
    t.seek(0)
    with pytest.raises(SystemExit):
        inventory.load(t.name)

def test_inventory_dump(mocker):
    """
    inventory.dump should write a valid json file to disk
    """
    t = tempfile.NamedTemporaryFile(delete=False)
    t.close()
    mocker.patch('spwd.getspnam', return_value=mocker.Mock(sp_pwd='password'))
    mocker.patch('grp.getgrall', return_value=[
        mocker.Mock(gr_name='admin', gr_mem=['kevin']),
        mocker.Mock(gr_name='other', gr_mem=[]),
        mocker.Mock(gr_name='wheel', gr_mem=['kevin','bob']),
    ]
    )
    inventory.dump(t.name,['kevin','bob'])
    with open(t.name) as f:
        assert f.read() == """[{"name": "kevin", "groups": ["admin", "wheel"], "password": "password"}, {"name": "bob", "groups": ["wheel"], "password": "password"}]"""
