empty_list = list()

#2
list = ["item1","item2","item3","item4","item5"]

#3
print(len(list))

#4
print(list[0:5:2])

#5
mixed_data_types =["Yug Shah",18,5.8,False,"103 Goare apt,90 feet Road,Bhyander(w)"]

#6
companies = ['Facebook', 'Google', 'Microsoft', 'Apple','IBM', 'Oracle ','Amazon']

#7
print(companies)

#8
print(len(companies))

#9
print(companies[0:7:3])

#10
companies[0]="Netflix"
print(companies)

#11
companies.append("TCS")

#12
companies.insert(4,"Infosys")

#13
companies[4] = companies[4].upper()

#14
companies += "#"

#15
print(companies.index('Google'))
