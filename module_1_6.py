
# Работа со словарями

my_dict = {'Alex': 1963, 'Alena': 1967, 'Mary': 2004, 'Lola': 2000}

print(my_dict.get('Alex'))
print(my_dict.get('sasha', 'Нет такого в справочнике!'))

my_dict['Katy'] = 2011
my_dict['Lisa'] = 2011
del my_dict['Lola']
print(my_dict)

# Работа с множествами

my_set = {1, 2, 3, 4, 4, 4}

print(my_set)
my_set.discard(2)
print(my_set)
