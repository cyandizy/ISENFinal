# Cover page


### Assignment
#### By Komes Pispol 90035701
#### Class Tuesday, 9:00 AM


# Introduction

I have developed a tool specialized in birthday and numerology. This application is capable of calculating a lucky number from given date and a lucky number can be translated to its respective lucky animal. It is useful for telling fortune and whether two persons are compatible with the use of lucky number and animal. This tool is also able to identify which generation a person belong to by checking their birthday against generation map. It has  a command line interface that allows users to interact with the program easily. 

# Module descriptions
## Module calculator

```
Submodule calculate_lucky_number
Imports: birthday (Date)
Exports: lucky_number (integer)

Calculates lucky number by receiving birthday from argument. Once calculated, the lucky number is output through return value.
```

```
Submodule get_lucky_animal
Imports: lucky_number (integer)
Exports: lucky_animal (string)

Calculates lucky animal by receiving a lucky number as an argument and comparing it to a dictionary of lucky number to lucky animals. It outputs by returning the value. 
```

```
Submodule get_generation
Imports: year (integer)
Exports: generation (string)

Calculates generation of a birthday by receiving year as an argument and comparing it to a set of conditions. It returns generation as output.
```

## Module logic

```
Submodule same_luck
Imports: birthday1 (Date), birthday2 (Date)
Exports: result (boolean)

Checks if two dates have the same lucky number and lucky animal by receiving birthday1 and birthday2 as arguments, then call calculate_lucky_number for each birthday and compare the results. It returns True if both have the same lucky number, and False if not.
```

```
Submodule is_master_number
Imports: lucky_number (integer)
Exports: result (boolean)

Checks if a lucky number is a master number by receiving lucky number as argument and check if the number is in the list of master numbers of not. If it is in the list, return True. If it is not, return False.
```

## Module date

```
Class Date
Imports: None

Stores day, month, year in integer format.
```

```
Method prompt_date
Imports: None
Exports: None

Prompts for user input for day, month, and year, validifies if they are in correct formats and calls format_month to format month if month is not a digit. Finally, it modifies class members day, month, year with new values.
```

```
Method format_month
Imports: None
Exports: month (integer)

Formats month to integer by using a dictionary that maps month strings to integers and return the integer. 
```

### Explanation

I have designed so that each submodule satisfies each requirement without doing too many things at once in the same submodule. Each module only contains submodule with related functionalities for scalability.

### Assumptions

It is assumed that, in `get_generation()`, `year` is passed from a `Date()` object, meaning the input type is automatically validated. This means that in order to use    
`get_generation()`, you need to create a `Date()` object and call `prompt_date()` to take in inputs.

# Modularity
### Instructions

The code can be run by running `python3 main.py`. The user interface will appear, prompting to choose a scenario to run. 

- Scenario A queries your birthday and outputs your generation, lucky number, animal, and check whether your lucky number is a master number or not.
- Scenario B queries two birthdays and outputs whether they have the same lucky number and animal or not.
- Scenario C queries your birthday and outputs the generation you belong to.

If your scenario selection input is invalid, it will prompt until you enter a correct input.
You need to rerun the code if you would like to try another scenario. 

![[code_running_instructions_1.png]]
![[code_running_instructions_2.png]]
![[code_running_instructions_3.png]]
### Modularity Checklist
| No. | Question                        | Yes/No | Where |
| --- | ------------------------------- | ------ | ----- |
|     | **Coupling**                    |        |       |
| 1   | More than 6 function parameters | No     |       |
| 2   | Global variables                | No     |       |
| 3   | Control flags                   | No     |       |
|     | **Cohesion**                    |        |       |
| 4   | Sequential tasks                | No     |       |
| 5   | Different kinds of data         | No     |       |
|     | **Redundancy**                  |        |       |
| 6   | Duplication                     | No     |       |
| 7   | Supersets                       | No     |       |

In the code shows that each submodule only does what it is meant to do, which shows separation of concern. However, a submodule can also call other modules to help complete its task to avoid Redundancy when two submodule has a similar sub-task. For example, `calculate_lucky_number()` makes use `is_master_number()` as a part of its calculation while `is_master_number()` can also be used elsewhere, which is user interface in this case.
Each module is designed with modularity in mind from the beginning to avoid too many refactoring.

# Black-box test cases
### Module calculator
#### Submodule calculate_lucky_number
##### Equivalence Partitioning
| No. | Category          | Input<br>birthday   | Expected Output<br>lucky_number |
| --- | ----------------- | ------------------- | ------------------------------- |
| 1   | Not master number | = Date(10, 3, 2006) | 3                               |
| 2   | Master number     | = Date(6, 6, 2017)  | 22                              |

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

### Module date
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
| 2   | February                        | = "February"   | 2                        |
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
### Module calculator
#### Submodule calculate_lucky_number
| No. | Path            | Test Data                    | Expected Output   |
| --- | --------------- | ---------------------------- | ----------------- |
| 1.  | Do not enter if | birthday = Date(10, 3, 2006) | lucky_number = 3  |
| 2.  | Enter if        | birthday = Date(6, 6, 2017)  | lucky_number = 22 |

### Module date
#### Method prompt_date
| No. | Path<br>                                       | Test Data                                   | Expected Output |
| --- | ---------------------------------------------- | ------------------------------------------- | --------------- |
| 1   | Enter first if, do not enter second if         | day = 10<br>month = "march" <br>year = 2006 | (10, 3, 2006)   |
| 2   | Enter first if, enter second if                | day = 44<br>month = "april"<br>year = 2006  | ValueError      |
| 3   | Enter 1st if, enter 2nd else of 2nd if         | day = 14<br>month = "may"<br>year = 200     | ValueError      |
| 4   | Enter else of 1st if, do not enter second if   | day = 12<br>month = 9<br>year = 2004        | (12, 9, 2004)   |
| 5   | Enter else of 1st if, enter 2nd if             | day = -1<br>month = 4<br>year = 2024        | ValueError      |
| 6   | Enter else of 1st if, enter 1st else of 2nd if | day = 4<br>month = 99<br>year = 1945        | ValueError      |
| 7   | Enter else of 1st if, enter 2nd else of 2nd if | day = 9<br>month = 12<br>year = 2174        | ValueError      |


# Test implementation and test execution

I have implemented test cases for each submodule in Black-Box Test Cases section. Most of test cases are in form of Equivalence Partitioning. One test case is in form of Boundary Value Analysis, which is submodule `get_generation()`, which I deemed appropriate.

As for White-Box testing, I have chosen `calculate_lucky_number()` and `prompt_date()`
as their paths affect their processes.

All test cases can be executed as follows,
```
python3 -m unittest
```
Note that this command needs to be executed inside `code/` directory

The result is that all test cases passed as expected.
![[unittest_passed.png]]
The debug processes can be seen in the Version Control section.

# Traceability Matrix
### Design | Implementation

| Module name            | BB (EP) | BB (BVA) | WB   | Data types            | Form of IO                                                  | EP   | BVA  | WB   |
| ---------------------- | ------- | -------- | ---- | --------------------- | ----------------------------------------------------------- | ---- | ---- | ---- |
| calculate_lucky_number | Done    | -        | Done | Date -> integer       | Input: <br>Parameter<br>Output:<br>Return                   | Done | -    | Done |
| get_lucky_animal       | Done    | -        | -    | integer -> string     | Input: <br>Parameter<br>Output:<br>Return                   | Done | -    | -    |
| get_generation         | Done    | Done     | -    | integer -> string     | Input: <br>Parameter<br>Output:<br>Return                   | Done | Done | -    |
| same_luck              | Done    | -        | -    | Date -> boolean       | Input: <br>Parameter<br>Output:<br>Return                   | Done | -    | -    |
| is_master_number       | Done    | -        | -    | integer -> boolean    | Input: <br>Parameter<br>Output:<br>Return                   | Done | -    | -    |
| prompt_date            | Done    | -        | Done | string<br>-> Date     | Input: <br>Keyboard<br>Output:<br>Class member modification | Done | -    | Done |
| format_month           | Done    | -        | -    | string <br>-> integer | Input: <br>Parameter<br>Output:<br>Return                   | Done | -    | -    |
# Version control
`Log of the use of your version control system (image of the log is sufficient), any explanation/discussion on version control. (refer part 1 of the detailed description)`
# Discussion

I started this project by writing module descriptions in order to develop black box test cases first and foremost. With that, I have experienced test-driven development for the first time. It is convenience that each implementation can immediately be verified whether it is working as intended or not, using Black-Box test cases. However, the module design had improved over time, leading to modification of test cases and documentation. This in turn led to multiple context switching, having to switch branches every few modifications, which is tedious for a solo development. 

I believe that my work flow would be better if I had understood every requirement at the beginning. There were times that I would misunderstand a requirement halfway and had to rewrite every part, including report, test code, and production code. Some changes led to chain reactions that I had to apply the change I made on one submodule and a few other modules. But ultimately, I had to change the code back when I had finally understood the requirement because I couldn't use `git reset` when I have already made new features over the misunderstood changes. This taught me that branches should not be defined from start but should be created as I need, so that `git reset` can actually be useful. 

In the end, this assignment effectively taught me how to use git version control effectively, how to use merge, and when to branch.