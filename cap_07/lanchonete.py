pedidos_sanduiche = ['atum', 'queijo', 'picanha', 'especial']
sanduiches_prontos = []

while pedidos_sanduiche:
    for sanduiche in pedidos_sanduiche:
        sanduiche_preparado = pedidos_sanduiche.pop()
        print("Preparei seu sanduíche: {}".format(sanduiche_preparado))
        sanduiches_prontos.append(sanduiche_preparado)

print("\nSegue abaixo os sanduíches preparados:")
for sanduíche in sanduiches_prontos:
    print("\t- " + sanduíche)