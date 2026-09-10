<div align="center">
  <h1> 30天Python：第14天 - 高阶函数</h1>
  <a class="header-badge" target="_blank" href="https://www.linkedin.com/in/asabeneh/">
  <img src="https://img.shields.io/badge/style--5eba00.svg?label=LinkedIn&logo=linkedin&style=social">
  </a>
  <a class="header-badge" target="_blank" href="https://twitter.com/Asabeneh">
  <img alt="Twitter Follow" src="https://img.shields.io/twitter/follow/asabeneh?style=social">
  </a>

<sub>作者:
<a href="https://www.linkedin.com/in/asabeneh/" target="_blank">Asabeneh Yetayeh</a><br>
<small>第二版：2021 年 7 月</small>
</sub>

</div>

[<< 第 13 天](../13_Day_List_comprehension/13_list_comprehension.md) | [第 15 天>>](../15_Day_Python_type_errors/15_python_type_errors.md)

![30DaysOfPython](../images/30DaysOfPython_banner3@2x.png)

- [📘 第 14 天](#-第14天)
  - [高阶函数](#高阶函数)
    - [函数作为参数](#函数作为参数)
    - [函数作为返回值](#函数作为返回值)
  - [Python 闭包](#python闭包)
  - [Python 装饰器](#python装饰器)
    - [创建装饰器](#创建装饰器)
    - [将多个装饰器应用于单个函数](#将多个装饰器应用于单个函数)
    - [在装饰器函数中接受参数](#在装饰器函数中接受参数)
  - [内置高阶函数](#内置高阶函数)
    - [Python - Map 函数](#python---map函数)
    - [Python - Filter 函数](#python---filter函数)
    - [Python - Reduce 函数](#python---reduce函数)
  - [💻 练习：第 14 天](#-练习-第14天)
    - [练习：简单](#练习-简单)
    - [练习：中等](#练习-中等)
    - [练习：高级](#练习-高级)

# 📘 第 14 天

## 高阶函数

在 Python 中，函数被视为第一类公民，可以对函数执行以下操作：

- 一个函数可以接收一个或多个函数作为参数
- 一个函数可以作为另一个函数的返回值
- 一个函数可以被修改
- 一个函数可以被赋值给变量

在本节中，我们将讨论：

1. 将函数作为参数传递
2. 将函数作为返回值返回
3. 使用 Python 闭包和装饰器

### 函数作为参数

```py
def sum_numbers(nums):
    """对可迭代对象中的数字求和，并验证输入类型。"""
    if not hasattr(nums, "__iter__"):
        raise TypeError("nums 必须是一个可迭代对象")
    return sum(nums)


def higher_order_function(func, iterable):
    """
    高阶函数：接收一个函数和一个可迭代对象，
    用该函数处理可迭代对象后返回结果。
    """
    # 校验 func 是否为可调用对象
    if not callable(func):
        raise TypeError("func 必须是一个可调用对象")
    # 校验 iterable 是否为可迭代对象
    if not hasattr(iterable, "__iter__"):
        raise TypeError("iterable 必须是一个可迭代对象")

    return func(iterable)


result = higher_order_function(sum_numbers, [1, 2, 3, 4, 5])
print(result)  # 15
```

### 函数作为返回值

```py
def square(x):
    """返回 x 的平方。"""
    return x ** 2


def cube(x):
    """返回 x 的立方。"""
    return x ** 3


def absolute(x):
    """返回 x 的绝对值。"""
    return x if x >= 0 else -x


# 用字典集中管理 operation -> function 的映射，避免冗长的 if/elif
_OPERATION_MAP = {
    "square": square,
    "cube": cube,
    "absolute": absolute,
}


def higher_order_function(operation):
    """
    根据 operation 名称返回对应的函数。
    如果名称无效，抛出 ValueError。
    """
    if operation not in _OPERATION_MAP:
        raise ValueError(f"未知操作: {operation!r}")

    return _OPERATION_MAP[operation]


result = higher_order_function("square")
print(result(3))        # 9

result = higher_order_function("cube")
print(result(3))        # 27

result = higher_order_function("absolute")
print(result(-3))       # 3
```

从上述示例中可以看到，高阶函数根据传入的参数来返回不同的函数。

## Python 闭包

Python 允许嵌套函数访问外部封闭函数的作用域。这称为闭包。让我们看看闭包在 Python 中的工作原理。在 Python 中，闭包是通过在另一个封装函数内部嵌套函数，然后返回内部函数来创建的。请看下面的例子。

**示例：**

```py
def add_ten():
    """创建并返回一个闭包，内部函数始终加 10。"""
    ten = 10

    def add(num):
        if not isinstance(num, (int, float)):
            raise TypeError("num 必须是数字")
        return num + ten

    return add


closure_result = add_ten()
print(closure_result(5))   # 15
print(closure_result(10))  # 20
```

## Python 装饰器

装饰器是一种设计模式，允许用户在不修改对象结构的情况下为其添加新功能。装饰器通常在你想要装饰的函数定义之前调用。

### 创建装饰器

要创建装饰器函数，我们需要一个带有内部包装器函数的外部函数。

**示例：**

```py
def greeting():
    return "Welcome to Python"


def uppercase_decorator(function):
    """将函数返回的字符串转为大写。"""
    if not callable(function):
        raise TypeError("function 必须是一个可调用对象")

    def wrapper():
        result = function()
        if not isinstance(result, str):
            raise TypeError("被装饰函数必须返回字符串")
        return result.upper()

    return wrapper


# 手动使用装饰器
g = uppercase_decorator(greeting)
print(g())  # WELCOME TO PYTHON


# 使用 @ 语法糖
@uppercase_decorator
def greeting():
    return "Welcome to Python"

print(greeting())  # WELCOME TO PYTHON
```

### 将多个装饰器应用于单个函数

```py
def uppercase_decorator(function):
    """将函数返回的字符串转为大写。"""
    if not callable(function):
        raise TypeError("function 必须是一个可调用对象")

    def wrapper():
        result = function()
        if not isinstance(result, str):
            raise TypeError("被装饰函数必须返回字符串")
        return result.upper()

    return wrapper


def split_string_decorator(function):
    """将函数返回的字符串按空格拆分为列表。"""
    if not callable(function):
        raise TypeError("function 必须是一个可调用对象")

    def wrapper():
        result = function()
        if not isinstance(result, str):
            raise TypeError("被装饰函数必须返回字符串")
        return result.split()

    return wrapper


# 装饰器从下往上执行：先 upper，再 split。
# 注意顺序很重要，如果对列表调用 upper() 会报错。
@split_string_decorator
@uppercase_decorator
def greeting():
    return "Welcome to Python"

print(greeting())  # ['WELCOME', 'TO', 'PYTHON']
```

### 在装饰器函数中接受参数

大多数时候我们需要我们的函数接受参数，所以我们可能需要定义一个接受参数的装饰器。

```py
def decorator_with_parameters(function):
    """接收带参数函数的装饰器，保留原函数返回值并额外打印居住信息。"""
    if not callable(function):
        raise TypeError("function 必须是一个可调用对象")

    def wrapper(first_name, last_name, country):
        # 先执行原函数，并保留其返回值
        result = function(first_name, last_name, country)
        print("I live in {}".format(country))
        return result

    return wrapper


@decorator_with_parameters
def print_full_name(first_name, last_name, country):
    print("I am {} {}. I love to teach.".format(first_name, last_name))
    return f"{first_name} {last_name}"


print_full_name("Asabeneh", "Yetayeh", "Finland")
```

## 内置高阶函数

在本部分中，我们将讨论一些内置的高阶函数，如 *map()*, *filter* 和 *reduce*。
Lambda 函数可以作为参数传递，其最佳使用案例是在 map、filter 和 reduce 等功能中。

### Python - Map 函数

map() 函数是一个内置函数，接收一个函数和可迭代对象作为参数。

```py
    # 语法
    map(function, iterable)
```

**示例：1**

```py
numbers = [1, 2, 3, 4, 5]  # 可迭代对象


def square(x):
    """返回 x 的平方。"""
    return x ** 2


# 使用普通函数
numbers_squared = map(square, numbers)
print(list(numbers_squared))  # [1, 4, 9, 16, 25]

# 使用 lambda 函数，写法更简洁
numbers_squared = map(lambda x: x ** 2, numbers)
print(list(numbers_squared))  # [1, 4, 9, 16, 25]
```

**示例：2**

```py
numbers_str = ["1", "2", "3", "4", "5"]  # 可迭代对象
numbers_int = map(int, numbers_str)
print(list(numbers_int))  # [1, 2, 3, 4, 5]
```

**示例：3**

```py
names = ["Asabeneh", "Lidiya", "Ermias", "Abraham"]  # 可迭代对象


def change_to_upper(name):
    """将名称转换为大写，并验证输入类型。"""
    if not isinstance(name, str):
        raise TypeError("name 必须是字符串")
    return name.upper()


names_upper_cased = map(change_to_upper, names)
print(list(names_upper_cased))  # ["ASABENEH", "LIDIYA", "ERMIAS", "ABRAHAM"]

# 使用 lambda 函数
names_upper_cased = map(lambda name: name.upper(), names)
print(list(names_upper_cased))  # ["ASABENEH", "LIDIYA", "ERMIAS", "ABRAHAM"]
```

map 函数实际上是迭代列表。例如，它将名称更改为大写并返回一个新列表。

### Python - Filter 函数

filter() 函数调用指定函数，该函数对指定的可迭代对象（列表）中的每个项目返回布尔值。它过滤出满足过滤条件的项目。

```py
    # 语法
    filter(function, iterable)
```

**示例：1**

```py
# 让我们只过滤偶数
numbers = [1, 2, 3, 4, 5]  # 可迭代对象


def is_even(num):
    """判断数字是否为偶数。"""
    return num % 2 == 0


even_numbers = filter(is_even, numbers)
print(list(even_numbers))  # [2, 4]
```

**示例：2**

```py
numbers = [1, 2, 3, 4, 5]  # 可迭代对象


def is_odd(num):
    """判断数字是否为奇数。"""
    return num % 2 != 0


odd_numbers = filter(is_odd, numbers)
print(list(odd_numbers))  # [1, 3, 5]
```

**示例：3**

```py
# 过滤长名称
names = ["Asabeneh", "Lidiya", "Ermias", "Abraham"]  # 可迭代对象


def make_length_predicate(min_len):
    """
    返回一个可复用的判断函数：
    当字符串长度大于 min_len 时返回 True。
    """
    def predicate(name):
        return isinstance(name, str) and len(name) > min_len

    return predicate


long_names = filter(make_length_predicate(7), names)
print(list(long_names))  # ["Asabeneh"]
```

### Python - Reduce 函数

*reduce()* 函数定义在 functools 模块中，我们需要从这个模块中导入它。像 map 和 filter 一样，它接收两个参数，一个函数和一个可迭代对象。然而，它不返回另一个可迭代对象，而是返回一个单一的值。

**示例：1**

```py
from functools import reduce

numbers_str = ["1", "2", "3", "4", "5"]  # 可迭代对象


def add_two_nums(x, y):
    """将两个值转为整数后求和。"""
    return int(x) + int(y)


total = reduce(add_two_nums, numbers_str)
print(total)  # 15
```

## 💻 练习：第 14 天

```py
countries = ["Estonia", "Finland", "Sweden", "Denmark", "Norway", "Iceland"]
names = ["Asabeneh", "Lidiya", "Ermias", "Abraham"]
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
```

### 练习：简单

1. 解释 map、filter 和 reduce 的区别。
2. 解释高阶函数、闭包和装饰器的区别。
3. 定义调用函数，见示例。
4. 使用 for 循环打印 countries 列表中的每个国家。
5. 使用 for 循环打印 names 列表中的每个名称。
6. 使用 for 循环打印 numbers 列表中的每个数字。

### 练习：中等

1. 使用 map 将 countries 列表中的每个国家更改为大写，生成一个新列表。
2. 使用 map 将 numbers 列表中的每个数字更改为平方，生成一个新列表。
3. 使用 map 将 names 列表中的每个名称更改为大写，生成一个新列表。
4. 使用 filter 过滤出包含“land”的国家。
5. 使用 filter 过滤出正好六个字符的国家。
6. 使用 filter 过滤出包含六个字母及以上的国家。
7. 使用 filter 过滤出以'E'开头的国家。
8. 链接两个或多个列表迭代器（例如 arr.map(callback).filter(callback).reduce(callback)）。
9. 声明一个函数 get_string_lists，它接收一个列表作为参数并返回一个仅包含字符串项的列表。
10. 使用 reduce 对 numbers 列表中的所有数字求和。
11. 使用 reduce 将所有国家连接起来，生成句子：Estonia, Finland, Sweden, Denmark, Norway, and Iceland are north European countries。
12. 声明一个函数 categorize_countries，返回一个包含某种通用模式的国家列表（可以在本仓库的 countries.js 文件中找到国家列表，例如 "land", "ia", "island", "stan"）。
13. 创建一个返回字典的函数，其中键表示国家名称的首字母，值表示以该字母开头的国家数。
14. 声明一个 get_first_ten_countries 函数 - 它返回数据文件夹中 countries.js 列表中的前十个国家。
15. 声明一个 get_last_ten_countries 函数 - 它返回国家列表中的最后十个国家。

### 练习：高级

1. 使用 countries_data.py (https://github.com/Asabeneh/30-Days-Of-Python/blob/master/data/countries-data.py) 文件，完成以下任务：
   - 按国家名称、首都和人口排序国家
   - 按位置排序出前十个最常用语言。
   - 排序出前十个人口最多的国家。

🎉 恭喜你！ 🎉

[<< 第 13 天](../13_Day_List_comprehension/13_list_comprehension.md) | [第 15 天>>](../15_Day_Python_type_errors/15_python_type_errors.md)