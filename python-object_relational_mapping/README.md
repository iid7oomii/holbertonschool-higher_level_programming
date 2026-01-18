# Python - Object-relational mapping

Short description
-----------------
A small collection of Python scripts and SQLAlchemy models demonstrating basic object-relational mapping (ORM) and simple MySQL queries for a database containing `states` and `cities`.

Problem this project solves
---------------------------
Provides simple, focused examples for:
- Defining SQLAlchemy models for `State` and `City`.
- Querying a MySQL database from Python using MySQLdb (classic DB-API) and SQLAlchemy.
- Safe parameterized queries to help avoid SQL injection.
- Demonstrating a relationship (one-to-many) between states and cities and a sample update using SQLAlchemy sessions.

Main features
-------------
- SQLAlchemy model definitions:
  - `model_state.py` and `relationship_state.py` show how to define a `State` model (one file with simple declarative Base, another with a `cities` relationship).
  - `model_city.py` defines a `City` model with a foreign key to `states.id`.
- Small utility scripts using MySQLdb:
  - `0-select_states.py` — list all states (ordered by id).
  - `3-my_safe_filter_states.py` — parameterized query to safely filter states by name.
  - `5-filter_cities.py` — list all cities for a given state.
- SQLAlchemy example:
  - `12-model_state_update_id_2.py` — find the `State` record with id 2 and rename it (commits via SQLAlchemy session).
- Helper/setup scripts:
  - `setup.sh` — convenience script to install some tools referenced in the repository (pycodestyle, tmux, mysql-server) and to configure Git global user/email.
  - `p` — a small bash helper to add/commit/push changes (simple push helper script).

Tech stack
----------
- Python 3 (shebangs show usage as executable scripts)
- MySQL (server)
- MySQLdb DB-API (imported as `MySQLdb` in scripts)
- SQLAlchemy ORM (models and session usage)
- Shell scripts for setup and git convenience
- pycodestyle referenced in `setup.sh` for style checking

Project structure and file purposes
-----------------------------------
- model_state.py — SQLAlchemy `State` model using `declarative_base()`. 
- relationship_state.py — SQLAlchemy `State` model including:
  - `cities = relationship("City", backref="state", cascade="all, delete")`
  - demonstrates a one-to-many relationship and cascade delete.
- model_city.py — SQLAlchemy `City` model with `state_id` ForeignKey to `states.id`.
- 0-select_states.py — lists all rows from `states` (uses MySQLdb).
- 3-my_safe_filter_states.py — parameterized query selecting states by name (safe against SQL injection).
- 5-filter_cities.py — lists city names for a provided state name (joins cities and states).
- 12-model_state_update_id_2.py — uses SQLAlchemy to change the name of the State where id == 2.
- setup.sh — installs pycodestyle, tmux, mysql-server and sets Git global user/email as configured in the script.
- p — simple commit-and-push helper (adds, commits, pushes).
- README.md — this file.

Setup and installation
----------------------
The repository assumes a local MySQL server is available and that you will provide MySQL credentials and a database name when running the scripts.

A basic setup flow (adjust for your OS/distribution):

1. Install system dependencies (on Debian/Ubuntu-like systems):
   - mysql-server (setup.sh installs it via apt)
   - build dependencies required by some Python MySQL clients (e.g., `build-essential`, `libmysqlclient-dev`, `python3-dev`) — install as needed for your platform.

2. Install Python packages used by this project:
   - SQLAlchemy
   - a MySQLdb-compatible package (the code imports `MySQLdb`; commonly this is provided by `mysqlclient` on many systems)

   Example:
   - pip install SQLAlchemy mysqlclient pycodestyle

3. (Optional) Run the provided setup helper script to install some utilities and set git config:
   - bash setup.sh
   - Note: `setup.sh` installs `pycodestyle`, `tmux`, `mysql-server` and sets Git global name/email as configured in the script.

How to run the project
----------------------
All Python scripts are executable and expect command-line arguments for DB credentials and database name.

Examples (replace placeholders with your credentials and database):

- List all states (0-select_states.py)
  - python3 0-select_states.py <mysql_user> <mysql_password> <database_name>

- Safe filter by state name (3-my_safe_filter_states.py)
  - python3 3-my_safe_filter_states.py <mysql_user> <mysql_password> <database_name> "<state_name>"

- List cities for a state (5-filter_cities.py)
  - python3 5-filter_cities.py <mysql_user> <mysql_password> <database_name> "<state_name>"

- Update state name with SQLAlchemy (12-model_state_update_id_2.py)
  - python3 12-model_state_update_id_2.py <mysql_user> <mysql_password> <database_name>
  - This script looks up the State with id == 2 and changes its name to `New Mexico` (commits if found).

Configuration / environment variables
-------------------------------------
- No environment variables are read by the scripts in this folder.
- Database credentials and database name must be supplied as positional command-line arguments, in the order visible in the scripts:
  1. MySQL username
  2. MySQL password
  3. Database name
  - For the scripts that filter by name (3-my_safe_filter_states.py, 5-filter_cities.py) an additional 4th argument is the state name to filter by.

- SQLAlchemy connection string used in `12-model_state_update_id_2.py`:
  - `'mysql+mysqldb://{}:{}@localhost/{}'` filled with the three command-line args.

Example usage
-------------
Assuming a local MySQL server, a database `hbtn_0e_0_usa` and user `root`:

- List states:
  - python3 0-select_states.py root mypassword hbtn_0e_0_usa

- Get information for state named "California" (safe):
  - python3 3-my_safe_filter_states.py root mypassword hbtn_0e_0_usa "California"

- List cities in state "California":
  - python3 5-filter_cities.py root mypassword hbtn_0e_0_usa "California"

- Update state with id 2 using SQLAlchemy:
  - python3 12-model_state_update_id_2.py root mypassword hbtn_0e_0_usa

Notes and limitations
---------------------
- The scripts assume:
  - A local MySQL server is running on `localhost` using port `3306`.
  - The database and tables (`states`, `cities`) exist and follow the expected schema (fields used in the scripts: `id`, `name`, `state_id`).
  - Proper credentials are provided as command-line arguments.
- There are no migration scripts or DDL included to create the `states` and `cities` tables — you must create them separately or use an existing dataset.
- Error handling is minimal (scripts will raise exceptions on connection failure or missing arguments).
- `0-select_states.py` and `5-filter_cities.py` print raw rows or comma-separated names; they are intended as small demonstration scripts rather than production utilities.
- `3-my_safe_filter_states.py` demonstrates parameterized queries to avoid SQL injection; other scripts that compose SQL strings without parameters may be vulnerable if altered.
- `relationship_state.py` sets `cascade="all, delete"` for the `cities` relationship — deleting a State via an ORM session will delete related City objects (SQLAlchemy behavior).
- The `setup.sh` script contains hardcoded Git user/email configuration:
  - user.email: abdulrahman18alghamdi@gmail.com
  - user.name: iid7oomii
  - Adjust before running if those values are not desired.

Repository analysis notes
-------------------------
I based this README strictly on the files found in the repository folder `python-object_relational_mapping`. The code search results used to build this summary may be incomplete; to view the folder in the repository, see:

https://github.com/iid7oomii/holbertonschool-higher_level_programming/tree/main/python-object_relational_mapping
