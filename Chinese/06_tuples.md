<div align="center">
  <h1>30 天 Python：第六天 - Tuples</h1>
  <a class="header-badge" target="_blank" rel="noopener noreferrer" href="https://www.linkedin.com/in/asabeneh/">
    <img alt="LinkedIn badge" src="https://img.shields.io/badge/style--5eba00.svg?label=LinkedIn&logo=linkedin&style=social">
  </a>
  <a class="header-badge" target="_blank" rel="noopener noreferrer" href="https://twitter.com/Asabeneh">
    <img alt="Twitter Follow" src="https://img.shields.io/twitter/follow/asabeneh?style=social">
  </a>

  <sub>Author:
    <a href="https://www.linkedin.com/in/asabeneh/" target="_blank" rel="noopener noreferrer">Asabeneh Yetayeh</a><br>
    <small>第二版：2021 年 7 月</small>
  </sub>
</div>

[<< 第五天](./05_lists.md) | [第七天 >>](./07_sets.md)

![30DaysOfPython](../images/30DaysOfPython_banner3@2x.png)

- [第六天:](#第六天)
  - [元组](#元组)
    - [如何创建元组](#如何创建元组)
    - [元组长度](#元组长度)
    - [获取元组项](#获取元组项)
    - [元组切片](#元组切片)
    - [将元组更改为列表](#将元组更改为列表)
    - [检索元组中的项](#检索元组中的项)
    - [连接元组](#连接元组)
    - [删除元组](#删除元组)
  - [💻 练习 - 第六天](#-练习---第六天)
    - [练习： 1级](#练习-1级)
    - [练习： 2级](#练习-2级)

# 第六天:

## 元组

元组是有序且不可变的不同数据类型的集合。一旦创建了元组，我们就无法更改其值。我们不能在元组中使用 add、insert、remove 方法，因为它是不可修改的（不可变的）。与列表不同，元组的方法很少。与元组相关的方法有：

- `tuple()`：创建一个空元组
- `count()`：计算元组中指定项的数量
- `index()`：查找元组中指定项的索引
- `+` 运算符：连接两个或多个元组并创建一个新元组

### 如何创建元组

- 创建一个空元组

  ```py
  # 语法
  empty_tuple = ()
  # 或使用元组构造函数
  empty_tuple = tuple()
  ```

- 创建一个具有初始值的元组

  ```py
  # 语法
  tpl = ('item1', 'item2', 'item3')
  ```

  ```py
  def make_tuple(*items):
      """使用任意数量的参数创建并返回一个元组。

      参数：
          *items: 要放入元组的任意元素。

      返回：
          tuple: 包含所有传入元素的新元组。
      """
      return tuple(items)


  fruits = make_tuple('banana', 'orange', 'mango', 'lemon')
  ```

### 元组长度

我们使用 `len()` 方法来获取元组的长度。

```py
# 语法
tpl = ('item1', 'item2', 'item3')
len(tpl)
```

```py
def tuple_length(tpl):
    """返回元组的长度。

    参数：
        tpl: 需要计算长度的元组或序列。

    返回：
        int: 元组中元素的数量。
    """
    return len(tpl)


fruits = ('banana', 'orange', 'mango', 'lemon')
print(tuple_length(fruits))  # 4
```

### 获取元组项

- 正索引

  与列表数据类型类似，我们使用正索引或负索引来访问元组项。
  ![Accessing tuple items](../images/tuples_index.png)

  ```py
  # 语法
  tpl = ('item1', 'item2', 'item3')
  first_item = tpl[0]
  second_item = tpl[1]
  ```

  ```py
  def get_tuple_item(tpl, index):
      """安全地获取元组中指定索引的项。

      该函数会验证索引是否越界，避免产生难以调试的 IndexError。

      参数：
          tpl: 目标元组。
          index: 整数索引（支持正负索引）。

      返回：
          元组中指定索引处的项。

      异常：
          IndexError: 当索引超出有效范围时抛出。
      """
      length = len(tpl)
      if not -length <= index < length:
          raise IndexError(
              f"索引 {index} 超出范围。元组长度为 {length}，"
              f"有效索引范围是 {-length} 到 {length - 1}。"
          )
      return tpl[index]


  fruits = ('banana', 'orange', 'mango', 'lemon')
  first_fruit = get_tuple_item(fruits, 0)
  second_fruit = get_tuple_item(fruits, 1)
  last_index = len(fruits) - 1
  last_fruit = get_tuple_item(fruits, last_index)
  ```

- 负索引

  负索引是从末尾开始的，-1 表示最后一项，-2 表示倒数第二项，列表/元组长度的负数表示第一项。
  ![Tuple Negative indexing](../images/tuple_negative_indexing.png)

  ```py
  # 语法
  tpl = ('item1', 'item2', 'item3', 'item4')
  first_item = tpl[-4]
  second_item = tpl[-3]
  ```

  ```py
  fruits = ('banana', 'orange', 'mango', 'lemon')
  first_fruit = get_tuple_item(fruits, -4)
  second_fruit = get_tuple_item(fruits, -3)
  last_fruit = get_tuple_item(fruits, -1)
  ```

### 元组切片

我们可以通过指定开始和结束的索引范围来切出子元组，返回值是一个包含指定项的新元组。

```py
def slice_tuple(tpl, start=None, stop=None):
    """返回元组的一个切片。

    参数：
        tpl: 源元组。
        start: 起始索引（包含），默认为 None，即从开头开始。
        stop: 结束索引（不包含），默认为 None，即到末尾结束。

    返回：
        tuple: 切片后的新元组。
    """
    return tpl[start:stop]
```

- 正索引范围

  ```py
  # 语法
  tpl = ('item1', 'item2', 'item3', 'item4')
  all_items = tpl[0:4]         # 所有项
  all_items = tpl[0:]          # 所有项
  middle_two_items = tpl[1:3]  # 不包括索引 3 的项
  ```

  ```py
  fruits = ('banana', 'orange', 'mango', 'lemon')
  all_fruits = slice_tuple(fruits, 0, 4)    # 所有项
  all_fruits = slice_tuple(fruits, 0)       # 所有项
  orange_mango = slice_tuple(fruits, 1, 3)  # 不包括索引 3 的项
  orange_to_the_rest = slice_tuple(fruits, 1)
  ```

- 负索引范围

  ```py
  # 语法
  tpl = ('item1', 'item2', 'item3', 'item4')
  all_items = tpl[-4:]            # 所有项
  middle_two_items = tpl[-3:-1]   # 不包括索引 3 的项
  ```

  ```py
  fruits = ('banana', 'orange', 'mango', 'lemon')
  all_fruits = slice_tuple(fruits, -4)       # 所有项
  orange_mango = slice_tuple(fruits, -3, -1) # 不包括索引 3 的项
  orange_to_the_rest = slice_tuple(fruits, -3)
  ```

### 将元组更改为列表

我们可以将元组更改为列表，将列表更改为元组。如果我们想修改元组，应该将其更改为列表。

```py
# 语法
tpl = ('item1', 'item2', 'item3', 'item4')
lst = list(tpl)
```

```py
def update_tuple_item(tpl, index, value):
    """通过先转换为列表、修改后再转回元组的方式更新元组中的某一项。

    参数：
        tpl: 原始元组。
        index: 要修改的项的索引。
        value: 新值。

    返回：
        tuple: 修改后的新元组。
    """
    lst = list(tpl)
    lst[index] = value
    return tuple(lst)


fruits = ('banana', 'orange', 'mango', 'lemon')
fruits = update_tuple_item(fruits, 0, 'apple')
print(fruits)     # ('apple', 'orange', 'mango', 'lemon')
```

### 检索元组中的项

我们可以使用 `in` 检查元组中是否存在某个项，它返回一个布尔值。

```py
def item_in_tuple(tpl, item):
    """检查指定项是否存在于元组中。

    参数：
        tpl: 要搜索的元组。
        item: 要查找的项。

    返回：
        bool: 存在返回 True，否则返回 False。
    """
    return item in tpl
```

```py
# 语法
tpl = ('item1', 'item2', 'item3', 'item4')
'item2' in tpl  # True
```

```py
fruits = ('banana', 'orange', 'mango', 'lemon')
print(item_in_tuple(fruits, 'orange'))  # True
print(item_in_tuple(fruits, 'apple'))   # False

# 元组不支持直接赋值，以下代码会抛出 TypeError
# fruits[0] = 'apple'
```

### 连接元组

我们可以使用 `+` 运算符连接两个或多个元组。

```py
def concat_tuples(*tuples):
    """连接两个或多个元组并返回一个新元组。

    参数：
        *tuples: 任意数量的元组。

    返回：
        tuple: 连接后的新元组。
    """
    result = ()
    for t in tuples:
        result += t
    return result
```

```py
# 语法
tpl1 = ('item1', 'item2', 'item3')
tpl2 = ('item4', 'item5', 'item6')
tpl3 = tpl1 + tpl2
```

```py
fruits = ('banana', 'orange', 'mango', 'lemon')
vegetables = ('Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot')
fruits_and_vegetables = concat_tuples(fruits, vegetables)
```

### 删除元组

不能删除元组中的单个项，但可以使用 `del` 删除元组本身。

> ⚠️ 安全提示：`del` 会永久删除变量绑定。删除后再次访问该变量将引发 `NameError`，请谨慎使用。

```py
# 语法
tpl1 = ('item1', 'item2', 'item3')
del tpl1
```

```py
fruits = ('banana', 'orange', 'mango', 'lemon')
del fruits
```

🌕 你太勇敢了，你做到了。你刚刚完成了第 6 天的挑战，你已向着伟大的目标迈出了 6 步。现在做一些练习来锻练你的大脑和肌肉。

## 💻 练习 - 第六天

以下辅助函数将在练习参考实现中复用。

```py
def concat_tuples(*tuples):
    """连接任意数量的元组并返回新元组。"""
    result = ()
    for t in tuples:
        result += t
    return result


def slice_tuple(tpl, start=None, stop=None):
    """返回元组切片。"""
    return tpl[start:stop]


def get_middle_items(seq):
    """返回序列的中间一项（长度为奇数）或两项（长度为偶数）。

    参数：
        seq: 任意可切片的序列。

    返回：
        tuple: 中间元素组成的元组。
    """
    length = len(seq)
    mid = length // 2
    if length % 2 == 0:
        return tuple(seq[mid - 1:mid + 1])
    return tuple(seq[mid:mid + 1])


def slice_edges(seq, n=3):
    """返回序列的前 n 项与后 n 项。

    参数：
        seq: 任意可切片的序列。
        n: 要切出的边缘项数量，默认为 3。

    返回：
        tuple: (前 n 项, 后 n 项)。
    """
    return seq[:n], seq[-n:]


def item_in_tuple(tpl, item):
    """检查 item 是否存在于 tpl 中。"""
    return item in tpl
```

### 练习： 1级

1. 创建一个空元组
1. 创建一个包含你姐妹和兄弟名字的元组（虚构的兄弟姐妹也可以）
1. 连接兄弟姐妹元组并将其分配给 siblings
1. 你有多少兄弟姐妹？
1. 修改兄弟姐妹元组并添加你父母的名字，然后将其分配给 family_members

```py
# 参考实现
def build_family():
    """创建兄弟姐妹元组并扩展为家庭成员元组。

    返回：
        tuple: (siblings, family_members)
    """
    sisters = ('小红', '小芳')
    brothers = ('小明', '小华')
    siblings = concat_tuples(sisters, brothers)

    parents = ('父亲', '母亲')
    family_members = concat_tuples(siblings, parents)

    return siblings, family_members


siblings, family_members = build_family()
print(siblings)                      # ('小红', '小芳', '小明', '小华')
print(len(siblings))                 # 4
print(family_members)                # ('小红', '小芳', '小明', '小华', '父亲', '母亲')
```

### 练习： 2级

1. 从 family_members 中获取兄弟姐妹和父母
1. 创建 fruits、vegetables 和 animal products 元组。连接三个元组并将其分配给名为 food_stuff_tp 的变量。
1. 将 food_stuff_tp 元组更改为 food_stuff_lt 列表
1. 从 food_stuff_tp 元组或 food_stuff_lt 列表中切出中间项或项。
1. 从 food_stuff_lt 列表中切出前三项和最后三项
1. 完全删除 food_stuff_tp 元组
1. 检查元组中是否存在项：
   - 检查 'Estonia' 是否在 nordic_country 元组中
   - 检查 'Iceland' 是否在 nordic_country 元组中

```py
# 1. 拆分家庭成员
def split_family(family_members):
    """从家庭成员元组中拆分出兄弟姐妹和父母。

    假设最后两项是父母。
    """
    siblings = family_members[:-2]
    parents = family_members[-2:]
    return siblings, parents


siblings, parents = split_family(family_members)
print(siblings)
print(parents)

# 2. 连接食物元组
fruits = ('banana', 'orange', 'mango', 'lemon')
vegetables = ('Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot')
animal_products = ('milk', 'meat', 'butter', 'yoghurt')
food_stuff_tp = concat_tuples(fruits, vegetables, animal_products)

# 3. 元组转列表
food_stuff_lt = list(food_stuff_tp)

# 4. 切出中间项
middle = get_middle_items(food_stuff_tp)
print(middle)

# 5. 切出前三项和最后三项
first_three, last_three = slice_edges(food_stuff_lt, 3)
print(first_three)
print(last_three)

# 6. 删除 food_stuff_tp 元组
del food_stuff_tp

# 7. 检查 nordic_countries 中的成员
nordic_countries = ('Denmark', 'Finland', 'Iceland', 'Norway', 'Sweden')
print(item_in_tuple(nordic_countries, 'Estonia'))  # False
print(item_in_tuple(nordic_countries, 'Iceland'))  # True
```

[<< 第五天](./05_lists.md) | [第七天 >>](./07_sets.md)