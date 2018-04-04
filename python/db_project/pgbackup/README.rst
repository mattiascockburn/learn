pgbackup
========

Creates backups of remote pgsql databases and may save them locally or on S3

Prepare for Development
-----------------------

1. Make sure ``pip`` and ``pipenv`` are installed
2. Clone repo
3. cd into it
4. Fetch dev deps: ``make install``
5. Activate virtualenv: ``pipenv shell``

Usage
-----

::

    $ pgbackup postgres://bob@example.com:5432/db_one --driver s3 backups

Local Example w/ local path:

::

    $ pgbackup postgres://bob@example.com:5432/db_one --driver local /var/local/db_one/backups

Running Tests
-------------

Run tests locally using ``make`` if virtualenv is active:

::

    $ make

If virtualenv isn’t active then use:

::

    $ pipenv run make
