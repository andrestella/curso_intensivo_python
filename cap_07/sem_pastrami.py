pedidos_sanduiche = ['atum', 'pastrami', 'queijo', 'pastrami', 'picanha', 'pastrami', 'especial']
sanduiches_prontos = []

print("A lanchonete está sem pastrami para os sanduíches!\n")

# for sanduiche in pedidos_sanduiche:
#     if sanduiche == 'pastrami':
#         pedidos_sanduiche.remove('pastrami')
while 'pastrami' in pedidos_sanduiche:
    pedidos_sanduiche.remove('pastrami')

while pedidos_sanduiche:
    for sanduiche in pedidos_sanduiche:
        sanduiche_preparado = pedidos_sanduiche.pop()
        print("Preparei seu sanduíche: {}".format(sanduiche_preparado))
        sanduiches_prontos.append(sanduiche_preparado)

print("\nSegue abaixo os sanduíches preparados:")
for sanduíche in sanduiches_prontos:
    print("\t- " + sanduíche)