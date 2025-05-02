# Cover page
`Include the assessment name, your name as in Moodle, Curtin student ID, practical class (date/
time). This may not be in a separate page, but as the first thing in your document in a clear
format.`
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
Imports: day (integer), month (integer or string), year (integer)

Stores day, month, year in integer format

Method format_month
import: None
export: month (integer)

Formats month to integer
```

# Modularity
`A description on how to run your production code with correct commands.
Sample output of running your production code. You must use screen shots to support your answer
in this section.
A brief explanation on how different modularity concepts is applied in your code.
Your review checklist, results of reviewing your production code using the review checklist,
with explanation on your results, and refactoring decisions.
Revised module descriptions resulted after refactoring, if any (after doing the part 3 of the
detailed description)`
# Black-box test cases
### Module calculator
#### Submodule calculate_lucky_number
| No. | Category          | Input<br>birthday | Expected Output<br>lucky_number |
| --- | ----------------- | ----------------- | ------------------------------- |
| 1   | Not master number | Date(10, 3, 2006) | 3                               |
| 2   | Master number     | Date(6, 6, 2017)  | 22                              |


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
### Module logic
#### Submodule same_luck
| No. | Category<br>                                                                 | Input<br>                                                        | Expected Output<br>result |
| --- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------- | ------------------------- |
| 1   | Lucky number of birthday1 <br>is equal to <br>lucky number of birthday 2     | birthday1 = Date(09, 07, 2005)<br>birthday2 = Date(08, 08, 2005) | True                      |
| 2   | Lucky number of birthday1 <br>is NOT equal to <br>lucky number of birthday 2 | birthday1 = Date(09, 07, 2005)<br>birthday2 = Date(08, 09, 2005) | False                     |
#### Submodule is_master_number
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
#### Constructor

| No. | Category<br>                                                           | Input<br>                                  | Expected Output<br>result |
| --- | ---------------------------------------------------------------------- | ------------------------------------------ | ------------------------- |
| 1   | Day = 1-31, <br>Month = 1-12, <br>Year = 1901-2024 <br>(all inclusive) | day = 10<br>month = 3 <br>year = 2006      | None                      |
| 2   | String month                                                           | day = 10<br>month = "March"<br>year = 2006 | None                      |
| 3   | Invalid day                                                            | day = 0<br>month = 2<br>year = 2001        | ValueError                |
| 4   | Invalid month                                                          | day = 10<br>month = 0<br>year = 1999       | ValueError                |
| 5   | Invalid year                                                           | day = 20<br>month = 4<br>year = 9999       | ValueError                |
| 6   | Invalid day and month                                                  | day = -1<br>month = 0<br>year = 2024       | ValueError                |
| 7   | Invalid month and year                                                 | day = 4<br>month = 99<br>year = 2193       | ValueError                |
| 8   | Invalid day and year                                                   | day = 111<br>month = 12<br>year = 9        | ValueError                |
| 9   | Invalid day, month, and year                                           | day = 99<br>month = 99<br>year = 9999      | ValueError                |

#### Method format_month
| No. | Category<br> | Input<br>month | Expected Output<br>month |
| --- | ------------ | -------------- | ------------------------ |
| 1   | January      | = "January"    | 1                        |
| 2   | Febuary      | = "Febuary"    | 2                        |
| 3   | March        | = "March"      | 3                        |
| 4   | April        | = "April"      | 4                        |
| 5   | May          | = "May"        | 5                        |
| 6   | June         | = "June"       | 6                        |
| 7   | July         | = "July"       | 7                        |
| 8   | August       | = "August"     | 8                        |
| 9   | September    | = "September"  | 9                        |
| 10  | October      | = "October"    | 10                       |
| 11  | November     | = "November"   | 11                       |
| 12  | December     | = "December"   | 12                       |
| 13  | Jan          | = "Jan"        | 1                        |
| 14  | Feb          | = "Feb"        | 2                        |
| 15  | Mar          | = "Mar"        | 3                        |
| 16  | Apr          | = "Apr"        | 4                        |
| 17  | Jun          | = "Jun"        | 6                        |
| 18  | Jul          | = "Jul"        | 7                        |
| 19  | Aug          | = "Aug"        | 8                        |
| 20  | Sep          | = "Sep"        | 9                        |
| 21  | Sept         | = "Sept"       | 9                        |
| 22  | Oct          | = "Oct"        | 10                       |
| 23  | Nov          | = "Nov"        | 11                       |
| 24  | Dec          | = "Dec"        | 12                       |

# White-box test cases
`All test cases you have designed as the answer for part 5 of this assessment, produced in the
tubular format shown in lecture 10, brief explanation on your test design, and any
assumptions you made.`
# Test implementation and test execution
`A brief description of how to run your test code with correct commands.
Results of test execution with outputs of test successes and failures, with short discussion
of results/improvements from part 5 of this assessment.`
# Summary
`Table you have produced in the part 6 of this assessment.`
# Version control
`Log of the use of your version control system (image of the log is sufficient), any explanation/discussion on version control. (refer part 1 of the detailed description)`
# Discussion
`Reflect on your own work including summary of what you have achieved, challenges you have
faced, limitations and ways to improve your work with other features you have not considered, and
any other information you wish to present.`