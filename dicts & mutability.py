# Dictionaries are mutable and there are no duplicates
# You can perform all the list functions on dictionaries (only difference is the key value pair)

school = {  # Or define a dict as school = dict('name'='Aima'); different notation
    'name': 'Aima',  # key:value
    'id': 1,
    'roll number': 10,
    'car': ['bmw', 'mer', 'lex']  # Lists can be used within dictionaries bc both are mutable
}
# print(school)
# print(type(school))
# print(school['name'])  # Print the value referenced by the key 'name'
print(len(school))  # Prints the number of key value PAIRS

