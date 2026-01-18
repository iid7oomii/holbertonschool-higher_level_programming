# Python - Data Structures: Lists & Tuples

Short exercises and utilities implemented in Python 3 that demonstrate basic operations on lists, tuples and related simple data structures. Each exercise implements a small function (or set of functions) and is accompanied by a short `*_main.py` script that illustrates usage.

Problem this project solves
- Provides concise, focused implementations of common list/tuple tasks to help learners practice and understand:
  - reading and printing list contents
  - accessing elements by index
  - replacing or inserting elements
  - simple tuple operations
  - basic matrix printing
  - small utility operations commonly required in introductory Python courses

Main features
- Small, single-purpose Python functions (one file = one exercise)
- Paired `*-main.py` example scripts that demonstrate how each function is intended to be used
- Clear, minimal implementations suitable for study, testing and incremental learning

Tech stack
- Python 3 (scripts use Python 3 syntax; run with `python3`)

Project structure (relevant files in python-data_structures/)
- 0-print_list_integer.py — print each integer from a list on its own line
- 0-main.py — example/test runner for `0-print_list_integer.py`
- 1-element_at.py — return element at a given index (with bounds handling)
- 1-main.py — example/test runner for `1-element_at.py`
- 2-replace_in_list.py — replace an element at a given index (with bounds handling)
- 2-main.py — example/test runner for `2-replace_in_list.py`
- 3-print_reversed_list_integer.py / 3-main.py — print a list of integers in reverse order
- 4-new_in_list.py / 4-main.py — insert a new element at a given index (preserve original on out-of-range)
- 5-no_c.py / 5-main.py — small string/list-related utility (filename indicates intent)
- 6-print_matrix_integer.py — print a matrix of integers in row/column format
- 7-add_tuple.py / 7-main.py — tuple addition helper
- 8-multiple_returns.py — function returning several related values for a list
- 9-max_integer.py — find the maximum integer in a list
- 10-divisible_by_2.py — boolean list indicating divisibility by 2
- 11-delete_at.py — delete element at a given index (with bounds handling)
- 12-switch.py — small utility (filename indicates intent)
- __pycache__/ — pycache files (ignored for source)

Notes on structure
- Each exercise file implements a single function. The corresponding `*-main.py` files import the function and print example outputs, which makes it easy to run and verify behavior manually.

Setup and installation
1. Ensure Python 3 is installed on your system (Python 3.6+ recommended).
2. Clone the repository:
   - git clone https://github.com/iid7oomii/holbertonschool-higher_level_programming.git
3. Change to the repository directory:
   - cd holbertonschool-higher_level_programming

How to run the project (examples)
- Run any example/main file with Python 3. Example:
  - python3 python-data_structures/0-main.py
  - python3 python-data_structures/1-main.py
  - python3 python-data_structures/2-main.py

Example outputs (inferred from the example scripts)
- python3 python-data_structures/0-main.py
  - Output:
    1
    2
    3
    4
    5

- python3 python-data_structures/1-main.py
  - Output:
    Element at index 3 is 4

- python3 python-data_structures/2-main.py
  - Output:
    [1, 2, 3, 9, 5]
    [1, 2, 3, 9, 5]

Configuration or environment variables
- None required. These are simple Python scripts with no external dependencies or configuration.

Example usage
- Use the provided `*-main.py` files to see how functions are called.
- Import the functions into other scripts:
  - from python-data_structures import 1-element_at (or use relative import patterns when packaging)

Notes / limitations
- This collection is a teaching / exercises repository rather than a production library.
- Functions are intentionally minimal and focused on demonstrating concepts rather than providing extensive error handling or validation beyond bounds checks where appropriate.
- No automated tests or packaging are included in this directory (use the `*-main.py` files for manual checks).
