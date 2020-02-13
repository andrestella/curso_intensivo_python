requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping == 'green peppers':
        print("Sorry, we are out of green peppers right now.")
    else:
        print("Adding {}.".format(requested_topping))

print("Finished making your pizza!\n")

# Verificando se uma lista não está vazia:
requested_toppings = []

if requested_toppings: # quando o nome de uma lista é usado em uma
# instrução "if", Python devolve 'True' se a lista contiver pelo menos
# um item; uma lista vazia é avaliada como 'False'
    for requested_topping in requested_toppings:
        print("Adding {}.".format(requested_topping))
    print("Finished making your pizza!\n")
else:
    print("Are you sure you want a plain pizza?\n")

# Usando várias listas:
available_toppings = ['mushrooms', 'olives', 'green peppers', 'pepperoni', 
                      'pineapple', 'extra cheese']
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print("Adding {}.".format(requested_topping))
    else:
        print("Sorry, we don't have {}.".format(requested_topping))

print("Finished making your pizza!")