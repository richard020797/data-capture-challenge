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

  The fixed complexity of O(1) is only achievable for `add` method, since it represents a push into a stack.

  `less, greater and between` can only be implemented using O(n) since will required either to order the data provided
  which in best case scenario is a O(log(n)) complexity considering an ordered insertion or a simple Tim sort algorithm
  which was the actual implmentation.
  Or the second option will require a standard linear search algorithm that would check if every element in the data
  array fulfils one or both conditions for `less, greater or between`.
  Simple O(1) complexity is not possible with the provided paradigm.

- `build_stats` algorithm includes a sort (Tim sort) and a data asignation which translates into a
  O(n log(n)) complexity, better than O(n).


## Logging
  A basic loggin strategy was implemented, just a basic error handling and a text file based system
  (.gitignored for convenience)
