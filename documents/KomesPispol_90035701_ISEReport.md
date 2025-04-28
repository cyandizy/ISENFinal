# Cover page

# Introduction

# Module descriptions

## Module calculator

Submodule calculate_lucky_number
Imports: birthday (Date)
Exports: lucky_number (integer)

Calculates lucky number.

Submodule get_lucky_animal
Imports: lucky_number (integer)
Exports: lucky_animal (string)

Calculates lucky animal.

Submodule get_generation
Imports: birthday (Date)
Exports: result (string)

Calculates generation of a birthday.

Submodule is_master_number
Imports: lucky_number (integer)
Exports: result (boolean)

Checks if a lucky number is a master number.

## Module logic

Submodule same_luck
Imports: birthday1 (Date), birthday2 (Date)
Exports: result (boolean)

Checks if two dates have the same lucky number and lucky animal.

## Module data_structures

Class Date
day: integer
month: integer
year: integer

# Modularity

# Black-box test cases

#### Submodule calculate_lucky_number
| No. | Category<br>Date.day, Date.month, Date.year | Input<br>Date | Expected Output<br>lucky_number |
| --- | ------------------------------------------- | ------------- | ------------------------------- |
| 1   | 1-31, 1-12, 1901-2024 (all inclusive)       | 10, 3, 2006   | 12                              |
| 2   | Invalid day                                 | 0, 2, 2001    | Exception                       |
| 3   | Invalid month                               | 10, 0, 1999   | Exception                       |
| 4   | Invalid year                                | 20, 4, 9999   | Exception                       |
| 5   | Invalid day and month                       | -1, 0, 2004   | Exception                       |
| 6   | Invalid month and year                      | 4, 99, 2193   | Exception                       |
| 7   | Invalid day and year                        | 111, 12, 9    | Exception                       |
| 8   | Invalid day, month, and year                | 99, 99, 9999  | Exception                       |


#### Submodule is_master_number
| No. | Category<br>lucky_number | Input<br>lucky_number | Expected Output<br>result |
| --- | ------------------------ | --------------------- | ------------------------- |
| 1   | == 11                    | = 11                  | True                      |
| 2   | == 22                    | = 22                  | True                      |
| 3   | == 33                    | = 33                  | True                      |
| 4   | != 11                    | = 20                  | False                     |
| 5   | != 22                    | = 14                  | False                     |
| 6   | != 33                    | = 43                  | False                     |


# White-box test cases

# Test implementation and test execution

# Summary

# Version control

# Discussion