#Q1

dog = {}

#Q2

dog['name']='Khushi'
dog['color']='white'
dog['breed']='Akita'
dog['leg']=4
dog["age"]=5
print(dog)

#Q3

student = {
    "first_name": "Yug",
    "last_name": "Shah",
    "gender": "Male",
    "age": 20,
    "marital_status": "Single",
    "skills": ["Python", "JavaScript"],
    "country": "India",
    "city": "Ahmedabad",
    "address": "Some Street, Some Area"
}

#Q4

print(len(student))

#Q5

print(type(student["skills"]))

#Q6

student['skills'].append("C++")
print(student["skills"])

#Q7

keys_list = list(student.keys())
print(keys_list)

#Q8

value_list = list(student.values())
print(value_list)

#Q9

student_list = list(student.items())
print(student_list)

#Q10

print(student.pop('last_name'))

#Q11
del dog

