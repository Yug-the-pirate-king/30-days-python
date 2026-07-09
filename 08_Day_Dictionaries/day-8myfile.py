# Exercise 1: Create an empty dictionary for a pet.
pet_dog = {}

# Exercise 2: Populate the pet dictionary with details.
pet_dog["name"] = "Khushi"
pet_dog["color"] = "white"
pet_dog["breed"] = "Akita"
pet_dog["legs"] = 4
pet_dog["age"] = 5
print(pet_dog)

# Exercise 3: Create a student profile dictionary.
student_profile = {
    "first_name": "Yug",
    "last_name": "Shah",
    "gender": "Male",
    "age": 20,
    "marital_status": "Single",
    "skills": ["Python", "JavaScript"],
    "country": "India",
    "city": "Ahmedabad",
    "address": "Some Street, Some Area",
}

# Exercise 4: Print the number of keys in the student profile.
print(len(student_profile))

# Exercise 5: Print the data type of the 'skills' value.
print(type(student_profile["skills"]))

# Exercise 6: Add a new skill and display the updated skills list.
student_profile["skills"].append("C++")
print(student_profile["skills"])

# Exercise 7: Extract all dictionary keys into a list.
student_keys = list(student_profile.keys())
print(student_keys)

# Exercise 8: Extract all dictionary values into a list.
student_values = list(student_profile.values())
print(student_values)

# Exercise 9: Extract all key-value pairs as a list of tuples.
student_items = list(student_profile.items())
print(student_items)

# Exercise 10: Remove and print the 'last_name' entry.
print(student_profile.pop("last_name"))

# Exercise 11: Delete the pet dictionary to free the variable.
del pet_dog