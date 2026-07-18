from functools import reduce
from operator import add
from typing import Any, Optional, Sequence, Union


def combine_values(*values: Union[str, tuple, list]) -> Union[str, tuple, list]:
    if not values:
        return ()
    first = values[0]
    first_type = type(first)
    if not all(isinstance(value, first_type) for value in values):
        raise TypeError(f"All values must share the same type, got mixed types with {first_type.__name__}.")
    return reduce(add, values)


def to_list(value: tuple) -> list:
    if not isinstance(value, tuple):
        raise TypeError("Expected a tuple value.")
    return list(value)


def slice_sequence(seq: Sequence, start: int, stop: Optional[int] = None) -> Sequence:
    if not isinstance(seq, (list, tuple, str)):
        raise TypeError("Sequence must be a list, tuple, or string.")
    return seq[start:stop]


def is_member(container: tuple, item: Any) -> bool:
    if not isinstance(container, tuple):
        raise TypeError("Membership container must be a tuple.")
    return item in container


def main() -> None:
    empty_tuple: tuple = ()

    name_sister = "Khushi"
    name_brother = "Yug"
    siblings = combine_values(name_sister, name_brother)

    name_father = "Vipul"
    name_mother = "Meena"
    family_members = combine_values(siblings, name_mother, name_father)

    fruits = (
        "apple",
        "banana",
        "orange",
        "grape",
        "mango",
        "pear",
        "peach",
        "plum",
        "papaya",
        "watermelon",
    )
    vegetables = ("carrot", "broccoli", "spinach", "potato", "onion", "bell pepper")

    food_stuff_tp = combine_values(fruits, vegetables)
    food_stuff_lt = to_list(food_stuff_tp)

    print(food_stuff_lt)

    print(slice_sequence(food_stuff_tp, 0, 3))
    print(slice_sequence(food_stuff_tp, -3))

    try:
        del food_stuff_tp
    except NameError:
        pass

    nordic_countries = ("Denmark", "Finland", "Iceland", "Norway", "Sweden")

    print(is_member(nordic_countries, "Estonia"))
    print(is_member(nordic_countries, "Iceland"))


if __name__ == "__main__":
    main()