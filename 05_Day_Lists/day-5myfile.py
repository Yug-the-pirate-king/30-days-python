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

#16
companies.sort()

#17
companies.sort(reverse=True)

#18
print(companies[0:3])

#19
print(companies[-1:-3])

#20
#n = int(len(companies))
#print(companies[n/2,(n/2)+1])

#21
companies.pop(0)

#22
companies.pop(4)

#23
companies.pop()

#24
companies.clear()

#25
del companies