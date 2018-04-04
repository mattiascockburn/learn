from argparse import ArgumentParser

def create_parser():
    parser = ArgumentParser(description='Do some HR stuff')
    parser.add_argument('inventory',
                        help='The inventory file to use')
    parser.add_argument('--export',
                        help='Export stuff',
                        action='store_true',
                       )
    return parser

def main():
    from hr import users, inventory

    args = create_parser().parse_args()
    if args.export:
        inventory.dump(args.inventory)
    else:
        user_list = inventory.load(args.inventory)
        users.sync(user_list)
