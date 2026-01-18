# Python Exceptions

Small set of Python 3 exercises demonstrating how to handle and raise exceptions safely. Each file in this directory is a standalone function (plus small *-main.py drivers) focused on common exception patterns.

## Problem this project solves

When working with user input or external data, programs must fail gracefully. This project shows how to:

- Catch common runtime errors (`TypeError`, `ValueError`, `ZeroDivisionError`, `IndexError`)
- Provide safe defaults instead of crashing
- Use `try`/`except`/`finally` correctly
- Raise exceptions intentionally when a condition must be enforced

## Main features

- **Safe printing helpers**
  - Print the first *x* elements of a list without crashing when the list is too short.
  - Print only integer values from a mixed list.
  - Print an integer safely and report success/failure.
- **Safe division helpers**
  - Divide two values while handling division-by-zero.
  - Divide elements from two lists with detailed error handling per element.
- **Explicit exception raising**
  - Raise a `TypeError`
  - Raise a `NameError` with a custom message

## Tech stack

- **Python 3**
- Standard library only (no third-party dependencies)

## Project structure

This README documents the `python-exceptions/` directory within the larger Holberton School *higher level programming* repository.

```
python-exceptions/
├── README.md
├── 0-safe_print_list.py
├── 0-main.py
├── 1-safe_print_integer.py
├── 2-safe_print_list_integers.py
├── 3-safe_print_division.py
├── 4-list_division.py
├── 5-raise_exception.py
└── 6-raise_exception_msg.py
```

### File descriptions

- `0-safe_print_list.py`: Prints up to `x` elements from `my_list` and returns how many were printed; stops on `IndexError`.
- `1-safe_print_integer.py`: Prints `value` as an integer and returns `True` on success; returns `False` on `ValueError`/`TypeError`.
- `2-safe_print_list_integers.py`: Prints up to `x` elements from `my_list` **only if** they can be formatted as integers; skips non-integers.
- `3-safe_print_division.py`: Divides `a / b`; returns `None` on division by zero; always prints `Inside result: ...` in a `finally` block.
- `4-list_division.py`: Builds and returns a new list of length `list_length` where each item is `my_list_1[i] / my_list_2[i]`; prints an error message and uses `0` on common failures.
- `5-raise_exception.py`: Function that raises a `TypeError`.
- `6-raise_exception_msg.py`: Function that raises a `NameError` with an optional message.
- `0-main.py`: Small driver script to exercise `safe_print_list`.

## Setup and installation

1. Clone the repository:

   ```bash
   git clone https://github.com/iid7oomii/holbertonschool-higher_level_programming.git
   cd holbertonschool-higher_level_programming
   ```

2. Move into the project directory:

   ```bash
   cd python-exceptions
   ```

## How to run

Run any of the provided driver or test scripts with Python 3. For example:

```bash
python3 0-main.py
```

You can also import the functions from an interactive shell or another script:

```bash
python3
```

```python
from __future__ import print_function
from importlib import import_module

safe_print_list = import_module('0-safe_print_list').safe_print_list
print(safe_print_list([1, 2, 3], 10))
```

## Configuration / environment variables

None. These scripts use no environment variables and require no configuration files.

## Example usage

### Safe list printing

```python
from importlib import import_module

safe_print_list = import_module('0-safe_print_list').safe_print_list
print('printed:', safe_print_list([1, 2, 3], 5))
```

### List division with error handling

```python
from importlib import import_module

list_division = import_module('4-list_division').list_division
print(list_division([10, 20, 'x'], [2, 0, 5], 3))
```

## Notes / limitations

- These are educational exercise files, not a packaged library (no `setup.py`/`pyproject.toml`).
- Some modules begin with digits (e.g., `0-safe_print_list.py`), so direct `import 0-safe_print_list` is invalid Python syntax; use `__import__()` or `importlib.import_module()` as demonstrated.
