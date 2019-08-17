# # key, value, pairs

# people = {}

# print(people)

# people = {
#     'hayley': 'lead instructor',
#     'nanwen': 'wears checkered shirts',
# }

# print(people)

# #add things to dictionary
# people['chloe'] = 'wears classes'

# print(people)

# people['hayley'] = 'wears red'

# print(people)

# #print only value associated with specific key
# print(people['chloe'])

#task 1 - use a for loop to print out each key and value in dictionary

# countries = {
#     'spain': 'spanish',
#     'america': 'english',
#     'japan': 'japanese',
#     'korea': 'korean',
#     'sweden': 'swedish'
# }

# for country,language in countries.items():
#     print (country+":", language)

#or

# for country in countries:
#     print('{key}: {value}'.format(
#         key = country,
#         value = countries[country]
#         )
#     )

# task 2: given a list of names, create a dictoinary wher the key
# is the index and the value is the names i.e. after adding
# the first name, the dictionary would look liike
# {0: 'chloe'}

# names = ['sarah', 'angela', 'hayley', 'brad', 'janet']


# name_dictionary = dict(enumerate(names,1))

# for index, name in name_dictionary.items():
#     print(f'{index}: {name}')


# task 3: 
# given a list of tuples, create a dictionary where the key
# is the first value in the tuple and the value is the second
# i.e. after adding the first item the dictionary would look like 
# this: {'chloe': 'wears glasses'}

# people = [
#     ('chloe', 'wears glasses'),
#     ('maddy', 'is sitting next to beverley'),
#     ('cass', 'is online'),
#     ('marc', 'is mentoring')
# ]

# people_dictionary = dict(people)

# print(people_dictionary)

# peep_dictionary = {}
# for tupple in people:
#     key = tupple[0]
#     variable = tupple[1]
#     peep_dictionary[key] = variable

# print(peep_dictionary)


# for person in people_dictionary:
#     print(f'{person}: {people_dictionary[person]}')

# names = ['sarah', 'angela', 'hayley', 'brad', 'janet']

# descriptions = ['a', 'b', 'c', 'd', 'e']

# print(dict(zip(names,descriptions)))

# Task 4:
# given a list of typles, create a dictionary of dictionaries
# where the first value in the tuple is the key a dictionary
# containing the second value in the tuple is the value for a
# 'description' key in the dictionary
# i.e. after adding the first item the dictionary would look like this:
# result = {
#     'chloe': {
#         'description': 'wears glasses'
#     }
# }

a_list_of_tuples = [
    ('marc', 'is mentoring'),
    ('chloe', 'wears glasses'),
    ('maddy', 'is sitting next to beverly'),
    ('cass', 'is online')
]

# peoplebook = {}
# descrip_dict = {}
# for people in a_list_of_tuples:
#     describe = people[1]
#     descrip_dict ['description: '] = people [1]
#     name_key = people[0]
#     peoplebook [name_key] = descrip_dict

# peoplebook = {}
# for people in a_list_of_tuples:
#     descrip_dict = {}
#     descrip_dict {'description': people[1]}
#     name_key = people[0]
#     peoplebook [name_key] = descrip_dict

# or 

peoplebook = {}
for name, desc in a_list_of_tuples:
    peoplebook [name] = {'description': desc}

print(peoplebook)

# peep_dictionary = {}
# for tupple in people:
#     key = tupple[0]
#     variable = tupple[1]
#     peep_dictionary[key] = variable

# print(peep_dictionary)

# print(peep_dictionary)
