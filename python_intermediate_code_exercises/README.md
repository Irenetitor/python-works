# Python Intermediate Code Exercises

Exercises from the MoureDev Pro course "Python Intermedio".

## Purpose

This folder contains practical exercises to reinforce intermediate Python concepts, including:

- Date and time manipulation
- List comprehensions and data structures
- Lambda functions and higher-order functions
- Error handling and exceptions
- File handling and I/O operations
- Regular expressions
- Package management and imports
- And more...

## Structure

Each file focuses on a specific topic, with small, runnable examples.

The `resources/` folder contains downloaded course files used as questions and templates for exercises.

## Getting Started

### Prerequisites

- Python 3.8+
- pip (Python package manager)

### Installation

1. Clone this repository:
```bash
git clone https://github.com/Irenetitor/python-works.git
cd python-works
```

2. Create a virtual environment (optional but recommended):
```bash
python -m venv .venv
.venv\Scripts\activate  # On Windows
source .venv/bin/activate  # On macOS/Linux
```

3. Install dependencies for this folder:
```bash
cd python_intermediate_code_exercises
pip install -r requirements.txt
```

## Usage

Run any exercise file directly:

```bash
python 00_dates.py
python 08_package_manager.py
```

## Dependencies by file

Most files use only the Python standard library. The only external dependencies are used in:

- `08_package_manager.py`: requires `numpy`, `pandas`, and `requests`

If you run `pip install -r requirements.txt`, you can execute all files in this folder.

## Learning Goals

- Strengthen core Python fundamentals
- Explore advanced Python features
- Develop problem-solving skills
- Build a solid foundation for more complex projects

## Notes

These exercises are part of the MoureDev Pro "Python Intermedio" course:
https://campus.mouredev.pro/courses/python-intermedio

---

**Happy Coding!** 🐍
