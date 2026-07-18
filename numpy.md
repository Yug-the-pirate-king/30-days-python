- [📘 Day 24](#-day-24)
  - [Python for Statistical Analysis](#python-for-statistical-analysis)
  - [Statistics](#statistics)
  - [Data](#data)
  - [Statistics Module](#statistics-module)
- [NumPy](#numpy)
  - [Importing NumPy](#importing-numpy)
  - [Creating numpy array using](#creating-numpy-array-using)
    - [Creating int numpy arrays](#creating-int-numpy-arrays)
    - [Creating float numpy arrays](#creating-float-numpy-arrays)
    - [Creating boolean numpy arrays](#creating-boolean-numpy-arrays)
    - [Creating multidimensional array using numpy](#creating-multidimensional-array-using-numpy)
    - [Converting numpy array to list](#converting-numpy-array-to-list)
    - [Creating numpy array from tuple](#creating-numpy-array-from-tuple)
    - [Shape of numpy array](#shape-of-numpy-array)
    - [Data type of numpy array](#data-type-of-numpy-array)
    - [Size of a numpy array](#size-of-a-numpy-array)
  - [Mathematical Operations using NumPy](#mathematical-operations-using-numpy)
    - [Addition](#addition)
    - [Subtraction](#subtraction)
    - [Multiplication](#multiplication)
    - [Division](#division)
    - [Modulus](#modulus)
    - [Floor Division](#floor-division)
    - [Exponential](#exponential)
  - [Checking data types](#checking-data-types)
    - [Converting types](#converting-types)
  - [Multi-dimensional Arrays](#multi-dimensional-arrays)
    - [Getting items from a numpy array](#getting-items-from-a-numpy-array)
  - [Slicing NumPy Arrays](#slicing-numpy-arrays)
    - [How to reverse the rows?](#how-to-reverse-the-rows)
    - [Reverse the row and column positions](#reverse-the-row-and-column-positions)
  - [How to represent missing values?](#how-to-represent-missing-values)
      - [Generating Random Numbers](#generating-random-numbers)
    - [Generating Normally Distributed Random Numbers](#generating-normally-distributed-random-numbers)
  - [NumPy and Statistics](#numpy-and-statistics)
    - [Matrix in numpy](#matrix-in-numpy)
    - [NumPy arange()](#numpy-arange)
      - [What is arange?](#what-is-arange)
    - [Creating sequence of numbers using linspace](#creating-sequence-of-numbers-using-linspace)
    - [NumPy Statistical Functions with Example](#numpy-statistical-functions-with-example)
    - [How to create repeating sequences?](#how-to-create-repeating-sequences)
    - [How to generate random numbers?](#how-to-generate-random-numbers)
    - [Linear Algebra](#linear-algebra)
    - [NumPy Matrix Multiplication with np.matmul()](#numpy-matrix-multiplication-with-npmatmul)
- [Summary](#summary)
  - [💻 Exercises: Day 24](#-exercises-day-24)

# 📘 Day 24

## Python for Statistical Analysis

## Statistics

Statistics is the discipline that studies the _collection_, _organization_, _displaying_, _analysis_, _interpretation_ and _presentation_ of data.
Statistics is a branch of mathematics that is recommended to be a prerequisite for data science and machine learning. Statistics is a very broad field but we will focus in this section only on the most relevant part.
After completing this challenge, you may go to web development, data analysis, machine learning and data science path. Whatever path you may follow, at some point in your career you will get data which you may work on. Having some statistical knowledge will help you to make decision based on data, _data tells as they say_.

## Data

What is data? Data is any set of characters that is gathered and translated for some purpose, usually analysis. It can be any character, including text and numbers, pictures, sound, or video. If data is not put into context, it doesn't give any sense to a human or computer. To make sense from data we need to work on the data using different tools.

The work flow of data analysis, data science or machine learning starts from data. Data can be provided from some data source or it can be created. There are structured and unstructured data.

Data can be found as small or big data format. Most of the data types we will get have been covered in the file handling section.

## Statistics Module

The python _statistics_ module provides functions for calculating mathematical statistics of numeric data. The module is not intended to be a competitor to third-party libraries such as NumPy, SciPy, or proprietary full-featured statistics packages aimed at professional statisticians such as Minitab, SAS and Matlab. It is aimed at the level of graphing and scientific calculators.

# NumPy

In the first section we defined python as a great general-purpose programming language on its own, but with the help of other popular libraries (numpy, scipy, matplotlib, pandas etc) it becomes a powerful environment for scientific computing.

NumPy is the core library for scientific computing in Python. It provides a high-performance multidimensional array object, and tools for working with arrays.

So far, we have been using vscode but from now on I would recommend using Jupyter Notebook. To access Jupyter Notebook let's install [anaconda](https://www.anaconda.com/). If you are using anaconda most of the common packages are included and you don't have install packages if you installed anaconda.

```sh
asabeneh@Asabeneh:~/Desktop/30DaysOfPython$ pip install numpy
```

## Importing NumPy

Jupyter notebook is available if your are in favor of [Jupyter Notebook](https://github.com/Asabeneh/data-science-for-everyone/blob/master/numpy/numpy.ipynb)

```py
# Import the NumPy package, conventionally aliased as np
import numpy as np

# Check the installed version of NumPy
print('numpy:', np.__version__)

# Inspect the available NumPy attributes and methods
print(dir(np))
```

## Creating numpy array using

### Creating int numpy arrays

```py
# A regular Python list of integers
numbers_list = [1, 2, 3, 4, 5]

# Verify the type of the Python object
print('Type:', type(numbers_list))  # <class 'list'>
print(numbers_list)                # [1, 2, 3, 4, 5]

# A nested Python list representing a 3x3 matrix
matrix_list = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
print(matrix_list)  # [[0, 1, 2], [3, 4, 5], [6, 7, 8]]

# Convert a Python list into a NumPy ndarray (N-dimensional array)
numbers_array = np.array(numbers_list)
print(type(numbers_array))   # <class 'numpy.ndarray'>
print(numbers_array)         # array([1, 2, 3, 4, 5])
```

### Creating float numpy arrays

Creating a float numpy array from a list with an explicit float dtype parameter

```py
# Python list of integers
numbers_list = [1, 2, 3, 4, 5]

# Create a NumPy array of floats by specifying dtype=float
float_array_from_list = np.array(numbers_list, dtype=float)
print(float_array_from_list)  # array([1., 2., 3., 4., 5.])
```

### Creating boolean numpy arrays

Creating a boolean NumPy array from a list

```py
# Any non-zero value becomes True; zero becomes False
bool_array = np.array([0, 1, -1, 0, 0], dtype=bool)
print(bool_array)  # array([False,  True,  True, False, False])
```

### Creating multidimensional array using numpy

A numpy array may have one or multiple rows and columns

```py
# Nested list representing a 3x3 matrix
matrix_list = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]

# Convert to a two-dimensional NumPy array
matrix_array = np.array(matrix_list)

print(type(matrix_array))
print(matrix_array)
```

```sh
<class 'numpy.ndarray'>
[[0 1 2]
 [3 4 5]
 [6 7 8]]
```

### Converting numpy array to list

```python
# We can always convert an array back to a Python list using tolist().
numbers_array_as_list = numbers_array.tolist()

print(type(numbers_array_as_list))
print('one dimensional array:', numbers_array_as_list)
print('two dimensional array:', matrix_array.tolist())
```

```sh
<class 'list'>
one dimensional array: [1, 2, 3, 4, 5]
two dimensional array:  [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
```

### Creating numpy array from tuple

```py
# A Python tuple
numbers_tuple = (1, 2, 3, 4, 5)

print(type(numbers_tuple))                    # <class 'tuple'>
print('numbers_tuple:', numbers_tuple)        # numbers_tuple: (1, 2, 3, 4, 5)

# Create a NumPy array from the tuple
array_from_tuple = np.array(numbers_tuple)

print(type(array_from_tuple))                 # <class 'numpy.ndarray'>
print('array_from_tuple:', array_from_tuple)  # array_from_tuple: [1 2 3 4 5]
```

### Shape of numpy array

The shape method provide the shape of the array as a tuple. The first is the row and the second is the column. If the array is just one dimensional it returns the size of the array.

```py
# A one-dimensional array
numbers = np.array([1, 2, 3, 4, 5])
print(numbers)
print('shape of numbers:', numbers.shape)

# A two-dimensional array
print(matrix_array)
print('shape of matrix_array:', matrix_array.shape)

# A 3x4 matrix
three_by_four_matrix = np.array([[0, 1, 2, 3],
                                 [4, 5, 6, 7],
                                 [8, 9, 10, 11]])
print(three_by_four_matrix.shape)
```

```sh
[1 2 3 4 5]
shape of numbers: (5,)
[[0 1 2]
 [3 4 5]
 [6 7 8]]
shape of matrix_array: (3, 3)
(3, 4)
```

### Data type of numpy array

Common NumPy data types include: int, float, complex, bool, str, object.

```py
int_values = [-3, -2, -1, 0, 1, 2, 3]

int_array = np.array(int_values)
float_array = np.array(int_values, dtype=float)

print(int_array)
print(int_array.dtype)
print(float_array)
print(float_array.dtype)
```

```sh
[-3 -2 -1  0  1  2  3]
int64
[-3. -2. -1.  0.  1.  2.  3.]
float64
```

### Size of a numpy array

In NumPy, to know the number of items in an array we use the `size` attribute.

```py
numbers_array = np.array([1, 2, 3, 4, 5])
matrix_array = np.array([[0, 1, 2],
                         [3, 4, 5],
                         [6, 7, 8]])

print('The size of numbers_array:', numbers_array.size)   # 5
print('The size of matrix_array:', matrix_array.size)     # 9 (3 rows * 3 columns)
```

```sh
The size of numbers_array: 5
The size of matrix_array: 9
```

## Mathematical Operations using NumPy

Numpy array is not exactly like a Python list. To do a mathematical operation on a Python list we have to loop through the items, but NumPy can perform element-wise operations without looping.

Mathematical operations:

- Addition (+)
- Subtraction (-)
- Multiplication (\*)
- Division (/)
- Modulus (%)
- Floor Division (//)
- Exponential (\*\*)

### Addition

```py
# Addition: add 10 to every element
numbers_array = np.array([1, 2, 3, 4, 5])
print('original array:', numbers_array)

plus_ten = numbers_array + 10
print(plus_ten)
```

```sh
original array: [1 2 3 4 5]
[11 12 13 14 15]
```

### Subtraction

```python
# Subtraction: subtract 10 from every element
numbers_array = np.array([1, 2, 3, 4, 5])
print('original array:', numbers_array)

minus_ten = numbers_array - 10
print(minus_ten)
```

```sh
original array: [1 2 3 4 5]
[-9 -8 -7 -6 -5]
```

### Multiplication

```python
# Multiplication: multiply every element by 10
numbers_array = np.array([1, 2, 3, 4, 5])
print('original array:', numbers_array)

times_ten = numbers_array * 10
print(times_ten)
```

```sh
original array: [1 2 3 4 5]
[10 20 30 40 50]
```

### Division

```python
# Division: divide every element by 10
numbers_array = np.array([1, 2, 3, 4, 5])
print('original array:', numbers_array)

divided_by_ten = numbers_array / 10
print(divided_by_ten)
```

```sh
original array: [1 2 3 4 5]
[0.1 0.2 0.3 0.4 0.5]
```

### Modulus

```python
# Modulus: remainder of division by 3 for each element
numbers_array = np.array([1, 2, 3, 4, 5])
print('original array:', numbers_array)

remainder_by_three = numbers_array % 3
print(remainder_by_three)
```

```sh
original array: [1 2 3 4 5]
[1 2 0 1 2]
```

### Floor Division

```py
# Floor division: division result without the remainder
numbers_array = np.array([1, 2, 3, 4, 5])
print('original array:', numbers_array)

floor_divided_by_ten = numbers_array // 10
print(floor_divided_by_ten)
```

```sh
original array: [1 2 3 4 5]
[0 0 0 0 0]
```

### Exponential

```py
# Exponential: raise each element to the power of 2
numbers_array = np.array([1, 2, 3, 4, 5])
print('original array:', numbers_array)

squared = numbers_array ** 2
print(squared)
```

```sh
original array: [1 2 3 4 5]
[ 1  4  9 16 25]
```

## Checking data types

```py
# Integer, float and boolean arrays
int_arr = np.array([1, 2, 3, 4])
float_arr = np.array([1.1, 2.0, 3.2])
bool_arr = np.array([-3, -2, 0, 1, 2, 3], dtype='bool')

print(int_arr.dtype)
print(float_arr.dtype)
print(bool_arr.dtype)
```

```sh
int64
float64
bool
```

### Converting types

We can convert the data types of a NumPy array.

1. Int to Float

```py
int_as_float = np.array([1, 2, 3, 4], dtype='float')
int_as_float
```

    array([1., 2., 3., 4.])

2. Float to Int

```py
float_as_int = np.array([1., 2., 3., 4.], dtype='int')
float_as_int
```

```sh
array([1, 2, 3, 4])
```

3. Int to boolean

```py
np.array([-3, -2, 0, 1, 2, 3], dtype='bool')
```

```sh
array([ True,  True, False,  True,  True,  True])
```

4. Float to int, then to str

```py
# astype returns a copy of the array cast to a new type
string_arr = float_arr.astype('int').astype('str')
string_arr
```

```sh
array(['1', '2', '3'], dtype='<U21')
```

## Multi-dimensional Arrays

```py
# A 2-dimensional array (3x3 matrix)
sample_matrix = np.array([(1, 2, 3), (4, 5, 6), (7, 8, 9)])

print(type(sample_matrix))
print(sample_matrix)
print('Shape:', sample_matrix.shape)
print('Size:', sample_matrix.size)
print('Data type:', sample_matrix.dtype)
```

```sh
<class 'numpy.ndarray'>
[[1 2 3]
 [4 5 6]
 [7 8 9]]
Shape: (3, 3)
Size: 9
Data type: int64
```

### Getting items from a numpy array

```py
# A 2-dimensional array
sample_matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Access rows by index
first_row = sample_matrix[0]
second_row = sample_matrix[1]
third_row = sample_matrix[2]

print('First row:', first_row)
print('Second row:', second_row)
print('Third row:', third_row)
```

```sh
First row: [1 2 3]
Second row: [4 5 6]
Third row: [7 8 9]
```

```py
# Access columns using the column index and a full row slice
first_column = sample_matrix[:, 0]
second_column = sample_matrix[:, 1]
third_column = sample_matrix[:, 2]

print('First column:', first_column)
print('Second column:', second_column)
print('Third column:', third_column)
print(sample_matrix)
```

```sh
First column: [1 4 7]
Second column: [2 5 8]
Third column: [3 6 9]
[[1 2 3]
 [4 5 6]
 [7 8 9]]
```

## Slicing NumPy Arrays

Slicing in NumPy is similar to slicing in a Python list.

```py
sample_matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Slice the first two rows and the first two columns
top_left_submatrix = sample_matrix[0:2, 0:2]
print(top_left_submatrix)
```

```sh
[[1 2]
 [4 5]]
```

### How to reverse the rows?

```py
# Reverse the order of rows (flip vertically)
sample_matrix[::-1]
```

```sh
array([[7, 8, 9],
       [4, 5, 6],
       [1, 2, 3]])
```

### Reverse the row and column positions

```py
sample_matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Reverse both rows and columns (flip vertically and horizontally)
sample_matrix[::-1, ::-1]
```

```sh
array([[9, 8, 7],
       [6, 5, 4],
       [3, 2, 1]])
```

## How to represent missing values?

Missing values in NumPy are usually represented with `np.nan`. Note that `np.nan` is a float value, so the array must have a float dtype to hold it correctly.

```python
print(sample_matrix)

# Modify specific elements
sample_matrix[1, 1] = 55
sample_matrix[1, 2] = 44
print(sample_matrix)
```

```sh
[[1 2 3]
 [4 5 6]
 [7 8 9]]
[[ 1  2  3]
 [ 4 55 44]
 [ 7  8  9]]
```

```py
# Represent missing values with np.nan using a float array
float_matrix = np.array([[1.0, 2.0, 3.0],
                         [4.0, 5.0, 6.0],
                         [7.0, 8.0, 9.0]])
float_matrix[1, 1] = np.nan
print(float_matrix)
```

```sh
[[ 1.  2.  3.]
 [ 4. nan  6.]
 [ 7.  8.  9.]]
```

```py
# Create an array filled with zeros
# numpy.zeros(shape, dtype=float, order='C')
zeros_array = np.zeros((3, 3), dtype=int, order='C')
print(zeros_array)
```

```sh
[[0 0 0]
 [0 0 0]
 [0 0 0]]
```

```py
# Create an array filled with ones
ones_array = np.ones((3, 3), dtype=int, order='C')
print(ones_array)
```

```sh
[[1 1 1]
 [1 1 1]
 [1 1 1]]
```

```py
# Scale the ones array to get an array of twos
twos_array = ones_array * 2
print(twos_array)
```

```sh
[[2 2 2]
 [2 2 2]
 [2 2 2]]
```

```py
# Reshape and flatten
# numpy.reshape() changes the shape without changing the data
# numpy.flatten() returns a one-dimensional copy of the data
original_shape_array = np.array([(1, 2, 3), (4, 5, 6)])
print(original_shape_array)

reshaped_array = original_shape_array.reshape(3, 2)
print(reshaped_array)
```

```sh
[[1 2 3]
 [4 5 6]]
[[1 2]
 [3 4]
 [5 6]]
```

```py
flattened_array = reshaped_array.flatten()
print(flattened_array)
```

```sh
[1 2 3 4 5 6]
```

```py
## Horizontal Stack
first_array = np.array([1, 2, 3])
second_array = np.array([4, 5, 6])

# Element-wise addition
print(first_array + second_array)

# Concatenate horizontally (along the existing axis)
print('Horizontal Append:', np.hstack((first_array, second_array)))
```

```sh
[5 7 9]
Horizontal Append: [1 2 3 4 5 6]
```

```py
## Vertical Stack
# Stack arrays vertically (as new rows)
print('Vertical Append:', np.vstack((first_array, second_array)))
```

```sh
Vertical Append: [[1 2 3]
 [4 5 6]]
```

#### Generating Random Numbers

```py
# Generate a single random float in the half-open interval [0.0, 1.0)
random_float = np.random.random()
print(random_float)
```

```sh
0.018929887384753874
```

```py
# Generate an array of 5 random floats in [0.0, 1.0)
random_floats = np.random.random(5)
print(random_floats)
```

```sh
array([0.26392192, 0.35842215, 0.87908478, 0.41902195, 0.78926418])
```

```py
# Generate a random integer in the half-open interval [0, 11)
# The low value is inclusive and the high value is exclusive
random_integer = np.random.randint(0, 11)
print(random_integer)
```

```sh
4
```

```py
# Generate 4 random integers between 2 (inclusive) and 10 (exclusive)
random_integers = np.random.randint(2, 10, size=4)
print(random_integers)
```

```sh
array([8, 8, 8, 2])
```

```py
# Generate a 3x3 matrix of random integers between 2 and 10
random_integer_matrix = np.random.randint(2, 10, size=(3, 3))
print(random_integer_matrix)
```

```sh
array([[3, 5, 3],
       [7, 3, 6],
       [2, 3, 3]])
```

### Generating Normally Distributed Random Numbers

```py
# np.random.normal(mu, sigma, size)
# mu = mean, sigma = standard deviation, size = number of samples
normal_samples = np.random.normal(79, 15, 80)
print(normal_samples)
```

```sh
array([ 89.49990595,  82.06056961, 107.21445842,  38.69307086,
        47.85259157,  93.07381061,  76.40724259,  78.55675184,
        72.17358173,  47.9888899 ,  65.10370622,  76.29696568,
        95.58234254,  68.14897213,  38.75862686, 122.5587927 ,
        67.0762565 ,  95.73990864,  81.97454563,  92.54264805,
        59.37035153,  77.76828101,  52.30752166,  64.43109931,
        62.63695351,  90.04616138,  75.70009094,  49.87586877,
        80.22002414,  68.56708848,  76.27791052,  67.24343975,
        81.86363935,  78.22703433, 102.85737041,  65.15700341,
        84.87033426,  76.7569997 ,  64.61321853,  67.37244562,
        74.4068773 ,  58.65119655,  71.66488727,  53.42458179,
        70.26872028,  60.96588544,  83.56129414,  72.14255326,
        81.00787609,  71.81264853,  72.64168853,  86.56608717,
        94.94667321,  82.32676973,  70.5165446 ,  85.43061003,
        72.45526212,  87.34681775,  87.69911217, 103.02831489,
        75.28598596,  67.17806893,  92.41274447, 101.06662611,
        87.70013935,  70.73980645,  46.40368207,  50.17947092,
        61.75618542,  90.26191397,  78.63968639,  70.84550744,
        88.91826581, 103.91474733,  66.3064638 ,  79.49726264,
        70.81087439,  83.90130623,  87.58555972,  59.95462521])
```

## NumPy and Statistics

```py
import matplotlib.pyplot as plt
import seaborn as sns

sns.set()
plt.hist(normal_samples, color="grey", bins=50)
```

```sh
(array([2., 0., 0., 0., 1., 2., 2., 0., 2., 0., 0., 1., 2., 2., 1., 4., 3.,
        4., 2., 7., 2., 2., 5., 4., 2., 4., 3., 2., 1., 5., 3., 0., 3., 2.,
        1., 0., 0., 1., 3., 0., 1., 0., 0., 0., 0., 0., 0., 0., 0., 1.]),
 array([ 38.69307086,  40.37038529,  42.04769973,  43.72501417,
         45.4023286 ,  47.07964304,  48.75695748,  50.43427191,
         52.11158635,  53.78890079,  55.46621523,  57.14352966,
         58.8208441 ,  60.49815854,  62.17547297,  63.85278741,
         65.53010185,  67.20741628,  68.88473072,  70.56204516,
         72.23935959,  73.91667403,  75.59398847,  77.27130291,
         78.94861734,  80.62593178,  82.30324622,  83.98056065,
         85.65787509,  87.33518953,  89.01250396,  90.6898184 ,
         92.36713284,  94.04444727,  95.72176171,  97.39907615,
         99.07639058, 100.75370502, 102.43101946, 104.1083339 ,
        105.78564833, 107.46296277, 109.14027721, 110.81759164,
        112.49490608, 114.17222052, 115.84953495, 117.52684939,
        119.20416383, 120.88147826, 122.5587927 ]),
 <a list of 50 Patch objects>)
```

### Matrix in numpy

```py
# Create a 4x4 matrix filled with ones of type float
ones_matrix = np.matrix(np.ones((4, 4), dtype=float))
print(ones_matrix)
```

```sh
matrix([[1., 1., 1., 1.],
        [1., 1., 1., 1.],
        [1., 1., 1., 1.],
        [1., 1., 1., 1.]])
```

```py
# Get an ndarray view of the matrix and modify the third row (index 2)
np.asarray(ones_matrix)[2] = 2
print(ones_matrix)
```

```sh
matrix([[1., 1., 1., 1.],
        [1., 1., 1., 1.],
        [2., 2., 2., 2.],
        [1., 1., 1., 1.]])
```

### NumPy arange()

#### What is arange?

Sometimes, you want to create values that are evenly spaced within a defined interval. For instance, to create values from 0 to 10 with a step of 2 you can use `numpy.arange()`.

```py
# Python range object (start, stop, step)
even_range = range(0, 11, 2)
print(even_range)
```

```python
range(0, 11, 2)
```

```python
for value in even_range:
    print(value)
```

```sh
0
2
4
6
8
10
```

```py
# np.arange works like Python's range but returns a NumPy array
whole_numbers = np.arange(0, 20, 1)
print(whole_numbers)
```

```sh
array([ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14, 15, 16,
           17, 18, 19])
```

```py
natural_numbers = np.arange(1, 20, 1)
print(natural_numbers)
```

```py
odd_numbers = np.arange(1, 20, 2)
print(odd_numbers)
```

```sh
array([ 1,  3,  5,  7,  9, 11, 13, 15, 17, 19])
```

```py
even_numbers = np.arange(2, 20, 2)
print(even_numbers)
```

```sh
array([ 2,  4,  6,  8, 10, 12, 14, 16, 18])
```

### Creating sequence of numbers using linspace

```py
# np.linspace returns evenly spaced numbers over a specified interval
# For instance, 10 values from 1.0 to 5.0
np.linspace(1.0, 5.0, num=10)
```

```sh
array([1.        , 1.44444444, 1.88888889, 2.33333333, 2.77777778,
       3.22222222, 3.66666667, 4.11111111, 4.55555556, 5.        ])
```

```py
# endpoint=False excludes the stop value from the result
np.linspace(1.0, 5.0, num=5, endpoint=False)
```

```
array([1. , 1.8, 2.6, 3.4, 4.2])
```

```py
# LogSpace returns evenly spaced numbers on a log scale.
# Syntax: numpy.logspace(start, stop, num, endpoint)
np.logspace(2, 4.0, num=4)
```

```sh
array([  100.        ,   464.15888336,  2154.43469003, 10000.        ])
```

```py
# Check the item size (bytes per element) of an array
complex_array = np.array([1, 2, 3], dtype=np.complex128)
print(complex_array)
print('item size:', complex_array.itemsize)
```

```sh
array([1.+0.j, 2.+0.j, 3.+0.j])
16
```

```py
# Indexing and slicing a two-dimensional array
sample_array = np.array([(1, 2, 3), (4, 5, 6)])
print(sample_array)
```

```sh
array([[1, 2, 3],
       [4, 5, 6]])
```

```py
print('First row:', sample_array[0])
print('Second row:', sample_array[1])
```

```sh
First row: [1 2 3]
Second row: [4 5 6]
```

```py
print('First column:', sample_array[:, 0])
print('Second column:', sample_array[:, 1])
print('Third column:', sample_array[:, 2])
```

```sh
First column: [1 4]
Second column: [2 5]
Third column: [3 6]
```

### NumPy Statistical Functions with Example

NumPy has quite useful statistical functions for finding minimum, maximum, mean, median, percentile, standard deviation and variance, etc. from the given elements in the array.

Statistical functions:

- Min: `np.min()`
- Max: `np.max()`
- Mean: `np.mean()`
- Median: `np.median()`
- Variance: `np.var()`
- Percentile: `np.percentile()`
- Standard deviation: `np.std()`

```python
# Generate a normal distribution and compute statistics on sample_matrix
normal_samples = np.random.normal(5, 0.5, 100)

print('min:', sample_matrix.min())
print('max:', sample_matrix.max())
print('mean:', sample_matrix.mean())
print('median:', np.median(sample_matrix))
print('sd:', sample_matrix.std())
```

```sh
min: 1
max: 55
mean: 14.777777777777779
median: 7.0
sd: 18.913709183069525
```

```python
print(sample_matrix)
print('Column minima:', np.amin(sample_matrix, axis=0))
print('Column maxima:', np.amax(sample_matrix, axis=0))
print('=== Row ==')
print('Row minima:', np.amin(sample_matrix, axis=1))
print('Row maxima:', np.amax(sample_matrix, axis=1))
```

```sh
[[ 1  2  3]
 [ 4 55 44]
 [ 7  8  9]]
Column minima: [1 2 3]
Column maxima: [ 7 55 44]
=== Row ==
Row minima: [1 4 7]
Row maxima: [ 3 55  9]
```

### How to create repeating sequences?

```python
sequence = [1, 2, 3]

# Repeat the whole sequence two times
print('Tile:  ', np.tile(sequence, 2))

# Repeat each element of the sequence two times
print('Repeat:', np.repeat(sequence, 2))
```

```sh
Tile:   [1 2 3 1 2 3]
Repeat: [1 1 2 2 3 3]
```

### How to generate random numbers?

```python
# One random float in [0.0, 1.0)
one_random_num = np.random.random()
print(one_random_num)
```

```sh
0.6149403282678213
```

```python
# Random floats in [0.0, 1.0) with shape (2, 3)
random_matrix = np.random.random(size=[2, 3])
print(random_matrix)
```

```sh
[[0.13031737 0.4429537  0.1129527 ]
 [0.76811539 0.88256594 0.6754075 ]]
```

```python
# Randomly sample 10 vowels (with replacement)
print(np.random.choice(['a', 'e', 'i', 'o', 'u'], size=10))
```

```sh
['u' 'o' 'o' 'i' 'e' 'e' 'u' 'o' 'u' 'a']
```

```python
# Random floats in [0.0, 1.0) from a uniform distribution, shape (2, 2)
uniform_random = np.random.rand(2, 2)
print(uniform_random)
```

```sh
array([[0.97992598, 0.79642484],
       [0.65263629, 0.55763145]])
```

```python
# Random floats from the standard normal distribution, shape (2, 2)
standard_normal_random = np.random.randn(2, 2)
print(standard_normal_random)
```

```sh
array([[ 1.65593322, -0.52326621],
       [ 0.39071179, -2.03649407]])
```

```python
# Random integers in [0, 10) with shape (5, 3)
random_integers = np.random.randint(0, 10, size=[5, 3])
print(random_integers)
```

```sh
array([[0, 7, 5],
       [4, 1, 4],
       [3, 5, 3],
       [4, 3, 8],
       [4, 6, 7]])
```

```py
from scipy import stats

# Generate 1000 samples from a normal distribution
normal_samples = np.random.normal(5, 0.5, 1000)  # mean, std dev, number of samples

# Compute descriptive statistics
print('min:', np.min(normal_samples))
print('max:', np.max(normal_samples))
print('mean:', np.mean(normal_samples))
print('median:', np.median(normal_samples))
print('mode:', stats.mode(normal_samples))
print('sd:', np.std(normal_samples))
```

```sh
min:  3.557811005458804
max:  6.876317743643499
mean:  5.035832048106663
median:  5.020161980441937
mode:  ModeResult(mode=array([3.55781101]), count=array([1]))
sd:  0.489682424165213
```

```python
plt.hist(normal_samples, color="grey", bins=21)
plt.show()
```

![png](test_files/test_121_0.png)

```python
# numpy.dot(): Dot Product in Python using NumPy
# NumPy is a powerful library for matrix computation.
# For instance, you can compute the dot product with np.dot.
#
# Syntax: numpy.dot(x, y, out=None)
```

### Linear Algebra

1. Dot Product

```python
## Linear algebra
### Dot product: product of two one-dimensional arrays
vector_a = np.array([1, 2, 3])
vector_b = np.array([4, 5, 3])

# 1*4 + 2*5 + 3*3 = 23
np.dot(vector_a, vector_b)
```

### NumPy Matrix Multiplication with np.matmul()

```python
### Matmul: matrix product of two arrays
matrix_a = [[1, 2], [3, 4]]
matrix_b = [[5, 6], [7, 8]]

# Top-left element: 1*5 + 2*7 = 19
np.matmul(matrix_a, matrix_b)
```

```sh
array([[19, 22],
       [43, 50]])
```

```py
## Determinant of a 2x2 matrix
# For a 2x2 matrix [[a, b], [c, d]], determinant = a*d - b*c
# Example: 5*8 - 6*7 = 40 - 42 = -2
np.linalg.det(matrix_b)
```

```python
np.linalg.det(matrix_b)
```

```sh
-1.999999999999999
```

```python
# Create an 8x8 checkerboard pattern using slicing
checkerboard = np.zeros((8, 8))

# Set every other column in odd-indexed rows to 1
checkerboard[1::2, ::2] = 1
# Set every other column in even-indexed rows to 1 (offset by 1)
checkerboard[::2, 1::2] = 1

print(checkerboard)
```

```sh
array([[0., 1., 0., 1., 0., 1., 0., 1.],
       [1., 0., 1., 0., 1., 0., 1., 0.],
       [0., 1., 0., 1., 0., 1., 0., 1.],
       [1., 0., 1., 0., 1., 0., 1., 0.],
       [0., 1., 0., 1., 0., 1., 0., 1.],
       [1., 0., 1., 0., 1., 0., 1., 0.],
       [0., 1., 0., 1., 0., 1., 0., 1.],
       [1., 0., 1., 0., 1., 0., 1., 0.]])
```

```python
# Python list comprehension: add 2 to each number from 0 to 10
doubled_list = [x + 2 for x in range(0, 11)]
print(doubled_list)
```

```sh
[2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
```

```python
# The same operation is much simpler with NumPy vectorisation
range_array = np.array(range(0, 11))
print(range_array + 2)
```

```sh
array([ 2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12])
```

We use linear equations for quantities which have a linear relationship. Let's see the example below:

```python
temperature = np.array([1, 2, 3, 4, 5])
pressure = temperature * 2 + 5
print(pressure)
```

```sh
array([ 7,  9, 11, 13, 15])
```

```python
plt.plot(temperature, pressure)
plt.xlabel('Temperature in °C')
plt.ylabel('Pressure in atm')
plt.title('Temperature vs Pressure')
plt.xticks(np.arange(0, 6, step=0.5))
plt.show()
```

![png](test_files/test_141_0.png)

To draw the Gaussian normal distribution using NumPy. As you can see below, NumPy can generate random numbers. To create a random sample, we need the mean (mu), the standard deviation (sigma), and the number of data points.

```python
mu = 28
sigma = 15
num_samples = 100000

samples = np.random.normal(mu, sigma, num_samples)
ax = sns.distplot(samples)
ax.set(xlabel="x", ylabel='y')
plt.show()
```

![png](test_files/test_143_0.png)

# Summary

To summarise, the main differences between Python lists and NumPy arrays are:

1. Arrays support vectorised operations, while lists don’t.
1. Once an array is created, you cannot change its size. You will have to create a new array or overwrite the existing one.
1. Every array has one and only one dtype. All items in it should be of that dtype.
1. An equivalent NumPy array occupies much less space than a Python list of lists.
1. NumPy arrays support boolean indexing.

## 💻 Exercises: Day 24

1. Repeat all the examples

```