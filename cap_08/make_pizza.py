# Passando um número arbitrário de argumentos
def make_pizza(*toppings): # o asterisco (*) diz a Python para criar
# uma tupla vazia e reunir os valores recebidos nessa tupla
    """ Exibe uma tupla com os ingredientes pedidos. """
    print(toppings)

make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')

def make_pizza(*toppings):
    """ Apresenta a pizza que estamos prestes a preparar. """
    print("\nMaking a pizza with the following toppings:")
    for topping in toppings:
        print("- " + topping)

make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')

# Misturando argumentos posicionais e arbitrários
def make_pizza(size, *toppings): # o parâmetro que aceita um número 
# arbitrário de argumentos deve ser colocado por último
    """ Apresenta a pizza que estamos prestes a preparar. """
    print("\nMaking a {}-inch pizza with the following toppings:".
        format(size))
    for topping in toppings:
        print("- " + topping)

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')