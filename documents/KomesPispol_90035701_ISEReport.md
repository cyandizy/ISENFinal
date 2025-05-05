# Cover page
### Assignment
#### By Komes Pispol 90035701
#### Class Tuesday, 9:00 AM


# Introduction
`A brief overview of work you have done.`
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

## Module logic

```
Submodule same_luck
Imports: birthday1 (Date), birthday2 (Date)
Exports: result (boolean)

Checks if two dates have the same lucky number and lucky animal.
```

```
Submodule is_master_number
Imports: lucky_number (integer)
Exports: result (boolean)

Checks if a lucky number is a master number.
```

## Module data_structures

```
Class Date
Imports: None

Stores day, month, year in integer format.

Method prompt_date
Imports: None
Exports: day, month, year (integer)

Prompts for user input for day, month, and year, validifies and calls format_month to format month

Method format_month
Imports: None
Exports: month (integer)

Formats month to integer
```

# Modularity
```A description on how to run your production code with correct commands.
Sample output of running your production code. You must use screen shots to support your answer
in this section.
A brief explanation on how different modularity concepts is applied in your code.
Your review checklist, results of reviewing your production code using the review checklist,
with explanation on your results, and refactoring decisions.
Revised module descriptions resulted after refactoring, if any (after doing the part 3 of the
detailed description)```
```

### Instruction

The code can be run by running `python3 main.py`. The user interface will appear, prompting to choose a scenario to run. 

- Scenario A queries your birthday and outputs your generation, lucky number, animal, and check whether your lucky number is a master number or not.
- Scenario B queries two birthdays and outputs whether they have the same lucky number and animal or not.
- Scenario C queries your birthday and outputs the generation you belong to.

If your scenario selection input is invalid, it will prompt until you enter a correct input.
You need to rerun the code if you would like to try another scenario. 

![[code_running_instructions.png]]

# Black-box test cases
### Module calculator
#### Submodule calculate_lucky_number
##### Equivalence Partitioning
| No. | Category          | Input<br>birthday | Expected Output<br>lucky_number |
| --- | ----------------- | ----------------- | ------------------------------- |
| 1   | Not master number | = 10, 3, 2006     | 3                               |
| 2   | Master number     | = 6, 6, 2017      | 22                              |

#### Submodule get_lucky_animal
##### Equivalence Partitioning
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
##### Equivalence Partitioning
| No. | Category             | Input<br>year | Expected Output<br>generation |
| --- | -------------------- | ------------- | ----------------------------- |
| 1   | 1901 <= year <= 1945 | = 1930        | "Silent Generation"           |
| 2   | 1946 <= year <= 1964 | = 1950        | "Baby Boomers"                |
| 3   | 1965 <= year <= 1979 | = 1970        | "Generation X"                |
| 4   | 1980 <= year <= 1994 | = 1990        | "Millennials"                 |
| 5   | 1995 <= year <= 2009 | = 2000        | "Generation Z"                |
| 6   | 2010 <= year <= 2024 | = 2020        | "Generation Alpha"            |
##### Boundary Value Analysis
| No. | Category                         | Input<br>                  | Expected Output<br>generation         |
| --- | -------------------------------- | -------------------------- | ------------------------------------- |
| 1   | Silent Generation / Baby Boomers | year = 1945<br>year = 1946 | "Silent Generation"<br>"Baby Boomers" |
| 2   | Baby Boomers / Generation X      | year = 1964<br>year = 1965 | "Baby Boomers"<br>"Generation X"      |
| 3   | Generation X / Millennials       | year = 1979<br>year = 1980 | "Generation X"<br>"Millennials"       |
| 4   | Millennials / Generation Z       | year = 1994<br>year = 1995 | "Millennials"<br>"Generation Z"       |
| 5   | Generation Z / Generation Alpha  | year = 2009<br>year = 2010 | "Generation Z"<br>"Generation Alpha"  |

### Module logic
#### Submodule same_luck
##### Equivalence Partitioning
| No. | Category<br>                                                                 | Input<br>                                        | Expected Output<br>result |
| --- | ---------------------------------------------------------------------------- | ------------------------------------------------ | ------------------------- |
| 1   | Lucky number of birthday1 <br>is equal to <br>lucky number of birthday 2     | birthday1 = 9, 7, 2005<br>birthday2 = 8, 8, 2005 | True                      |
| 2   | Lucky number of birthday1 <br>is NOT equal to <br>lucky number of birthday 2 | birthday1 = 9, 7, 2005<br>birthday2 = 8, 9, 2005 | False                     |

#### Submodule is_master_number
##### Equivalence Partitioning
| No. | Category<br>lucky_number | Input<br>lucky_number | Expected Output<br>result |
| --- | ------------------------ | --------------------- | ------------------------- |
| 1   | == 11                    | = 11                  | True                      |
| 2   | == 22                    | = 22                  | True                      |
| 3   | == 33                    | = 33                  | True                      |
| 4   | != 11                    | = 20                  | False                     |
| 5   | != 22                    | = 14                  | False                     |
| 6   | != 33                    | = 43                  | False                     |

### Module data_structures
#### Class Date
#### Method prompt_date
##### Equivalence Partitioning
| No. | Category<br>                                                           | Input<br>                                  | Expected Output<br>result |
| --- | ---------------------------------------------------------------------- | ------------------------------------------ | ------------------------- |
| 1   | Day = 1-31, <br>Month = 1-12, <br>Year = 1901-2024 <br>(all inclusive) | day = 10<br>month = 3 <br>year = 2006      | (10, 3, 2006)             |
| 2   | String month                                                           | day = 10<br>month = "March"<br>year = 2006 | (10, 3, 2006)             |
| 3   | Invalid day                                                            | day = 0<br>month = 2<br>year = 2001        | ValueError                |
| 4   | Invalid month                                                          | day = 10<br>month = 0<br>year = 1999       | ValueError                |
| 5   | Invalid year                                                           | day = 20<br>month = 4<br>year = 9999       | ValueError                |
| 6   | Invalid day and month                                                  | day = -1<br>month = 0<br>year = 2024       | ValueError                |
| 7   | Invalid month and year                                                 | day = 4<br>month = 99<br>year = 2193       | ValueError                |
| 8   | Invalid day and year                                                   | day = 111<br>month = 12<br>year = 9        | ValueError                |
| 9   | Invalid day, month, and year                                           | day = 99<br>month = 99<br>year = 9999      | ValueError                |

#### Method format_month
##### Equivalence Partitioning
| No. | Category<br>                    | Input<br>month | Expected Output<br>month |
| --- | ------------------------------- | -------------- | ------------------------ |
| 1   | January                         | = "January"    | 1                        |
| 2   | Febuary                         | = "Febuary"    | 2                        |
| 3   | March                           | = "March"      | 3                        |
| 4   | April                           | = "April"      | 4                        |
| 5   | May                             | = "May"        | 5                        |
| 6   | June                            | = "June"       | 6                        |
| 7   | July                            | = "July"       | 7                        |
| 8   | August                          | = "August"     | 8                        |
| 9   | September                       | = "September"  | 9                        |
| 10  | October                         | = "October"    | 10                       |
| 11  | November                        | = "November"   | 11                       |
| 12  | December                        | = "December"   | 12                       |
| 13  | Jan                             | = "Jan"        | 1                        |
| 14  | Feb                             | = "Feb"        | 2                        |
| 15  | Mar                             | = "Mar"        | 3                        |
| 16  | Apr                             | = "Apr"        | 4                        |
| 17  | Jun                             | = "Jun"        | 6                        |
| 18  | Jul                             | = "Jul"        | 7                        |
| 19  | Aug                             | = "Aug"        | 8                        |
| 20  | Sep                             | = "Sep"        | 9                        |
| 21  | Sept                            | = "Sept"       | 9                        |
| 22  | Oct                             | = "Oct"        | 10                       |
| 23  | Nov                             | = "Nov"        | 11                       |
| 24  | Dec                             | = "Dec"        | 12                       |
| 25  | All lowercase                   | = "jan"        | 1                        |
| 26  | All uppercase                   | = "JAN"        | 1                        |
| 27  | String does not match any month | = "Jupiter"    | ValueError               |

# White-box test cases
`All test cases you have designed as the answer for part 5 of this assessment, produced in the
tubular format shown in lecture 10, brief explanation on your test design, and any
assumptions you made.`
# Test implementation and test execution
I have implemented test cases for each submodule in Black-Box Test Cases section. Most of test cases are in form of Equivalence Partitioning. One test case is in form of Boundary Value Analysis, which is submodule get_generation, which I deemed appropriate.

All test cases can be executed as follows,
```
python3 -m unittest
```

The result is that all test cases passed as expected.
![[unittest_passed.png]]
The debug processes can be seen in the Version Control section.

# Summary

| Module name            | BB (EP) | BB (EVA) | WB  | Data types            | Form of IO                                | EP   | BVA  | WB  |
| ---------------------- | ------- | -------- | --- | --------------------- | ----------------------------------------- | ---- | ---- | --- |
| calculate_lucky_number | Done    | -        |     | Date -> integer       | Input: <br>Keyboard<br>Output:<br>Return  | Done | -    |     |
| get_lucky_animal       | Done    | -        |     | integer -> string     | Input: <br>Parameter<br>Output:<br>Return | Done | -    |     |
| get_generation         | Done    | Done     |     | integer -> string     | Input: <br>Parameter<br>Output:<br>Return | Done | Done |     |
| same_luck              | Done    | -        |     | Date -> boolean       | Input: <br>Parameter<br>Output:<br>Return | Done | -    |     |
| is_master_number       | Done    | -        |     | integer -> boolean    | Input: <br>Parameter<br>Output:<br>Return | Done | -    |     |
| prompt_date            | Done    | -        |     | string<br>-> Date     | Input: <br>Keyboard<br>Output:<br>Return  | Done | -    |     |
| format_month           | Done    | -        |     | string <br>-> integer | Input: <br>Parameter<br>Output:<br>Return | Done | -    |     |
# Version control
`Log of the use of your version control system (image of the log is sufficient), any explanation/discussion on version control. (refer part 1 of the detailed description)`
# Discussion
`Reflect on your own work including summary of what you have achieved, challenges you have
faced, limitations and ways to improve your work with other features you have not considered, and
any other information you wish to present.`