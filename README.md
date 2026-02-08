# Fields
Generates the field lines of irrotational fields and their respective equipotentual surfaces.

-----------------------------------------------------------------------------
# Setting up the virtual environment and installing libraries

A virtual environment is needed to install packages locally rather than globally.
This is important as different projects may need different versions of the same
library. It also allows to have project-specific dependencies.

1) Create a virtual environment via the following command:
```shell
$ py -m venv venv   //or//   python -m venv venv
```
2) Individual libraries(e.g. black) are then installed via the following command:
```shell
$ pip install black
```
For a particular version, one could use:
```shell
$ pip install black=22.3.0
```
-----------------------------------------------------------------------------
# Using Black

The Black library is a code formatter for Python, designed to enforce consistent and readable code formatting. It automatically reformats Python code to PEP 8.

1) Line length configuration - by default this sets lines to 88 characters. 
If needed, it can be changed via the following command:
```shell
$ black --line-length 100 my_file.py
```
2) Checking for formatting issues without modifying a file:
```shell
$ black --check my_file.py
```
3) Formatting a file:
```shell
$ black my_file.py
```
4) Formatting an entire directory:
```shell
$ black .
```



# TODO: Add in a separate file
Dependencies:
- matplotlib
- scipy
- pytest
- black