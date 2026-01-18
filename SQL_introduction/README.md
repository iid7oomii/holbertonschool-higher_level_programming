# SQL - Introduction

Short description
-----------------
A small collection of SQL exercise scripts and helper shell utilities used for introductory MySQL practice (part of Holberton School exercises). The scripts demonstrate basic DDL and DML queries such as creating a table, selecting rows, aggregation, ordering and grouping.

Problem this project solves
---------------------------
Provides example SQL statements and short exercise solutions to help learners practice fundamental SQL concepts and commands against simple example tables (e.g., `first_table`, `second_table`).

Main features
-------------
- SQL scripts that demonstrate:
  - creating a simple table (`first_table`)
  - showing table creation DDL
  - counting rows with conditions
  - ordering and selecting top scores
  - computing averages
  - grouping results and counting occurrences
  - filtering out NULL values
- Small bash helpers:
  - `setup.sh` — a convenience script to install a few utilities and configure git (see notes).
  - `p` — a tiny commit-and-push helper script.

Tech stack
----------
- SQL (MySQL dialect)
- Bash (shell helper scripts)
- MySQL server (for running SQL scripts)

Project structure and file purposes
-----------------------------------
- 4-first_table.sql — Creates a table named `first_table` (defines `id INT PRIMARY KEY`, `name VARCHAR(256)`).
- 5-full_table.sql — Prints the `CREATE TABLE` statement for `first_table` (uses `SHOW CREATE TABLE`).
- 8-count_89.sql — Counts rows in `first_table` where `id = "89"`.
- 10-top_score.sql — Lists `score` and `name` from `second_table` ordered by `score` descending.
- 14-average.sql — Computes the average score from `second_table` (`SELECT AVG(score) AS average`).
- 15-groups.sql — Lists each `score` and the number of records with that score (GROUP BY `score`).
- 16-no_link.sql — Selects `score` and `name` from `second_table` where `name IS NOT NULL`, ordered by `score` descending.
- setup.sh — Installs a few tools (calls `pip install pycodestyle`, installs `tmux` and `mysql-server` via apt) and sets global git config (email/name/credential helper).
- p — Small bash helper to add, commit and push changes (accepts an optional commit message).

Setup and installation steps
----------------------------
The repository assumes you have a local MySQL server available. The included `setup.sh` automates a few installs and git configuration (it uses apt and pip and therefore requires appropriate privileges on Debian/Ubuntu-like systems).

To run the helper script (optional):
1. Make the script executable (if needed):
   - chmod +x setup.sh
2. Run it:
   - ./setup.sh

What `setup.sh` does (based on its contents):
- Installs `pycodestyle` via pip
- Installs `tmux` via apt
- Installs `mysql-server` via apt
- Sets global git `user.email`, `user.name` and `credential.helper` to the values configured inside the script

Important: the script contains hard-coded git user/email values — review and edit the script before running if you do not want those global settings applied.

How to run the project
----------------------
These are SQL files intended to be executed against a MySQL server. The scripts in this folder are standalone SQL statements; run them using the MySQL client or any MySQL GUI tool.

Examples:
- Execute a single SQL file against a database:
  - mysql -u <user> -p <database_name> < 4-first_table.sql
- Run a query file that expects a specific database (files reference `hbtn_0c_0` in comments; ensure that database and any required tables exist):
  - mysql -u root -p hbtn_0c_0 < 10-top_score.sql
- Alternatively, start an interactive MySQL session and source a file:
  - mysql -u <user> -p
  - USE hbtn_0c_0;
  - SOURCE /path/to/14-average.sql;

Configuration or environment requirements
-----------------------------------------
- A running MySQL server and credentials with privileges to create/select tables as needed.
- The SQL files reference example table names such as `first_table` and `second_table` and (in comments) the database name `hbtn_0c_0`. Ensure these exist and are populated if you expect the scripts to return meaningful results.
- `setup.sh` uses apt and pip; running it requires a Debian/Ubuntu-like system and appropriate privileges (sudo/root).

Example usage
-------------
1. Create the `first_table`:
   - mysql -u root -p my_db < 4-first_table.sql
2. Show the table creation DDL:
   - mysql -u root -p my_db -e "SHOW CREATE TABLE first_table\G"
   - or: mysql -u root -p my_db < 5-full_table.sql
3. Count rows with id = 89:
   - mysql -u root -p my_db < 8-count_89.sql

Notes and limitations
---------------------
- These files are exercise/demo SQL scripts. Some scripts expect the presence of specific tables and a database (comments reference `hbtn_0c_0` and tables `first_table` / `second_table`). They will fail or return empty results if those objects are not present or populated.
- The `setup.sh` script will modify system packages and set global git config values; inspect and edit it before running if necessary.
- The small `p` helper performs `git add .`, `git commit -m "<message>"` and `git push`. Use it with caution; it stages all changes in the current repository.
- This README is based on the files present in this repository folder. The analysis may be incomplete; view the folder in the GitHub UI for the full file listing:
  - https://github.com/iid7oomii/holbertonschool-higher_level_programming/tree/main/SQL_introduction