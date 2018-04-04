import pytest
from hr import cli

inv = '/tmp/myinventory.json'

@pytest.fixture
def parser():
    return cli.create_parser()

def test_parser_without_arguments(parser):
    """
    Parser should fail with no arguments given
    """
    with pytest.raises(SystemExit):
        parser.parse_args()

def test_parser_with_inventory(parser):
    """
    Parser should succeed with an inventory
    """
    args = parser.parse_args([inv])
    assert args.inventory == inv


def test_parser_with_export_flag(parser):
    """
    export flag should be True if the flag is given
    and False by default
    """
    args = parser.parse_args([inv])
    assert args.export == False

    args = parser.parse_args([inv,'--export'])
    assert args.export == True

