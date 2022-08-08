# data-capture-challenge

## Overview
  Sample code for Data Capture challenge.

## Requirements
- Python3 installed version > 3.5
- python3 alias setup and available in PATH for the directory when running the python commands.
  see [python alias & path WINDOWS](https://docs.python.org/es/3/using/windows.html)
  see [python alias & path MAC](https://docs.python.org/es/3/using/mac.html)


## Makefile
  Make commands are available and described using make help inside the repository directory, if make is installed.

## Time complexity and requirements

### Available algorithms
  This sections will explain in Big O notation the complexity of the methods implemented of both classes
  DataCapture and DataStats

- `add, less, greater, between`
  This algorithms were required to be implemented using a complexity of O(1).

  The fixed complexity of O(1) is only achievable for `add` method, since it represents an insert into an
  specific index.

  The method `less` is complexity O(3) cause involves a value validation, subtraction and get value by index,
  but if the validation is ignored it would become O(2).

  The method `greater` is complexity O(3) cause involves a value validation and two get value by index,
  but if the validation is ignored it would become O(2).

  The method `between` is complexity O(7) cause involves three value validations, two substracions
  and two get value by index, but if the validations are ignored it would become O(4).

  All the previous methods are constant, but not time complexity O(1).


- `build_stats` It's a list transformation into a new list with the accumulates of the DataCapture.storage.
  Complexity O(n).


## Logging
  A basic loggin strategy was implemented, just a basic error handling and a text file based system
  (.gitignored for convenience)

