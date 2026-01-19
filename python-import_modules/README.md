# Python - Import & Modules

A collection of Python scripts demonstrating the fundamentals of importing modules, functions, and variables in Python.  This project is part of the Holberton School Higher Level Programming curriculum.

## Problem This Project Solves

This project addresses the essential concept of code reusability in Python through importing.  It demonstrates how to: 
- Import functions from other modules
- Use the `sys` module to handle command-line arguments
- Discover module attributes dynamically
- Prevent code execution during imports using `if __name__ == "__main__"`

## Main Features

- **Function Import**: Import and use functions from custom modules
- **Command-Line Argument Handling**: Parse and process arguments passed to Python scripts
- **Calculator Operations**: Perform basic arithmetic operations using imported functions
- **Dynamic Module Discovery**: Explore module attributes programmatically
- **Variable Import**: Load and use variables from external modules

## Tech Stack

- **Language**: Python 3
- **Standard Libraries**: `sys` module for command-line arguments

## Project Structure

```
python-import_modules/
├── README.md                    # Project documentation
├── add_0.py                     # Module with addition function
├── calculator_1.py              # Module with basic calculator functions (add, sub, mul, div)
├── 0-add.py                     # Script importing and using the add function
├── 1-calculation.py             # Script performing multiple calculations
├── 2-args.py                    # Script handling command-line arguments
├── 3-infinite_add.py            # Script adding infinite number of arguments
├── 4-hidden_discovery.py        # Script discovering non-hidden module names
└── 5-variable_load.py           # Script importing and printing a variable
```

## Setup and Installation

### Prerequisites

- Python 3.x installed on your system
- Unix-like environment (Linux, macOS, or WSL on Windows)

### Installation

1. Clone the repository:
```bash
git clone https://github.com/iid7oomii/holbertonschool-higher_level_programming.git
```

2. Navigate to the project directory:
```bash
cd holbertonschool-higher_level_programming/python-import_modules
```

3. Make scripts executable (if needed):
```bash
chmod +x *.py
```

## How to Run the Project

### Basic Addition (0-add.py)
```bash
./0-add.py
```
**Output**: `1 + 2 = 3`

### Calculator Operations (1-calculation.py)
```bash
./1-calculation.py
```
**Output**:
```
10 + 5 = 15
10 - 5 = 5
10 * 5 = 50
10 / 5 = 2
```

### Command-Line Arguments (2-args.py)
```bash
./2-args.py Hello World
```
**Output**:
```
2 arguments:
1: Hello
2: World
```

### Infinite Addition (3-infinite_add.py)
```bash
./3-infinite_add.py 10 20 30 40
```
**Output**: `100`

### Hidden Discovery (4-hidden_discovery.py)
```bash
./4-hidden_discovery.py
```
Discovers and prints all non-hidden names from the `hidden_4` module.

### Variable Load (5-variable_load.py)
```bash
./5-variable_load.py
```
Imports and prints the value of variable `a` from `variable_load_5` module.

## Configuration or Environment Variables

No special configuration or environment variables are required.  All scripts use standard Python 3 features.

## Example Usage

### Using the calculator module in your own script:
```python
#!/usr/bin/python3
from calculator_1 import add, mul

result_add = add(5, 3)
result_mul = mul(4, 7)
print(f"Addition: {result_add}, Multiplication: {result_mul}")
```

### Creating a module-safe script:
```python
#!/usr/bin/python3
if __name__ == "__main__": 
    # This code only runs when script is executed directly
    print("Running as main program")
```

## Notes or Limitations

- **Module Dependencies**: Scripts `4-hidden_discovery.py` and `5-variable_load.py` require external modules (`hidden_4` and `variable_load_5`) that are not included in this directory
- **Python 3 Only**: All scripts use Python 3 syntax and shebang (`#!/usr/bin/python3`)
- **Educational Purpose**: These scripts are designed for learning purposes and demonstrate fundamental concepts rather than production-ready code
- **Integer Division**: The `div` function in `calculator_1.py` performs integer division, not floating-point division