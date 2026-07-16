def _normalize_name(name, field_name):
    if not isinstance(name, str):
        raise TypeError(f"{field_name} must be a string, got {type(name).__name__}")
    stripped = name.strip()
    if not stripped:
        raise ValueError(f"{field_name} cannot be empty or whitespace")
    return stripped


def greet_person(firstname, lastname):
    first = _normalize_name(firstname, "firstname")
    last = _normalize_name(lastname, "lastname")
    return f'{first} {last}, welcome to 30DaysOfPython Challenge!'
