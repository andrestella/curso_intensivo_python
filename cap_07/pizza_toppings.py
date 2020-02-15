print("\nForneça os ingredientes da pizza. Quando finalizar digite 'quit'.")

toppings = []

while True:
    ingrediente = input("\nInforme o ingrediente: ")
    if ingrediente == 'quit':
        break
    if ingrediente in toppings:
        print("Ingrediente já informado.")
        continue
    toppings.append(ingrediente)
    print("O ingrediente {} foi adicionado à pizza!".format(ingrediente))

if toppings:
    print("\nA pizza contém {} ingredientes: ".format(len(toppings)))
    for ingrediente in toppings:
        print("\t- " + ingrediente)
else:
    print("\nNão foi informado nenhum ingrediente!")