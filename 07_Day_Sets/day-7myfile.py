# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

#1
print(len(it_companies))

#2
it_companies.add("Twitter")
print(it_companies)

#3
it_companies.update(['NVIDIA', 'Intel', 'Salesforce', 'Adobe', 'SAP', 'Cisco', 'Qualcomm','Broadcom', 'HP', 'Dell', 'Tesla', 'Netflix', 'Tencent', 'Alibaba','Samsung', 'Sony', 'Siemens', 'Palantir', 'OpenAI', 'DeepMind', 'Anthropic'])
print(it_companies)

#4
print(it_companies.pop())

#level2
#1
print(A.union(B))

#2
print(A.intersection(B))

#3
print("is A subset of B :",A.issubset(B))

#4
print("Is A and B disjoint set :",A.isdisjoint(B))

#5
print("Join A with B and B with A :",(A.difference(B)).join(B.difference(A)))