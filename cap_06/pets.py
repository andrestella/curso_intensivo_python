pets = []

pet = {
    'nome': 'pequeno',
    'tipo': 'cachorro',
    'dono': 'andré',
    }
pets.append(pet)

pet = {
    'nome': 'rápido',
    'tipo': 'gato',
    'dono': 'manoel',
    }
pets.append(pet)

pet = {
    'nome': 'cantor',
    'tipo': 'pássaro',
    'dono': 'joão',
    }
pets.append(pet)

for pet in pets:
    print("\nInformações sobre o {}:".format(pet['nome'].title()))
    for key, value in pet.items():
        print("\t{}: {}".format(key, value))