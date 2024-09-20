
# Работа со словарями

my_dict = {'Alex': 1963, 'Alena': 1967, 'Mary': 2004, 'Lola': 2000}
print('Dict:', my_dict)
print('Existing value:', my_dict.get('Alex'))
print('Not existing value:', my_dict.get('sasha'))

my_dict['Katy'] = 2011
my_dict['Lisa'] = 2011
print(my_dict)
deleted_pair = my_dict.pop('Lola')
print('Deleted value:', deleted_pair)
print('Modified dictionary:', my_dict)

# Работа с множествами

print()
my_set = {1, 2.5, 'Hello', 'Hello', True, False, False, 1, 4}
print('Set:', my_set)
my_set.discard(2.5)
print('Modified set:', my_set)