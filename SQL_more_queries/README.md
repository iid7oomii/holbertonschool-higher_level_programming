# SQL - More queries

Short description
-----------------
A small collection of SQL exercise scripts and helper shell utilities for practicing additional MySQL queries (part of Holberton School exercises). This folder focuses on "more queries" beyond the introductory examples and includes convenience scripts to prepare a local environment.

Problem this project solves
---------------------------
Provides example SQL statements and a minimal workspace to help learners practice and experiment with MySQL queries and database interactions on a local machine.

Main features
-------------
- setup.sh — convenience script that installs a few developer utilities (pip packages and system packages) and sets global Git configuration.
- p — tiny bash helper to add, commit and push changes to the repository.
- (Optional) SQL query files — this folder is the place to add SQL exercise files that demonstrate more advanced or varied SQL queries.

Tech stack
----------
- SQL (MySQL dialect)
- Bash (shell helper scripts)
- pycodestyle (referenced for style checks)

Project structure and file purposes
----------------------------------
- README.md — this file.
- setup.sh — installs pycodestyle, tmux and mysql-server (uses apt and pip) and configures global Git user/email/credential helper. Inspect before running.
- p — small commit-and-push helper script that stages all changes, commits with a provided message (or default message) and pushes to the remote.

Setup and installation steps
----------------------------
1. Inspect the included scripts before running them. They modify system packages and global Git configuration.
2. To run the environment setup (Debian/Ubuntu systems):
   - sudo bash setup.sh
3. Alternatively, install required software manually:
   - pip install pycodestyle
   - sudo apt update && sudo apt install -y tmux mysql-server
4. Configure MySQL (create users/databases) as needed for your exercises.

How to run the project
----------------------
- Run the setup script (if desired):
  - sudo bash setup.sh

- Use the `p` helper to commit and push changes (from inside the folder or repo root):
  - ./p "commit message"
  - If no message is provided, the script uses the default message "Update files".

- Execute SQL files against a running MySQL server using the mysql client:
  - mysql -u <user> -p <database_name> < 14-some_query.sql
  - Or open an interactive MySQL session and source a file:
    - mysql -u <user> -p
    - USE <database_name>;
    - SOURCE /path/to/file.sql;

Configuration or environment variables
--------------------------------------
- The scripts in this folder do not read environment variables. When running SQL queries you will need a running MySQL server and valid credentials (username/password) and the target database name.
- `setup.sh` requires sudo/root to install system packages and will set Git global configuration values listed in the script. Edit the script if you want to use different Git user/email settings.

Example usage
-------------
- Install and configure tools (Debian/Ubuntu):
  - sudo bash setup.sh

- Add, commit and push changes using the helper:
  - ./p "Add new SQL exercises"

- Run an SQL file against a database:
  - mysql -u root -p my_db < 10-more_query.sql

Notes and limitations
---------------------
- setup.sh uses apt and pip and is tailored to Debian/Ubuntu-like environments. Do not run it on other distributions without inspection and modification.
- setup.sh modifies global Git configuration (user.email, user.name, credential.helper); inspect and change those values before running if needed.
- The `p` helper stages all changes in the repository (git add .) before committing; use with caution to avoid committing unintended files.
- This README is based strictly on the files currently present in this folder (setup.sh and p). There may be no SQL exercise files yet; add SQL files to this folder to store and share queries and exercises.