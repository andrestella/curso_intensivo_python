minhas_pizzas = ['mussarela', 'calabresa', 'atum']
friend_pizzas = minhas_pizzas[:]

minhas_pizzas.append('baiana')
friend_pizzas.append('aliche')

print("Minhas pizzas favoritas são:")
for pizza in minhas_pizzas:
    print("- " + pizza)

print("\nAs pizzas favoritas de meu amigo são:")
for pizza in friend_pizzas:
    print("- " + pizza)