pratos = ('arroz', 'feijão', 'batata', 'carne', 'cenoura')
print(id(pratos))
for prato in pratos:
    print("- " + prato)

# pratos[0] = 'alface'

pratos = ('alface', 'macarrão', 'batata', 'carne', 'cenoura')
print("\n" + str(id(pratos)))
for prato in pratos:
    print("- " + prato)