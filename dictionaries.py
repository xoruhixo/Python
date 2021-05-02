# Create dict
person = {
    'first_name': 'Rachana',
    'last_name': 'Kumari',
    'age': 26
}

#print (person, type(person))
##Output {'first_name': 'Rachana', 'last_name': 'Kumari', 'age': 26} <class 'dict'>

# Use constructor
#person2 = dict(first_name='Ruhi', last_name='Kumari')
#print (person2, type(person2))
##Output {'first_name': 'Ruhi', 'last_name': 'Kumari'} <class 'dict'>

# # Get value
#print(person['first_name'])
##Output Rachana

#print(person.get('last_name'))
##Output Kumari

# Add key/value
person['phone'] = '555-555-5555'
print(person)
##Output {'first_name': 'Rachana', 'last_name': 'Kumari', 'age': 26, 'phone': '555-555-5555'}

# Get dict keys
print(person.keys())
##Output dict_keys(['first_name', 'last_name', 'age', 'phone'])

# Get dict items
print(person.items())
##Output dict_items([('first_name', 'Rachana'), ('last_name', 'Kumari'), ('age', 26), ('phone', '555-555-5555')])

# Copy dict
person2 = person.copy()
person2['city'] = 'Hyderabad'
print(person2)
##Output {'first_name': 'Rachana', 'last_name': 'Kumari', 'age': 26, 'phone': '555-555-5555', 'city': 'Hyderabad'}


# Remove item
del(person['age'])
print(person)
##Output {'first_name': 'Rachana', 'last_name': 'Kumari', 'phone': '555-555-5555'}

person.pop('phone')
print(person)
##Output {'first_name': 'Rachana', 'last_name': 'Kumari'}

# # Clear
person.clear()
print(person)
##Output {}

# # Get length
print(len(person2))
##Output 5

# List of dict
people = [
{'name': 'ABC', 'age': 30},
{'name': 'XYZ', 'age': 25}
         ]

print (people)
print(people[1]['name'])

##Output XYZ