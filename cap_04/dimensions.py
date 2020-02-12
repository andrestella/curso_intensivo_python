dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])

for dimension in dimensions:
    print(dimension)

# Não é possível alterar qualquer dos itens de uma tupla
# O código abaixo gera um erro de tipo:
# dimensions[0] = 250

# Sobrescrevendo uma tupla
# Embora não seja possível modificar uma tupla, podemos atribuir um novo valor
# a uma variável que armazena uma tupla. Portanto, se quiséssemos alterar nossas
# dimensões, poderíamos redefinir a tupla toda:
dimensions = (200, 50)
print("\nOriginal dimensions:")
print(id(dimensions))
for dimension in dimensions:
    print(dimension)

dimensions = (400, 100)
print("\nModified dimensions:")
print(id(dimensions))
for dimension in dimensions:
    print(dimension)