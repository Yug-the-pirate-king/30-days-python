<div align="center">
  <h1>30 Days Of Python: Day 14 - Higher Order Functions</h1>
  <a class="header-badge" target="_blank" href="https://www.linkedin.com/in/asabeneh/">
    <img src="https://img.shields.io/badge/style--5eba00.svg?label=LinkedIn&logo=linkedin&style=social">
  </a>
  <a class="header-badge" target="_blank" href="https://twitter.com/Asabeneh">
    <img alt="Twitter Follow" src="https://img.shields.io/twitter/follow/asabeneh?style=social">
  </a>

  <sub>Author:
    <a href="https://www.linkedin.com/in/asabeneh/" target="_blank">Asabeneh Yetayeh</a><br>
    <small>Second Edition: July, 2021</small>
  </sub>
</div>

[<< Day 13](../13_Day_List_comprehension/13_list_comprehension.md) | [Day 15>>](../15_Day_Python_type_errors/15_python_type_errors.md)

![30DaysOfPython](../images/30DaysOfPython_banner3@2x.png)

- [📘 Day 14](#-day-14)
  - [Higher Order Functions](#higher-order-functions)
    - [Function as a Parameter](#function-as-a-parameter)
    - [Function as a Return Value](#function-as-a-return-value)
  - [Python Closures](#python-closures)
  - [Python Decorators](#python-decorators)
    - [Creating Decorators](#creating-decorators)
    - [Applying Multiple Decorators to a Single Function](#applying-multiple-decorators-to-a-single-function)
    - [Accepting Parameters in Decorator Functions](#accepting-parameters-in-decorator-functions)
  - [Built-in Higher Order Functions](#built-in-higher-order-functions)
    - [Python - Map Function](#python---map-function)
    - [Python - Filter Function](#python---filter-function)
    - [Python - Reduce Function](#python---reduce-function)
  - [💻 Exercises: Day 14](#-exercises-day-14)
    - [Exercises: Level 1](#exercises-level-1)
    - [Exercises: Level 2](#exercises-level-2)
    - [Exercises: Level 3](#exercises-level-3)

# 📘 Day 14

## Higher Order Functions

In Python, functions are treated as first-class citizens, allowing you to perform the following operations on functions:

- A function can take one or more functions as parameters.
- A function can be returned as a result of another function.
- A function can be modified.
- A function can be assigned to a variable.

In this section, we will cover:

1. Handling functions as parameters.
2. Returning functions as return values from other functions.
3. Using Python closures and decorators.

### Function as a Parameter

```py
def sum_numbers(nums):
    """Return the sum of a list of numbers."""
    return sum(nums)


def apply_function(func, data):
    """
    Higher-order function: applies *func* to *data* and returns the result.
    """
    return func(data)


result = apply_function(sum_numbers, [1, 2, 3, 4, 5])
print(result)       # 15
```

### Function as a Return Value

```py
def square(x):
    """Return the square of a number."""
    return x ** 2


def cube(x):
    """Return the cube of a number."""
    return x ** 3


def absolute(x):
    """Return the absolute value of a number."""
    return x if x >= 0 else -x


def build_function(operation):
    """
    Higher-order function that returns the requested arithmetic function.
    Raises ValueError for an unsupported operation.
    """
    if operation == 'square':
        return square
    if operation == 'cube':
        return cube
    if operation == 'absolute':
        return absolute

    raise ValueError(f"Unknown operation: {operation!r}")


result = build_function('square')
print(result(3))       # 9

result = build_function('cube')
print(result(3))       # 27

result = build_function('absolute')
print(result(-3))      # 3
```

You can see from the above example that the higher-order function returns different functions depending on the passed parameter.

## Python Closures

Python allows a nested function to access the outer scope of the enclosing function. This is known as a closure. A closure is created by nesting a function inside another function and then returning the inner function.

**Example:**

```py
def add_ten():
    ten = 10  # variable in the enclosing scope

    def add(num):
        # The inner function captures *ten* from the enclosing scope.
        return num + ten

    return add


closure_result = add_ten()
print(closure_result(5))   # 15
print(closure_result(10))  # 20
```

## Python Decorators

A decorator is a design pattern in Python that allows a user to add new functionality to an existing object without modifying its structure. Decorators are usually applied before the definition of the function you want to decorate.

### Creating Decorators

To create a decorator function, we need an outer function with an inner wrapper function.

**Example:**

```py
import functools


def uppercase_decorator(function):
    """Decorator that converts the wrapped function's result to uppercase."""
    @functools.wraps(function)  # preserves original function metadata
    def wrapper(*args, **kwargs):
        result = function(*args, **kwargs)
        return result.upper()

    return wrapper


# Applying the decorator manually
def greeting():
    return 'Welcome to Python'


greet = uppercase_decorator(greeting)
print(greet())          # WELCOME TO PYTHON


# Applying the decorator with @ syntax
@uppercase_decorator
def greeting():
    return 'Welcome to Python'


print(greeting())   # WELCOME TO PYTHON
```

### Applying Multiple Decorators to a Single Function

```py
import functools


def uppercase_decorator(function):
    @functools.wraps(function)
    def wrapper(*args, **kwargs):
        return function(*args, **kwargs).upper()
    return wrapper


def split_string_decorator(function):
    @functools.wraps(function)
    def wrapper(*args, **kwargs):
        return function(*args, **kwargs).split()
    return wrapper


# Decorators are applied bottom-up.
# uppercase_decorator runs first (produces a string),
# then split_string_decorator splits that string into a list.
@split_string_decorator
@uppercase_decorator
def greeting():
    return 'Welcome to Python'


print(greeting())   # ['WELCOME', 'TO', 'PYTHON']
```

### Accepting Parameters in Decorator Functions

Most of the time, we need our functions to take parameters, so we might need to define a decorator that accepts parameters.

```py
import functools


def decorator_with_parameters(function):
    @functools.wraps(function)
    def wrapper(*args, **kwargs):
        result = function(*args, **kwargs)

        # Extract the country argument whether it was passed positionally or by keyword.
        country = kwargs.get("country")
        if country is None and len(args) >= 3:
            country = args[2]

        if country:
            print(f"I live in {country}")

        return result

    return wrapper


@decorator_with_parameters
def print_full_name(first_name, last_name, country):
    print(f"I am {first_name} {last_name}. I love to teach.")


print_full_name("Asabeneh", "Yetayeh", "Finland")
```

## Built-in Higher Order Functions

Some of the built-in higher-order functions that we cover in this part are _map()_, _filter()_, and _reduce_().
Lambda functions can be passed as parameters, and the best use case for lambda functions is in functions like map, filter, and reduce.

### Python - Map Function

The `map()` function is a built-in function that takes a function and an iterable as parameters.

```py
# syntax
map(function, iterable)
```

**Example: 1**

```py
numbers = [1, 2, 3, 4, 5]  # iterable


def square(x):
    return x ** 2


# map() returns a lazy iterator; convert it to a list to see the values.
numbers_squared = map(square, numbers)
print(list(numbers_squared))    # [1, 4, 9, 16, 25]

# Using a lambda function for a concise, one-off transformation
numbers_squared = map(lambda x: x ** 2, numbers)
print(list(numbers_squared))    # [1, 4, 9, 16, 25]
```

**Example: 2**

```py
numbers_str = ['1', '2', '3', '4', '5']  # iterable

# int is applied to every element in the iterable.
numbers_int = map(int, numbers_str)
print(list(numbers_int))    # [1, 2, 3, 4, 5]
```

**Example: 3**

```py
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']  # iterable


def change_to_upper(name):
    return name.upper()


names_upper_cased = map(change_to_upper, names)
print(list(names_upper_cased))    # ['ASABENEH', 'LIDIYA', 'ERMIAS', 'ABRAHAM']

# Let us apply it with a lambda function
names_upper_cased = map(lambda name: name.upper(), names)
print(list(names_upper_cased))    # ['ASABENEH', 'LIDIYA', 'ERMIAS', 'ABRAHAM']
```

What `map()` actually does is iterate over a list, transform each item, and return a new iterator.

### Python - Filter Function

The `filter()` function calls the specified function, which returns a boolean, for each item of the specified iterable. It filters the items that satisfy the filtering criteria.

```py
# syntax
filter(function, iterable)
```

**Example: 1**

```py
# Let's filter only even numbers
numbers = [1, 2, 3, 4, 5]  # iterable


def is_even(num):
    return num % 2 == 0


even_numbers = filter(is_even, numbers)
print(list(even_numbers))       # [2, 4]
```

**Example: 2**

```py
numbers = [1, 2, 3, 4, 5]  # iterable


def is_odd(num):
    return num % 2 != 0


odd_numbers = filter(is_odd, numbers)
print(list(odd_numbers))       # [1, 3, 5]
```

**Example: 3**

```py
# Filter long names
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']  # iterable


def is_name_long(name):
    return len(name) > 7


long_names = filter(is_name_long, names)
print(list(long_names))         # ['Asabeneh']
```

### Python - Reduce Function

The `reduce()` function is defined in the `functools` module, so we import it from there. Like `map()` and `filter()`, it takes two parameters—a function and an iterable. However, it does not return another iterable; instead, it returns a single value.

**Example: 1**

```py
from functools import reduce

numbers_str = ['1', '2', '3', '4', '5']  # iterable


def add_two_nums(x, y):
    return int(x) + int(y)


total = reduce(add_two_nums, numbers_str)
print(total)    # 15
```

## 💻 Exercises: Day 14

```py
countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
```

### Exercises: Level 1

1. Explain the difference between map, filter, and reduce.
2. Explain the difference between higher-order function, closure, and decorator.
3. Define a callback function before using map, filter, or reduce. See examples.
4. Use a `for` loop to print each country in the `countries` list.
5. Use a `for` loop to print each name in the `names` list.
6. Use a `for` loop to print each number in the `numbers` list.

### Exercises: Level 2

1. Use `map` to create a new list by changing each country to uppercase in the `countries` list.
2. Use `map` to create a new list by changing each number to its square in the `numbers` list.
3. Use `map` to change each name to uppercase in the `names` list.
4. Use `filter` to filter out countries containing `'land'`.
5. Use `filter` to filter out countries having exactly six characters.
6. Use `filter` to filter out countries containing six letters or more in the country list.
7. Use `filter` to filter out countries starting with an `'E'`.
8. Chain two or more list iterators (e.g. `arr.map(callback).filter(callback).reduce(callback)`).
9. Declare a function called `get_string_lists` which takes a list as a parameter and then returns a list containing only string items.
10. Use `reduce` to sum all the numbers in the `numbers` list.
11. Use `reduce` to concatenate all the countries and produce this sentence:  
    _Estonia, Finland, Sweden, Denmark, Norway, and Iceland are north European countries_.
12. Declare a function called `categorize_countries` that returns a list of countries with some common pattern (you can find the [countries list](https://github.com/Asabeneh/30-Days-Of-Python/blob/master/data/countries.py) in this repository as `countries.js` (e.g. `'land'`, `'ia'`, `'island'`, `'stan'`)).
13. Create a function returning a dictionary, where keys stand for starting letters of countries and values are the number of country names starting with that letter.
14. Declare a `get_first_ten_countries` function - it returns a list of the first ten countries from the `countries.js` list in the data folder.
15. Declare a `get_last_ten_countries` function that returns the last ten countries in the countries list.

### Exercises: Level 3

1. Use the `countries_data.py` (https://github.com/Asabeneh/30-Days-Of-Python/blob/master/data/countries-data.py) file and follow the tasks below:
   - Sort countries by name, by capital, by population.
   - Sort out the ten most spoken languages by location.
   - Sort out the ten most populated countries.

🎉 CONGRATULATIONS ! 🎉

[<< Day 13](../13_Day_List_comprehension/13_list_comprehension.md) | [Day 15>>](../15_Day_Python_type_errors/15_python_type_errors.md)