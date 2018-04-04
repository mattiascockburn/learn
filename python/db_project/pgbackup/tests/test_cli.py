import pytest
from pgbackup import cli

url = 'postgres://bob:password@example.com:5432/db_one'

@pytest.fixture
def parser():
    return cli.create_parser()

def test_parser_fails_without_driver(parser):
    """
    Parser should fail if we don't supply a driver
    """
    with pytest.raises(SystemExit):
        args = parser.parse_args([url])

def test_parser_with_missing_destination(parser):
    """
    Parser should fail if we forget to supply a destination
    """
    with pytest.raises(SystemExit):
        args = parser.parse_args([url, '--driver', 'local'])

def test_parser_with_unknown_driver(parser):
    """
    Parser should fail if we supply an unknown driver
    """
    with pytest.raises(SystemExit):
        args = parser.parse_args([url, '--driver', 'foobar','random_dest'])

def test_parser_with_known_drivers(parser):
    """
    Parser should not exit if we supply known drivers
    """
    for driver in ['local', 's3']:
        assert parser.parse_args([url, '--driver', driver, 'foobar_dest'])



def test_parser_with_driver_and_destination(parser):
    """
    Parser should not raise an error when all parameters are supplied
    on the command line
    """
    args = parser.parse_args([url, '--driver', 'local', '/some/random/path'])
    assert args.url == url
    assert args.driver == 'local'
    assert args.destination == '/some/random/path'

