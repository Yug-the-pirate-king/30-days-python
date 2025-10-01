#1
# a,b,c,d = 'Thirty', 'Days', 'Of', 'Python'

# print('{} {} {} {}'.format(a,b,c,d))

#2
# e,f,g = 'Coding', 'For' , 'All'
# print('{} {} {}'.format(e,f,g))

#3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31
company = "Coding For All"
print(company)
print(len(company))
print(company.upper())
print(company.lower())
print(company.capitalize())
print(company.title())
print(company.swapcase())
print(company[0:6])
print(company.find('Coding'))
print(company.replace('Coding','Python'))
print(company.split())
print("Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon".split(','))
print(company[0])
print("The last index is : ",len(company)-1)
print(company[10])
print("PFE → Python For Everyone")
print("C4A → Coding For All")
print(company.index('C'))
print(company.index('F'))
print("Coding For All People".rfind("l"))
print('You cannot end a sentence with because because because is a conjunction'.find("because"))
print('You cannot end a sentence with because because because is a conjunction'.rfind("because"))
print('You cannot end a sentence with because because because is a conjunction'.replace("because because because", ""))
print(company.startswith("Coding"))
print(company.endswith('coding'))
print('   Coding For All      '.strip())
print('30DaysOfPython'.isidentifier())
print('thirty_days_of_python'.isidentifier())

