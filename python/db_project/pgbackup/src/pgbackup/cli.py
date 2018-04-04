"""
CLI part of pgbackup
"""
from argparse import Action, ArgumentParser

known_drivers = ['local', 's3']

class DriverAction(Action):
    def __call__(self, parser, namespace, values, option_string=None):
        driver, destination = values
        namespace.driver = driver.lower()
        if driver.lower() not in known_drivers:
            parser.error('Unknown driver. Known drivers are local and s3')
        namespace.destination = destination

def create_parser():
    parser = ArgumentParser()
    parser.add_argument('url', help='URL of remote postgres database')
    parser.add_argument('--driver','-d',
                        help='Where and how to store the backup',
                        required=True,
                        nargs=2,
                        action=DriverAction,
                        metavar=('driver','destination'))
    return parser

def main():
    import time
    import boto3
    from pgbackup import pgdump, storage
    args = create_parser().parse_args()
    dump = pgdump.dump(args.url)
    if args.driver == 's3':
        client = boto3.client('s3')
        timestamp = time.strftime('%Y-%m-%dT%H:%M:%S')
        filename = pgdump.dump_file_name(args.url, timestamp)
        print(f'Backup up database to S3 as {filename}')
        storage.s3(client, dump.stdout, args.destination, filename)
    else:
        outfile = open(args.destination, 'wb')
        print(f'Backup up database locally to {args.destination}')
        storage.local(dump.stdout, outfile)
