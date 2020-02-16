def make_pizza(size, *toppings): 
    """ Apresenta a pizza que estamos prestes a preparar. """
    print("\nMaking a {}-inch pizza with the following toppings:".
        format(size))
    for topping in toppings:
        print("- " + topping)