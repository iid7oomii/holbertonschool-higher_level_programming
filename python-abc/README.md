# Python - Abstract Classes and Interfaces

Short description
-----------------
Small collection of Python examples demonstrating abstract base classes (ABCs), interfaces, and a simple example of duck typing for shapes.

Problem this project solves
---------------------------
These examples show how to define and use abstract classes and interfaces in Python using the `abc` module, and how to design classes that follow a common interface (duck typing) so they can be used interchangeably by client code.

Main features
-------------
- task_00_abc.py
  - Defines an abstract `Animal` class with an abstract `sound` method.
  - Implements concrete `Dog` and `Cat` subclasses that provide `sound()` implementations.
  - Simple top-level demonstration that prints the sound of each animal.
- task_01_duck_typing.py
  - Defines a `Shape` abstract base class with `area()` and `perimeter()` abstract methods.
  - Implements `Circle` and `Rectangle` concrete classes.
  - Provides `shape_info(any_shape)` helper that prints area and perimeter for any object implementing the required methods (demonstrates duck typing).

Tech stack
----------
- Python 3
- Standard library modules:
  - `abc` (abstract base classes)
  - `math` (for `pi` in the circle implementation)

Project structure
-----------------
- python-abc/
  - README.md (this file)
  - task_00_abc.py — Abstract `Animal` example with `Dog` and `Cat`.
  - task_01_duck_typing.py — `Shape` ABC, `Circle`, `Rectangle`, and `shape_info` helper.

Setup and installation
----------------------
No external dependencies. Ensure you have Python 3 installed.

On most systems:
- Check Python version:
  - python3 --version
- If needed, install Python 3 via your system package manager or from https://www.python.org/.

How to run the project
----------------------
Run the provided example scripts from the repository root or from within the `python-abc` directory.

Examples:
- Run the animal ABC demo:
  - python3 python-abc/task_00_abc.py
  - Output:
    - Bark
    - Meow

- Use the shape examples (interactive or via a short script). Example using Python REPL or a one-liner:
  - python3 - <<'PY'
    from python_abc.task_01_duck_typing import Circle, Rectangle, shape_info
    shape_info(Circle(3))
    shape_info(Rectangle(2, 4))
    PY

  - Or from the repository root in an interactive session:
    >>> from python_abc.task_01_duck_typing import Circle, Rectangle, shape_info
    >>> shape_info(Circle(3))
    Area: 28.274333882308138
    Perimeter: 18.84955592153876

Configuration or environment variables
--------------------------------------
None required.

Example usage
--------------
- Using `task_00_abc.py` (already performs a simple demo when run):
  - python3 python-abc/task_00_abc.py

- Using `task_01_duck_typing.py` in your code:
  - from python_abc.task_01_duck_typing import Circle, Rectangle, shape_info
  - c = Circle(5)
  - r = Rectangle(3, 6)
  - shape_info(c)
  - shape_info(r)

Notes and limitations
---------------------
- These are simple educational examples focused on illustrating ABCs and duck typing. They are intentionally minimal:
  - No unit tests are included.
  - `task_00_abc.py` contains top-level demo code (instantiates `Dog` and `Cat` and prints their sounds).
  - `task_01_duck_typing.py` defines classes and a helper function but does not include a top-level script entry point.
- Module import paths in example commands assume you run them from the repository root and that the `python-abc` package/module path is available; you may need to adjust imports or run from the `python-abc` directory depending on how you execute the examples.