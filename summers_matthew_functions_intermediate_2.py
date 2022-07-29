#I Update Values in Dictionaries and Lists
x = [ [5,2,3], [10,8,9] ] 
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

#1
print("Original: ", x)

x[1][0] = 15
print("New: ", x)
print("\n")


#2
print("Original:", students[0]['last_name'])

students[0]['last_name']='Bryant'
print("New:", students[0]['last_name'])
print("\n")


#3
print("Original:", sports_directory['soccer'][0])

sports_directory['soccer'][0] = 'Andres'
print("New:", sports_directory['soccer'][0])
print("\n")


#4
print("Original:", z)

z[0]['y'] = 30
print("New:", z)
print("\n")


#II Iterate Through a List of Dictionaries
students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

def iterateDictionary(some_list):
    for i in range(len(some_list)):
        students_dict = some_list[i]
        for key in students_dict:
            print(key, '-', students[i][key])
print(iterateDictionary(students))
print("\n")


#III Get Values From a List of Dictionaries
def iterateDictionary2(key_name, some_list):
    for i in range(len(some_list)):
        print(some_list[i][key_name])
print(iterateDictionary2('first_name', students))
print(iterateDictionary2('last_name', students))
print("\n")


#IV Iterate Through a Dictionary with List Values
dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def printInfo(some_dict):
    for key in some_dict:
        print(len(some_dict[key]), key.upper(), "\n")
        for val in some_dict[key]:
            print(val)
        print("\n")
print(printInfo(dojo))