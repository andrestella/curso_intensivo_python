favorite_numbers = {
    'andré': [40, 10, 7],
    'andré_pai': [70, 35, 20],
    'maria': [60, 54],
    'henri': [30, 10, 7],
    'nádia': [35, 20],
    }

for key, values in favorite_numbers.items():
    print("\nOs números favoritos de {} são:".format(key.title()))
    for numero in values:
        print("\t- " + str(numero))