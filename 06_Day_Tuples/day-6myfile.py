#1
empty_tuple = tuple()

#2
name_sister = ('Khushi')
name_brother = ('Yug')
#3
siblings = name_sister+name_brother

#4
#1

#5
name_father = ('Vipul')
name_mother = ('Meena')

family_members = siblings + name_mother + name_father

#level 2
fruits = ("apple", "banana", "orange", "grape", "mango", "pear", "peach", "plum", "papaya", "watermelon")
vegetables = ("carrot", "broccoli", "spinach", "potato", "onion", "bell pepper")

food_stuff_tp = fruits + vegetables

#print(food_stuff_tp)

#3
food_stuff_lt = list(food_stuff_tp)

print(food_stuff_lt)

#4

#5
print(food_stuff_tp[0:3])
print(food_stuff_tp[-3:])

#6
del food_stuff_tp

#7
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')

print('Estonia' in nordic_countries)
print('Iceland' in nordic_countries)
