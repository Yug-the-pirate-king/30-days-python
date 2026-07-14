def print_string_details(text: str) -> None:
    print(text)
    print(len(text))


def demonstrate_basic_strings() -> None:
    print_string_details("P")
    print_string_details("Hello, World!")
    print("I hope you are enjoying 30 days of python challenge")


def demonstrate_multiline_strings() -> None:
    multiline_string = """I am a teacher and enjoy teaching.
I didn't find anything as rewarding as empowering people.
That is why I created 30 days of python."""
    print(multiline_string)
    multiline_string = '''I am a teacher and enjoy teaching.
I didn't find anything as rewarding as empowering people.
That is why I created 30 days of python.'''
    print(multiline_string)


def demonstrate_concatenation() -> None:
    first_name = "Asabeneh"
    last_name = "Yetayeh"
    full_name = f"{first_name} {last_name}"
    print(full_name)
    print(len(first_name))
    print(len(last_name))
    print(len(first_name) > len(last_name))
    print(len(full_name))


def demonstrate_unpacking(text: str) -> None:
    first, second, third, fourth, fifth, sixth = text
    print(first)
    print(second)
    print(third)
    print(fourth)
    print(fifth)
    print(sixth)


def demonstrate_indexing(text: str) -> None:
    print(text[0])
    print(text[1])
    print(text[len(text) - 1])
    print(text[-1])
    print(text[-2])


def demonstrate_slicing(text: str) -> None:
    print(text[:3])
    print(text[3:6])
    print(text[-3:])
    print(text[3:])
    print(text[0:6:2])


def demonstrate_escape_sequences() -> None:
    print("I hope every one enjoying the python challenge.\nDo you ?")
    print("Days\tTopics\tExercises")
    for day in range(1, 5):
        print(f"Day {day}\t3\t5")
    print("This is a back slash  symbol (\\)")
    print('In every programming language it starts with \"Hello, World!\"')


def demonstrate_string_formatting() -> None:
    first_name = "Asabeneh"
    last_name = "Yetayeh"
    job = "teacher"
    country = "Finland"
    sentence = f"I am {first_name} {last_name}. I am a {job}. I live in {country}."
    print(sentence)

    radius = 10
    pi = 3.14
    area = pi * radius ** 2
    print(f"The area of circle with {radius} is {area}")


def display(value: object) -> None:
    print(value)


CHALLENGE = "thirty days of python"
CHALLENGE_TITLE = "Thirty Days Of Python"
CHALLENGE_WITH_TABS = "thirty\tdays\tof\tpython"


def demonstrate_string_methods() -> None:
    display(CHALLENGE.capitalize())

    display(CHALLENGE.count("y"))
    display(CHALLENGE.count("y", 7, 14))
    display(CHALLENGE.count("th"))

    display(CHALLENGE.endswith("on"))
    display(CHALLENGE.endswith("tion"))

    display(CHALLENGE_WITH_TABS.expandtabs())
    display(CHALLENGE_WITH_TABS.expandtabs(10))

    display(CHALLENGE.find("y"))
    display(CHALLENGE.find("th"))

    display("ThirtyDaysPython".isalnum())
    display("30DaysPython".isalnum())
    display(CHALLENGE.isalnum())
    display("thirty days of python 2019".isalnum())

    display(CHALLENGE.isalpha())
    display("123".isalpha())

    display(CHALLENGE.find("y"))
    display(CHALLENGE.find("th"))

    display("Thirty".isdigit())
    display("30".isdigit())

    display("10".isdecimal())
    display("10.5".isdecimal())

    display("30DaysOfPython".isidentifier())
    display("thirty_days_of_python".isidentifier())

    display(CHALLENGE.islower())
    display("Thirty days of python".islower())

    display(CHALLENGE.isupper())
    display("THIRTY DAYS OF PYTHON".isupper())

    display("10".isnumeric())
    display("ten".isnumeric())

    web_tech = ["HTML", "CSS", "JavaScript", "React"]
    display("#, ".join(web_tech))

    display(" thirty days of python ".strip("y"))

    display(CHALLENGE.replace("python", "coding"))

    display(CHALLENGE.split())

    display(CHALLENGE.title())

    display(CHALLENGE.swapcase())
    display(CHALLENGE_TITLE.swapcase())

    display(CHALLENGE.startswith("thirty"))
    display("30 days of python".startswith("thirty"))


def main() -> None:
    demonstrate_basic_strings()
    demonstrate_multiline_strings()
    demonstrate_concatenation()
    demonstrate_unpacking("Python")
    demonstrate_indexing("Python")
    demonstrate_slicing("Python")
    demonstrate_escape_sequences()
    demonstrate_string_formatting()
    demonstrate_string_methods()


if __name__ == "__main__":
    main()