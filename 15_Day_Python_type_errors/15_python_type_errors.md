<div align="center">
  <h1> 30 Days Of Python: Day 15 - Python Type Errors </h1>
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
</div>

[<< Day 14](../14_Day_Higher_order_functions/14_higher_order_functions.md) | [Day 16 >>](../16_Day_Python_date_time/16_python_datetime.md)

![30DaysOfPython](../images/30DaysOfPython_banner3@2x.png)
- [📘 Day 15](#-day-15)
  - [Python Error Types](#python-error-types)
    - [SyntaxError](#syntaxerror)
    - [NameError](#nameerror)
    - [IndexError](#indexerror)
    - [ModuleNotFoundError](#modulenotfounderror)
    - [AttributeError](#attributeerror)
    - [KeyError](#keyerror)
    - [TypeError](#typeerror)
    - [ImportError](#importerror)
    - [ValueError](#valueerror)
    - [ZeroDivisionError](#zerodivisionerror)
  - [💻 Exercises: Day 15](#-exercises-day-15)

# 📘 Day 15

## Python Error Types

When we write code it is common that we make a typo or some other common error. If our code fails to run, the Python interpreter will display a message, containing feedback with information on where the problem occurs and the type of an error. It will also sometimes gives us suggestions on a possible fix. Understanding different types of errors in programming languages will help us to debug our code quickly and also it makes us better at what we do.

Let us see the most common error types one by one. First let us open our Python interactive shell. Go to your you computer terminal and write 'python'. The python interactive shell will be opened.

### Reusable error-handling helpers

The examples below use a small set of helper functions. Centralising error handling, input validation, and repeated logic keeps the snippets concise and robust.

```py
from __future__ import annotations
import types
from typing import Any, Callable


def run_example(label: str, func: Callable, *args, **kwargs) -> Any:
    """Run a snippet, catch any exception, and print the result or error."""
    print(f">>> {label}")
    try:
        result = func(*args, **kwargs)
        if result is not None:
            print(result)
        return result
    except Exception as exc:
        print(f"{type(exc).__name__}: {exc}")
        return None


def resolve_name(name: str, namespace: dict | None = None) -> Any:
    """Look up a name in a namespace, raising NameError when missing."""
    if not isinstance(name, str) or not name:
        raise ValueError("name must be a non-empty string")
    namespace = namespace or globals()
    if name not in namespace:
        raise NameError(f"name {name!r} is not defined")
    return namespace[name]


def safe_import(module_name: str) -> Any:
    """Import a module, validating the name and preserving ModuleNotFoundError."""
    if not isinstance(module_name, str) or not module_name:
        raise ValueError("module_name must be a non-empty string")
    try:
        return __import__(module_name, fromlist=[""])
    except ModuleNotFoundError as exc:
        raise ModuleNotFoundError(f"No module named {module_name}") from exc


def safe_import_from(module_name: str, name: str) -> Any:
    """Import a name from a module, raising ImportError when it does not exist."""
    if not isinstance(name, str) or not name:
        raise ValueError("name must be a non-empty string")
    module = safe_import(module_name)
    if not hasattr(module, name):
        raise ImportError(f"cannot import name {name!r} from {module_name!r}")
    return getattr(module, name)


def safe_getattr(obj: Any, attr: str) -> Any:
    """Get an attribute, raising AttributeError with the standard message."""
    if not isinstance(attr, str) or not attr:
        raise ValueError("attr must be a non-empty string")
    if not hasattr(obj, attr):
        if isinstance(obj, types.ModuleType):
            raise AttributeError(f"module {obj.__name__!r} has no attribute {attr!r}")
        raise AttributeError(f"{type(obj).__name__!r} object has no attribute {attr!r}")
    return getattr(obj, attr)


def safe_get(mapping: dict, key: Any) -> Any:
    """Return a dictionary value, raising KeyError for missing keys."""
    if not isinstance(mapping, dict):
        raise TypeError("mapping must be a dict")
    if key not in mapping:
        raise KeyError(key)
    return mapping[key]


def safe_index(sequence, index: int) -> Any:
    """Return sequence[index], raising IndexError when out of range."""
    if not isinstance(index, int):
        raise TypeError("index must be an integer")
    if not -len(sequence) <= index < len(sequence):
        raise IndexError(f"{type(sequence).__name__} index out of range")
    return sequence[index]


def safe_add(a: Any, b: Any) -> Any:
    """Add two numeric values after type validation."""
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError(
            f"unsupported operand type(s) for +: '{type(a).__name__}' and '{type(b).__name__}'"
        )
    return a + b


def safe_int(value: Any, base: int = 10) -> int:
    """Convert a value to int, preserving ValueError and its standard message."""
    if not isinstance(base, int):
        raise TypeError("base must be an integer")
    try:
        return int(value, base)
    except ValueError as exc:
        raise ValueError(f"invalid literal for int() with base {base}: {value!r}") from exc


def safe_divide(a: Any, b: Any) -> float:
    """Divide two numbers after validating inputs and the divisor."""
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("both operands must be numbers")
    if b == 0:
        raise ZeroDivisionError("division by zero")
    return a / b
```

### SyntaxError

**Example 1: SyntaxError**

```py
asabeneh@Asabeneh:~$ python
Python 3.9.6 (default, Jun 28 2021, 15:26:21)
[Clang 11.0.0 (clang-1100.0.33.8)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> print 'hello world'
  File "<stdin>", line 1
    print 'hello world'
                      ^
SyntaxError: Missing parentheses in call to 'print'. Did you mean print('hello world')?
>>>
```

As you can see we made a syntax error because we forgot to enclose the string with parenthesis and Python already suggests the solution. Let us fix it.

```py
asabeneh@Asabeneh:~$ python
Python 3.9.6 (default, Jun 28 2021, 15:26:21)
[Clang 11.0.0 (clang-1100.0.33.8)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> print 'hello world'
  File "<stdin>", line 1
    print 'hello world'
                      ^
SyntaxError: Missing parentheses in call to 'print'. Did you mean print('hello world')?
>>> print('hello world')
hello world
>>>
```

The error was a _SyntaxError_. After the fix our code was executed without a hitch. Let see more error types.

### NameError

**Example 1: NameError**

```py
run_example("print(age)", lambda: resolve_name("age"))

age = 25
run_example("print(age)", lambda: resolve_name("age"))
```

```text
>>> print(age)
NameError: name 'age' is not defined
>>> print(age)
25
```

As you can see from the message above, name age is not defined. Yes, it is true that we did not define an age variable but we were trying to access it. Now, lets fix this by declaring it and assigning with a value.

The type of error was a _NameError_. We debugged the error by defining the variable name.

### IndexError

**Example 1: IndexError**

```py
numbers = [1, 2, 3, 4, 5]
run_example("numbers[5]", lambda: safe_index(numbers, 5))
```

```text
>>> numbers[5]
IndexError: list index out of range
```

In the example above, Python raised an _IndexError_, because the list has only indexes from 0 to 4 , so it was out of range.

### ModuleNotFoundError

**Example 1: ModuleNotFoundError**

```py
run_example("import maths", lambda: safe_import("maths"))
math_module = run_example("import math", lambda: safe_import("math"))
```

```text
>>> import maths
ModuleNotFoundError: No module named 'maths'
>>> import math
```

In the example above, I added an extra s to math deliberately and _ModuleNotFoundError_ was raised. Lets fix it by removing the extra s from math.

We fixed it, so let's use some of the functions from the math module.

### AttributeError

**Example 1: AttributeError**

```py
run_example("math.PI", lambda: safe_getattr(math_module, "PI"))
run_example("math.pi", lambda: safe_getattr(math_module, "pi"))
```

```text
>>> math.PI
AttributeError: module 'math' has no attribute 'PI'
>>> math.pi
3.141592653589793
```

As you can see, I made a mistake again! Instead of pi, I tried to call a PI function from maths module. It raised an attribute error, it means, that the function does not exist in the module. Lets fix it by changing from PI to pi.

Now, when we call pi from the math module we got the result.

### KeyError

**Example 1: KeyError**

```py
user = {"name": "Asab", "age": 250, "country": "Finland"}
run_example("user['name']", lambda: safe_get(user, "name"))
run_example("user['county']", lambda: safe_get(user, "county"))
run_example("user['country']", lambda: safe_get(user, "country"))
```

```text
>>> user['name']
Asab
>>> user['county']
KeyError: 'county'
>>> user['country']
Finland
```

As you can see, there was a typo in the key used to get the dictionary value. so, this is a key error and the fix is quite straight forward. Let's do this!

We debugged the error, our code ran and we got the value.

### TypeError

**Example 1: TypeError**

```py
run_example("4 + '3'", lambda: safe_add(4, "3"))
run_example("4 + int('3')", lambda: 4 + int("3"))
run_example("4 + float('3')", lambda: 4 + float("3"))
```

```text
>>> 4 + '3'
TypeError: unsupported operand type(s) for +: 'int' and 'str'
>>> 4 + int('3')
7
>>> 4 + float('3')
7.0
```

In the example above, a TypeError is raised because we cannot add a number to a string. First solution would be to convert the string to int or float. Another solution would be converting the number to a string (the result then would be '43'). Let us follow the first fix.

Error removed and we got the result we expected.

### ImportError

**Example 1: ImportError**

```py
run_example("from math import power", lambda: safe_import_from("math", "power"))
pow_func = run_example("from math import pow", lambda: safe_import_from("math", "pow"))
run_example("pow(2, 3)", lambda: pow_func(2, 3))
```

```text
>>> from math import power
ImportError: cannot import name 'power' from 'math'
>>> from math import pow
<built-in function pow>
>>> pow(2, 3)
8.0
```

There is no function called power in the math module, it goes with a different name: _pow_. Let's correct it:

### ValueError

**Example 1: ValueError**

```py
run_example("int('12a')", lambda: safe_int("12a"))
```

```text
>>> int('12a')
ValueError: invalid literal for int() with base 10: '12a'
```

In this case we cannot change the given string to a number, because of the 'a' letter in it.

### ZeroDivisionError

**Example 1: ZeroDivisionError**

```py
run_example("1 / 0", lambda: safe_divide(1, 0))
```

```text
>>> 1 / 0
ZeroDivisionError: division by zero
```

We cannot divide a number by zero.

We have covered some of the python error types, if you want to check more about it check the python documentation about python error types.
If you are good at reading the error types then you will be able to fix your bugs fast and you will also become a better programmer.

🌕 You are excelling. You made it to half way to your way to greatness. Now do some exercises for your brain and for your muscle.

## 💻 Exercises: Day 15

1. Open you python interactive shell and try all the examples covered in this section.

🎉 CONGRATULATIONS ! 🎉

[<< Day 14](../14_Day_Higher_order_functions/14_higher_order_functions.md) | [Day 16 >>](../16_Day_Python_date_time/16_python_datetime.md)