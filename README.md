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
  specific index, although the read to sum the existing value count transforms this into complexity O(2).

  `less, greater and between` can only be implemented using O(1) complexity considering it's a slicing of the
  self.storage list. Yet any strategy requires the sum of the result list of elements, to provide a count.
  adding a not so common described O(m) complexity, which will define the whole operation as O(1 + m), `m` being
  the size of the resulting slice and the operation of sum over that slice, worst case scenario `m` would be
  the same size as `n` and therefore complexity results as O(n), would appreciate a lot any comments suggesting
  a different alternative to reach complexity O(1).

- `build_stats` It's just an assignment of the sotorage list, O(1) 

## Logging
  A basic loggin strategy was implemented, just a basic error handling and a text file based system
  (.gitignored for convenience)

