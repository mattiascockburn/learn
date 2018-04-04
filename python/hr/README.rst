hr
==

Some random excercise which utilises a JSON inventory in order to manage users

Starting Development
--------------------

1. Install ``pipenv``
2. Clone the repo
3. Run ``pipenv install --dev``

Usage
-----

Execute it with an inventory:
::
  $ hr path/to/inventory.json
  Adding user 'kevin'
  Added user 'kevin'
  Updating user 'lisa'
  Updated user 'lisa'
  Removing user 'alex'
  Removed user 'alex'

Export data
::
  $ hr --export path/to/inventory.json
  stuff....


