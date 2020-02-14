# Informações aninhadas
# Uma lista em um dicionário:

# Armazena informações sobre uma pizza que está sendo pedida
pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese'],
    }

# Resume o pedido
print("You ordered a {}-crust pizza with the following toppings:"
    .format(pizza['crust']) )
for topping in pizza['toppings']:
    print("\t- " + topping)