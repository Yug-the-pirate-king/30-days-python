"""Day 1 - 30DaysOfPython Challenge.

This script demonstrates basic arithmetic operations and the built-in
types of common Python literals.
"""


def demonstrate_arithmetic():
    """Print sample results for basic arithmetic operators."""
    print(3 + 2)   # addition
    print(3 - 2)   # subtraction
    print(3 * 2)   # multiplication
    print(3 / 2)   # division
    print(3 ** 2)  # exponentiation
    print(3 % 2)   # modulus
    print(3 // 2)  # floor division


def demonstrate_data_types():
    """Print the built-in types of common Python literals."""
    print(type(10))  # int
    print(type(3.14))  # float
    print(type(1 + 3j))  # complex
    print(type("Asabeneh"))  # string
    print(type([1, 2, 3]))  # list
    print(type({"name": "Asabeneh"}))  # dict
    print(type({9.8, 3.14, 2.7}))  # set
    print(type((9.8, 3.14, 2.7)))  # tuple
    print(type(3 == 3))  # bool
    print(type(3 >= 3))  # bool


def main():
    """Run all Day 1 demonstrations."""
    demonstrate_arithmetic()
    demonstrate_data_types()


if __name__ == "__main__":
    main()