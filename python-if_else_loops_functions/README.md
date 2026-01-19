# Python — If / Else, Loops & Functions

Short description
This directory contains small Python 3 exercises that demonstrate core programming constructs: conditional statements (if/elif/else), loops, and simple functions. Files are individual exercises or small drivers intended for learning and manual verification.

Problem this project solves
These exercises provide concise, focused implementations to practice:
- conditionals and branching
- loops and iteration
- simple function definitions and returns
- basic string and numeric manipulation

Main features
- A set of minimal, self-contained Python exercises.
- Some files are executable scripts that print output when run.
- Other files provide a single function intended to be imported and tested or used by a driver.
- Uses only the Python standard library (no external dependencies).

Tech stack
- Python 3 (scripts include a Python 3 shebang).
- Standard library modules used: `random` in a couple of driver scripts.

Project structure explanation
The directory contains exercise files. Each file implements one small task. Below is the list of files found and short descriptions based strictly on the code in this directory:

- 0-positive_or_negative.py — script: generates a random integer and prints whether it is positive, zero, or negative.
- 1-last_digit.py — script: generates a random integer and prints a message about its last digit (uses modulo rules; output varies).
- 2-print_alphabet.py — script: prints the lowercase English alphabet (a..z) with no separator.
- 3-print_alphabt.py — script: prints lowercase alphabet excluding `e` and `q`.
- 5-print_comb2.py — script: prints all numbers from 00 to 99 separated by commas, formatted as two digits.
- 6-print_comb3.py — script: prints combinations of two different digits (00..99 style) as implemented in the file.
- 7-islower.py — function: `islower(c)` returns True if character `c` is lowercase (by checking ASCII code), otherwise False.
- 7-main.py — driver: imports `islower` from `7-islower.py` and prints whether a set of sample characters are lower/upper.
- 8-uppercase.py — function: `uppercase(str)` prints the given string converting lowercase ASCII letters to uppercase (outputs to stdout).
- 9-print_last_digit.py — function: `print_last_digit(number)` prints and returns the last digit of `number`.
- 10-add.py — function: `add(a, b)` returns the sum `a + b`.
- 11-pow.py — function: `pow(a, b)` returns `a ** b`.
- 12-fizzbuzz.py — function: `fizzbuzz()` prints numbers 1..100 with Fizz/Buzz/FizzBuzz rules to stdout.

Setup and installation steps
1. Ensure Python 3 is installed on your system:
   - python3 --version
2. Clone the repository (if you haven't already):
   - git clone https://github.com/iid7oomii/holbertonschool-higher_level_programming.git
3. Change to this directory:
   - cd holbertonschool-higher_level_programming/python-if_else_loops_functions

How to run the project
- Run an executable script directly with Python 3. Examples:
  - python3 2-print_alphabet.py
  - python3 3-print_alphabt.py
  - python3 5-print_comb2.py
  - python3 6-print_comb3.py
  - python3 7-main.py
- Import function modules from an interactive shell or another script and call functions:
  - python3
    >>> from 10-add import add
    >>> add(2, 3)
    5
  - For `fizzbuzz` (12-fizzbuzz.py):
    >>> from 12-fizzbuzz import fizzbuzz
    >>> fizzbuzz()
    (prints Fizz/Buzz/FizzBuzz output to stdout)

Configuration or environment variables
- None. These scripts use no configuration files or environment variables.

Example usage and expected outputs
- python3 2-print_alphabet.py
  - Output: the lowercase alphabet "abcdefghijklmnopqrstuvwxyz" (no newline after each char; the script prints a newline at the end if implemented).
- python3 3-print_alphabt.py
  - Output: the lowercase alphabet without 'e' and 'q'.
- python3 7-main.py
  - Deterministic output based on the driver code:
    a is lower
    H is upper
    A is upper
    3 is upper
    g is lower
- Using functions:
  - from 10-add import add; add(2, 3) -> returns 5
  - from 11-pow import pow; pow(2, 3) -> returns 8
  - from 9-print_last_digit import print_last_digit; print_last_digit(-98) -> prints '8' and returns 8
- Randomized scripts:
  - 0-positive_or_negative.py and 1-last_digit.py use `random.randint(...)`. Their exact printed messages vary each run.

Notes and limitations
- These are small educational exercises — not a production library.
- A number of files define functions but do not include command-line drivers; import them to use in scripts or the REPL.
- Some scripts produce non-deterministic output because they use `random`.
- There are no unit tests or packaging included in this directory.
- This README was generated strictly from the repository's current source files; if you need additional details or a different format (project-level README, badges, tests), tell me and I can prepare it.

Repository link and search results note
- I inspected files from this directory in the repository. The search/inspection results may be incomplete; to view the full directory contents in the GitHub UI visit:
  https://github.com/iid7oomii/holbertonschool-higher_level_programming/tree/main/python-if_else_loops_functions