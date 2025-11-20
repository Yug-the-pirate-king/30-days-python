
#level 1
# age = int(input("Enter your age: "))

# if age >= 18:
#     print("You are old enough to learn to drive.")
# else:
#     print("You need "+str(18-age)+" more years to learn to drive.")


# age_2 = int(input("Enter your age:"))

# if age_2-25==1:
#     print("You are 1 year older than me.")
# elif 25-age_2 == 1:
#     print("You are 1 year younger then me.")
# elif age_2 == 25:
#     print("We have the same age.")
# elif age_2>= 26:
#     print("You are "+str(age_2-25)+" years older than me.")
# else:
#     print("You are "+str(25-age_2)+" years younger then me.")

# a = int(input("Enter number one : "))
# b = int(input("Enter number two : "))

# print(str(a)+" is greater than "+str(b)) if a > b else print(str(b)+" is greater than "+str(a))

#level 2
# scores = int(input("Enter your scores :"))

# if scores <=100 and scores >= 80 :
#     print("A")
# elif scores <= 79 and scores >= 70 :
#     print("B")
# elif scores <= 69 and scores >= 60 :
#     print("C")
# elif scores <= 59 and scores >= 50 :
#     print("D")
# elif scores <= 49 and scores >= 0 :
#     print("F")

# Program to check the season based on month

# month = input("Enter the month: ").strip().capitalize()

# if month in ["September", "October", "November"]:
#     print("The season is Autumn.")
# elif month in ["December", "January", "February"]:
#     print("The season is Winter.")
# elif month in ["March", "April", "May"]:
#     print("The season is Spring.")
# elif month in ["June", "July", "August"]:
#     print("The season is Summer.")
# else:
#     print("Invalid month entered.")

# fruits = ['banana', 'orange', 'mango', 'lemon']

# user_fruits = input("Enter a fruits : ")

# if user_fruits in fruits:
#     print("fruit does exist.")
# else :
#     fruits.append(user_fruits)
#     print("fruit doesn't exist !, Added")
#     print(fruits)

#level3

person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
    }

if 'skills' in person:
    middle_index = len(person['skills']) // 2
    print(person['skills'][middle_index])
else:
    print("No Skill")