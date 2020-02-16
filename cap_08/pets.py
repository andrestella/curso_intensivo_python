def describle_pet(animal_type, pet_name):
    """ Exibe informações sobre uma animal de estimação. """
    print("\nI have a {}.".format(animal_type))
    print("My {}'s name is {}.".format(animal_type, pet_name.title()))

# Argumentos posicionais
describle_pet('hamster', 'harry')
describle_pet('dog', 'willie')
# Se alterarmos a ordem quando utilizarmos argumentos posicionais, o resultado
# é diferente do esperado:
describle_pet('harry', 'hamster')

# Argumentos nomeados (a ordem dos argumentos não importa)
describle_pet(animal_type='hamster', pet_name='harry')
describle_pet(pet_name='harry', animal_type='hamster')

# Utilizando valores default
def describle_pet(pet_name, animal_type='dog'): # qualquer parâmetro com valor default
# deverá ser listado após todos os parâmetros que não tenham valores default
    """ Exibe informações sobre uma animal de estimação. """
    print("\nI have a {}.".format(animal_type))
    print("My {}'s name is {}.".format(animal_type, pet_name.title()))

describle_pet(pet_name='willie')
describle_pet('willie')
describle_pet('harry', 'hamster')
describle_pet(pet_name='harry', animal_type='hamster')
describle_pet(animal_type='hamster', pet_name='harry')