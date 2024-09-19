
immutable_var = 1, 2, 'неизменяемая строка', 1.5, True, False
print('immutable tuple:', immutable_var)

# immutable_var[0] = 2
# TypeError: 'tuple' object does not support item assignment - элементы кортежа не изменяются

mutable_list = [1 > 0, 0 > 1, 5 / 2, 5, 2, 'изменяемая строка']
print('mutable liste:', mutable_list)
