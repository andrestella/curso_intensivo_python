favorite_places = {
    'andré': ['são paulo', 'curitiba', 'ribeirão preto'],
    'maria': ['são paulo', 'orlândia'],
    'henri': ['são paulo', 'ribeirão preto', 'minas gerais'],
    }

for key, values in favorite_places.items():
    print("\nOs lugares favoritos de {} são:".format(key.title()))
    for lugar in values:
        print("\t- " + lugar.title())