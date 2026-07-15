# Helper functions for safe input handling and reusable logic


def get_int_input(prompt):
    """Prompt the user until a valid integer is entered."""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a whole number.")


def check_driving_eligibility(age):
    """Print whether the user is old enough to learn to drive."""
    if age >= 18:
        print("You are old enough to learn to drive.")
    else:
        print(f"You need {18 - age} more years to learn to drive.")


def compare_ages(my_age, other_age):
    """Compare another person's age to mine and print the difference."""
    diff = other_age - my_age
    if diff == 0:
        print("We have the same age.")
    elif diff == 1:
        print("You are 1 year older than me.")
    elif diff == -1:
        print("You are 1 year younger then me.")
    elif diff > 1:
        print(f"You are {diff} years older than me.")
    else:
        print(f"You are {-diff} years younger then me.")


def compare_numbers(a, b):
    """Print which of two numbers is greater."""
    if a > b:
        print(f"{a} is greater than {b}")
    else:
        print(f"{b} is greater than {a}")


def get_grade(score):
    """Return the letter grade for a score between 0 and 100."""
    if not 0 <= score <= 100:
        return "Invalid score. Please enter a value between 0 and 100."
    if score >= 80:
        return "A"
    elif score >= 70:
        return "B"
    elif score >= 60:
        return "C"
    elif score >= 50:
        return "D"
    else:
        return "F"


def get_season(month):
    """Return the season for a given month name."""
    month = month.strip().capitalize()
    seasons = {
        "Autumn": ["September", "October", "November"],
        "Winter": ["December", "January", "February"],
        "Spring": ["March", "April", "May"],
        "Summer": ["June", "July", "August"],
    }
    for season, months in seasons.items():
        if month in months:
            return f"The season is {season}."
    return "Invalid month entered."


def manage_fruit_list(fruits, fruit):
    """Add a fruit to the list if it does not already exist."""
    fruit = fruit.strip().lower()
    if not fruit:
        print("Invalid fruit name.")
        return
    if fruit in fruits:
        print("fruit does exist.")
    else:
        fruits.append(fruit)
        print("fruit doesn't exist !, Added")
        print(fruits)


def get_middle_skill(person):
    """Print the middle skill from the person's skill list, if available."""
    skills = person.get("skills")
    if not skills:
        print("No Skill")
        return
    middle_index = len(skills) // 2
    print(skills[middle_index])


# Level 1
# age = get_int_input("Enter your age: ")
# check_driving_eligibility(age)

# other_age = get_int_input("Enter your age:")
# compare_ages(my_age=25, other_age=other_age)

# a = get_int_input("Enter number one : ")
# b = get_int_input("Enter number two : ")
# compare_numbers(a, b)


# Level 2
# score = get_int_input("Enter your scores :")
# print(get_grade(score))

# month = input("Enter the month: ")
# print(get_season(month))

# fruits = ['banana', 'orange', 'mango', 'lemon']
# user_fruit = input("Enter a fruit : ")
# manage_fruit_list(fruits, user_fruit)


# Level 3
person = {
    "first_name": "Asabeneh",
    "last_name": "Yetayeh",
    "age": 250,
    "country": "Finland",
    "is_marred": True,
    "skills": ["JavaScript", "React", "Node", "MongoDB", "Python"],
    "address": {
        "street": "Space street",
        "zipcode": "02210",
    },
}

get_middle_skill(person)