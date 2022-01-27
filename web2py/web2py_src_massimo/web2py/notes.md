# Files
- web2py.py: Start the rocket webserver.

- For every action there is a file in views folder.

- cron folder is used to set cron-jobs.

- Contains all python modules we create.

- Private folder is for all those file that is supose to be private for the user. Is used for example to store keys.

- routes.example.py: Maps routes in application level.

- settings.cfg: Different settings related to the web base editor.

## Gluon

Is the main folder of web2py, "The core of web2py".

- .pyc files are the bytecode copiled files.

- rocket.py: The webserver of web2py.

- template.py: Implements the web2py template language, it contains the render function that defines the form how the template is implemented.

- storage.py: Implements a storage object, is like a python dictionary excepted the items can be accesed as attributes.

- dal.py: The database abstraction layer, you can use the dal.py in whatever framework that you program.
