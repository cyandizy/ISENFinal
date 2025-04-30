# Cover page

# Introduction

# Module descriptions

## Module calculator

```
Submodule calculate_lucky_number
Imports: birthday (Date)
Exports: lucky_number (integer)

Calculates lucky number.
```

```
Submodule get_lucky_animal
Imports: lucky_number (integer)
Exports: lucky_animal (string)

Calculates lucky animal.
```

```
Submodule get_generation
Imports: year (integer)
Exports: generation (string)

Calculates generation of a birthday.
```

```
Submodule is_master_number
Imports: lucky_number (integer)
Exports: result (boolean)

Checks if a lucky number is a master number.
```

## Module logic

```
Submodule same_luck
Imports: birthday1 (Date), birthday2 (Date)
Exports: result (boolean)

Checks if two dates have the same lucky number and lucky animal.
```

## Module data_structures

```
Class Date
day: integer
month: integer
year: integer
```

# Modularity

# Black-box test cases

#### Submodule calculate_lucky_number
| No. | Category                                                                              | Input<br>Date | Expected Output<br>lucky_number |
| --- | ------------------------------------------------------------------------------------- | ------------- | ------------------------------- |
| 1   | Date.day = 1-31, <br>Date.month = 1-12, <br>Date.year = 1901-2024 <br>(all inclusive) | 10, 3, 2006   | 12                              |
| 2   | Invalid day                                                                           | 0, 2, 2001    | Exception                       |
| 3   | Invalid month                                                                         | 10, 0, 1999   | Exception                       |
| 4   | Invalid year                                                                          | 20, 4, 9999   | Exception                       |
| 5   | Invalid day and month                                                                 | -1, 0, 2004   | Exception                       |
| 6   | Invalid month and year                                                                | 4, 99, 2193   | Exception                       |
| 7   | Invalid day and year                                                                  | 111, 12, 9    | Exception                       |
| 8   | Invalid day, month, and year                                                          | 99, 99, 9999  | Exception                       |

#### Submodule get_lucky_animal
| No. | Category<br>lucky_number<br>                      | Input<br>lucky_number | Expected Output<br>lucky_animal |
| --- | ------------------------------------------------- | --------------------- | ------------------------------- |
| 1   | == 1                                              | = 1                   | "Parrot"                        |
| 2   | == 2                                              | = 2                   | "Rabbit"                        |
| 3   | == 3                                              | = 3                   | "Elephant"                      |
| 4   | == 4                                              | = 4                   | "Beetles"                       |
| 5   | == 5                                              | = 5                   | "Bears"                         |
| 6   | == 6                                              | = 6                   | "Deer"                          |
| 7   | == 7                                              | = 7                   | "Crane"                         |
| 8   | == 8                                              | = 8                   | "Horse"                         |
| 9   | == 9                                              | = 9                   | "Fish"                          |
| 10  | == 11                                             | = 11                  | "Dolphin"                       |
| 11  | == 22                                             | = 22                  | "Lion"                          |
| 12  | == 33                                             | = 33                  | "Turtle"                        |
| 13  | Not in range 1-9 inclusive and not 11, 22, and 33 | = 0                   | ""                              |

#### Submodule get_generation
| No. | Category             | Input<br>year | Expected Output<br>generation |
| --- | -------------------- | ------------- | ----------------------------- |
| 1   | 1901 <= year <= 1945 | = 1930        | "Silent Generation"           |
| 2   | 1946 <= year <= 1964 | = 1950        | "Baby Boomers"                |
| 3   | 1965 <= year <= 1979 | = 1970        | "Generation X"                |
| 4   | 1980 <= year <= 1994 | = 1990        | "Millennials"                 |
| 5   | 1995 <= year <= 2009 | = 2000        | "Generation Z"                |
| 6   | 2010 <= year <= 2024 | = 2020        | "Generation Alpha"            |

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