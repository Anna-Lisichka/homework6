# Работа со Словарями:
my_dict = {'Anna':1993, 'Sveta':2002, 'Kate':1980}
print(my_dict)

print(my_dict['Sveta'])

print(my_dict.get('Olga'))

my_dict.update({'Piter': 1996, 'Vasya': 1968})
print(my_dict)

del_element = my_dict.pop('Anna')
print(del_element)
print(my_dict)


# Работа со Множествами:
my_set = {'learn', 24, 'learn', 5, 5, 7.812}
print(my_set)

my_set.update({'sun', (17, 2, 5, 5)})
my_set.discard('learn')
print(my_set)