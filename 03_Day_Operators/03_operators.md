<div align="center">
  <h1> 30 Days Of Python: Day 3 - Operators</h1>
  <a class="header-badge" target="_blank" href="https://www.linkedin.com/in/asabeneh/">
  <img src="https://img.shields.io/badge/style--5eba00.svg?label=LinkedIn&logo=linkedin&style=social">
  </a>
  <a class="header-badge" target="_blank" href="https://twitter.com/Asabeneh">
  <img alt="Twitter Follow" src="https://img.shields.io/twitter/follow/asabeneh?style=social">
  </a>

<sub>Author:
<a href="https://www.linkedin.com/in/asabeneh/" target="_blank">Asabeneh Yetayeh</a><br>
<small> Second Edition: July, 2021</small>
</sub>
</div>

[<< Day 2](../02_Day_Variables_builtin_functions/02_variables_builtin_functions.md) | [Day 4 >>](../04_Day_Strings/04_strings.md)

![30DaysOfPython](../images/30DaysOfPython_banner3@2x.png)

- [📘 Day 3](#-day-3)
  - [Boolean](#boolean)
  - [Operators](#operators)
    - [Assignment Operators](#assignment-operators)
    - [Arithmetic Operators:](#arithmetic-operators)
    - [Comparison Operators](#comparison-operators)
    - [Logical Operators](#logical-operators)
  - [💻 Exercises - Day 3](#-exercises---day-3)

# 📘 Day 3

## Boolean

A boolean data type represents one of the two values: _True_ or _False_. The use of these data types will be clear once we start using the comparison operator. The first letter **T** for True and **F** for False should be capital unlike JavaScript.
**Example: Boolean Values**

```py
print(True)
print(False)
```

## Operators

Python language supports several types of operators. In this section, we will focus on a few of them.

### Assignment Operators

Assignment operators are used to assign values to variables. Let us take = as an example. Equal sign in mathematics shows that two values are equal, however in Python it means we are storing a value in a certain variable and we call it assignment or assigning value to a variable. The table below shows the different types of python assignment operators, taken from [w3school](https://www.w3schools.com/python/python_operators.asp).

![Assignment Operators](../images/assignment_operators.png)

### Arithmetic Operators:

- Addition(+): a + b
- Subtraction(-): a - b
- Multiplication(*): a * b
- Division(/): a / b
- Modulus(%): a % b
- Floor division(//): a // b
- Exponentiation(**): a ** b

![Arithmetic Operators](../images/arithmetic_operators.png)

**Example:Integers**

```py
# Arithmetic Operations in Python
# Integers

def show_operation(name, value):
    print(f'{name}: {value}')

show_operation('Addition', 1 + 2)                           # 3
show_operation('Subtraction', 2 - 1)                      # 1
show_operation('Multiplication', 2 * 3)                   # 6
show_operation('Division', 4 / 2)                         # 2.0  Division in Python gives floating number
show_operation('Division', 6 / 2)                         # 3.0
show_operation('Division', 7 / 2)                         # 3.5
show_operation('Division without the remainder', 7 // 2)  # 3,  gives without the floating number or without the remaining
show_operation('Division without the remainder', 7 // 3)  # 2
show_operation('Modulus', 3 % 2)                          # 1, Gives the remainder
show_operation('Exponentiation', 2 ** 3)                  # 8 it means 2 * 2 * 2
```

**Example:Floats**

```py
# Floating numbers
print(f'Floating Point Number, PI {3.14}')
print(f'Floating Point Number, gravity {9.81}')
```

**Example:Complex numbers**

```py
# Complex numbers
print(f'Complex number: {1 + 1j}')
print(f'Multiplying complex numbers: {(1 + 1j) * (1 - 1j)}')
```

Let's declare a variable and assign a number data type. I am going to use single character variable but remember do not develop a habit of declaring such types of variables. Variable names should be all the time mnemonic.

**Example:**

```python
# Declaring the variable at the top first

a = 3 # a is a variable name and 3 is an integer data type
b = 2 # b is a variable name and 3 is an integer data type

def show_result(label, value):
    print(f'{label} = {value}')

# Arithmetic operations and assigning the result to a variable
total = a + b
diff = a - b
product = a * b
division = a / b
remainder = a % b
floor_division = a // b
exponential = a ** b

# I should have used sum instead of total but sum is a built-in function - try to avoid overriding built-in functions
print(total) # if you do not label your print with some string, you never know where the result is coming from
show_result('a + b', total)
show_result('a - b', diff)
show_result('a * b', product)
show_result('a / b', division)
show_result('a % b', remainder)
show_result('a // b', floor_division)
show_result('a ** b', exponential)
```

**Example:**

```py
print('== Addition, Subtraction, Multiplication, Division, Modulus ==')

def show_result(label, value):
    print(f'{label}: {value}')

# Declaring values and organizing them together
num_one = 3
num_two = 4

# Arithmetic operations
total = num_one + num_two
diff = num_two - num_one
product = num_one * num_two
div = num_two / num_one
remainder = num_two % num_one

# Printing values with label
show_result('total', total)
show_result('difference', diff)
show_result('product', product)
show_result('division', div)
show_result('remainder', remainder)
```

Let us start connecting the dots and start making use of what we already know to calculate (area, volume,density,  weight, perimeter, distance, force).

**Example:**

```py
PI = 3.14

def circle_area(radius):
    return PI * radius ** 2

def rectangle_area(length, width):
    return length * width

def calculate_weight(mass, gravity):
    return mass * gravity

def calculate_density(mass, volume):
    return mass / volume

# Calculating area of a circle
radius = 10
area_of_circle = circle_area(radius)
print(f'Area of a circle: {area_of_circle}')

# Calculating area of a rectangle
length = 10
width = 20
area_of_rectangle = rectangle_area(length, width)
print(f'Area of rectangle: {area_of_rectangle}')

# Calculating a weight of an object
mass = 75
gravity = 9.81
weight = calculate_weight(mass, gravity)
print(f'{weight} N')

# Calculate the density of a liquid
mass = 75 # in Kg
volume = 0.075 # in cubic meter
density = calculate_density(mass, volume) # 1000 Kg/m^3
```

### Comparison Operators

In programming we compare values, we use comparison operators to compare two values. We check if a value is greater or less or equal to other value. The following table shows Python comparison operators which was taken from [w3school](https://www.w3schools.com/python/python_operators.asp).

![Comparison Operators](../images/comparison_operators.png)
**Example: Comparison Operators**

```py
print(3 > 2)     # True, because 3 is greater than 2
print(3 >= 2)    # True, because 3 is greater than 2
print(3 < 2)     # False,  because 3 is greater than 2
print(2 < 3)     # True, because 2 is less than 3
print(2 <= 3)    # True, because 2 is less than 3
print(3 == 2)    # False, because 3 is not equal to 2
print(3 != 2)    # True, because 3 is not equal to 2

def compare_lengths(first, second, operator):
    if operator == '==':
        return len(first) == len(second)
    if operator == '!=':
        return len(first) != len(second)
    if operator == '<':
        return len(first) < len(second)
    if operator == '>':
        return len(first) > len(second)
    return False

print(compare_lengths('mango', 'avocado', '=='))  # False
print(compare_lengths('mango', 'avocado', '!='))  # True
print(compare_lengths('mango', 'avocado', '<'))   # True
print(compare_lengths('milk', 'meat', '!='))      # False
print(compare_lengths('milk', 'meat', '=='))      # True
print(compare_lengths('tomato', 'potato', '=='))  # True
print(compare_lengths('python', 'dragon', '>'))   # False

# Comparing something gives either a True or False

print(f'True == True: {True == True}')
print(f'True == False: {True == False}')
print(f'False == False: {False == False}')
```

In addition to the above comparison operator Python uses:

- _is_: Returns true if both variables are the same object(x is y)
- _is not_: Returns true if both variables are not the same object(x is not y)
- _in_: Returns True if the queried list contains a certain item(x in y)
- _not in_: Returns True if the queried list doesn't have a certain item(x in y)

```py
print(f'1 is 1: {1 is 1}')
print(f'1 is not 2: {1 is not 2}')
print(f'A in Asabeneh: {"A" in "Asabeneh"}')
print(f'B in Asabeneh: {"B" in "Asabeneh"}')
print(f'coding in coding for all: {"coding" in "coding for all"}')
print(f'a in an: {"a" in "an"}')
print(f'4 is 2 ** 2: {4 is 2 ** 2}')
```

### Logical Operators

Unlike other programming languages python uses keywords _and_, _or_ and _not_ for logical operators. Logical operators are used to combine conditional statements:

![Logical Operators](../images/logical_operators.png)

```py
print(3 > 2 and 4 > 3) # True - because both statements are true
print(3 > 2 and 4 < 3) # False - because the second statement is false
print(3 < 2 and 4 < 3) # False - because both statements are false
print(f'True and True: {True and True}')
print(3 > 2 or 4 > 3)  # True - because both statements are true
print(3 > 2 or 4 < 3)  # True - because one of the statements is true
print(3 < 2 or 4 < 3)  # False - because both statements are false
print(f'True or False: {True or False}')
print(not 3 > 2)     # False - because 3 > 2 is true, then not True gives False
print(not True)      # False - Negation, the not operator turns true to false
print(not False)     # True
print(not not True)  # True
print(not not False) # False
```

🌕 You have boundless energy. You have just completed day 3 challenges and you are three steps ahead on your way to greatness. Now do some exercises for your brain and your muscles.

## 💻 Exercises - Day 3

1. Declare your age as integer variable
2. Declare your height as a float variable
3. Declare a variable that store a complex number
4. Write a script that prompts the user to enter base and height of the triangle and calculate an area of this triangle (area = 0.5 x b x h).

```py
    Enter base: 20
    Enter height: 10
    The area of the triangle is 100
```

5. Write a script that prompts the user to enter side a, side b, and side c of the triangle. Calculate the perimeter of the triangle (perimeter = a + b + c).

```py
Enter side a: 5
Enter side b: 4
Enter side c: 3
The perimeter of the triangle is 12
```

6. Get length and width of a rectangle using prompt. Calculate its area (area = length x width) and perimeter (perimeter = 2 x (length + width))
7. Get radius of a circle using prompt. Calculate the area (area = pi x r x r) and circumference (c = 2 x pi x r) where pi = 3.14.
8. Calculate the slope, x-intercept and y-intercept of y = 2x -2
9. Slope is (m = y2-y1/x2-x1). Find the slope and [Euclidean distance](https://en.wikipedia.org/wiki/Euclidean_distance#:~:text=In%20mathematics%2C%20the%20Euclidean%20distance,being%20called%20the%20Pythagorean%20distance.) between point (2, 2) and point (6,10) 
10. Compare the slopes in tasks 8 and 9.
11. Calculate the value of y (y = x^2 + 6x + 9). Try to use different x values and figure out at what x value y is going to be 0.
12. Find the length of 'python' and 'dragon' and make a falsy comparison statement.
13. Use _and_ operator to check if 'on' is found in both 'python' and 'dragon'
14. _I hope this course is not full of jargon_. Use _in_ operator to check if _jargon_ is in the sentence.
15. There is no 'on' in both dragon and python
16. Find the length of the text _python_ and convert the value to float and convert it to string
17. Even numbers are divisible by 2 and the remainder is zero. How do you check if a number is even or not using python?
18. Check if the floor division of 7 by 3 is equal to the int converted value of 2.7.
19. Check if type of '10' is equal to type of 10
20. Check if int('9.8') is equal to 10
21. Writ a script that prompts the user to enter hours and rate per hour. Calculate pay of the person?

```py
Enter hours: 40
Enter rate per hour: 28
Your weekly earning is 1120
```

22. Write a script that prompts the user to enter number of years. Calculate the number of seconds a person can live. Assume a person can live hundred years

```py
Enter number of years you have lived: 100
You have lived for 3153600000 seconds.
```

23. Write a Python script that displays the following table

```py
1 1 1 1 1
2 1 2 4 8
3 1 3 9 27
4 1 4 16 64
5 1 5 25 125
```

🎉 CONGRATULATIONS ! 🎉

[<< Day 2](../02_Day_Variables_builtin_functions/02_variables_builtin_functions.md) | [Day 4 >>](../04_Day_Strings/04_strings.md)