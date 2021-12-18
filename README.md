# sorting-tuples
Sort Name, Age, Score in ascending order

### Example for console input and importing as module

```Python
>>> from test import sorting
>>> a = [('Tommy', 19, 80), ('John', 20, 90), ('Jony', 17, 91), ('Jony', 17, 93), ('Json', 21, 85)]
>>> sorting(a)
Unsorted Inputs: [('Tommy', 19, 80), ('John', 20, 90), ('Jony', 17, 91), ('Jony', 17, 93), ('Json', 21, 85)]
Sorted Inputs: [('John', 20, 90), ('Jony', 17, 91), ('Jony', 17, 93), ('Json', 21, 85), ('Tommy', 19, 80)]
```

### Example for running from command line
```
(base) rashedul@Mds-MacBook-Pro Algocyte-Dev-AWS % python test.py
Set the total number of tuples to insert in integer: 3
Add comma seperated Name(String),Age (Int),Score (Int): abrar,20,15
Add comma seperated Name(String),Age (Int),Score (Int): Abrar,25,14
Add comma seperated Name(String),Age (Int),Score (Int): Abrar,14,80
Unsorted Inputs: [('abrar', 20, 15), ('Abrar', 25, 14), ('Abrar', 14, 80)]
Sorted Inputs: [('Abrar', 14, 80), ('Abrar', 25, 14), ('abrar', 20, 15)]
(base) rashedul@Mds-MacBook-Pro Algocyte-Dev-AWS % python test.py
Set the total number of tuples to insert in integer: 5
Add comma seperated Name(String),Age (Int),Score (Int): Tommy,19,80
Add comma seperated Name(String),Age (Int),Score (Int): John,20,90
Add comma seperated Name(String),Age (Int),Score (Int): Jony,17,91
Add comma seperated Name(String),Age (Int),Score (Int): Jony,17,93
Add comma seperated Name(String),Age (Int),Score (Int): Json,21,85
Unsorted Inputs: [('Tommy', 19, 80), ('John', 20, 90), ('Jony', 17, 91), ('Jony', 17, 93), ('Json', 21, 85)]
Sorted Inputs: [('John', 20, 90), ('Jony', 17, 91), ('Jony', 17, 93), ('Json', 21, 85), ('Tommy', 19, 80)]
```