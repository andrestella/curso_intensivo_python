# Para simplificar a tarefa, vamos supor que todos os valores da lista utilizam letras
# minúsculas. Ordenar uma lista em ordem alfabética é um pouco mais complicado
# quando existem valores que utilizam letras maiúsculas junto das minúsculas

# Ordenando uma lista em ordem alfabética de forma permanente com o método "sort()"
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)
cars.sort()
print(cars)
# Também podemos ordenar essa lista em ordem alfabética inversa
# - para isso devemos passar o argumento "reverse=True" ao método "sort()"
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)
cars.sort(reverse=True)
print(cars)

# Ordenando uma lista em ordem alfabética temporariamente com a função "sorted()"
cars = ['bmw', 'audi', 'toyota', 'subaru']
print("\nHere is the original list:")
print(cars)
print("Here is the sorted list:")
print(sorted(cars))
print("Here is the original list again:")
print(cars)
# Também podemos ordenar essa lista em ordem alfabética inversa
# - para isso devemos passar o argumento "reverse=True" à função "sorted()"
print("\n" + str(sorted(cars, reverse=True)))

# Exibindo uma lista em ordem inversa com o método "reverse()"
# - "reverse()" não reorganiza a lista em ordem alfabética inversa, ele simplesmente
# inverte a ordem da mesma
# - o método muda a ordem da lista de forma permanente, mas podemos restaurar
# a ordem original aplicando "reverse()" novamente
cars = ['bmw', 'audi', 'toyota', 'subaru']
print("\n" + str(cars))
cars.reverse()
print(cars)

# Obtendo o tamanho da lista com a função "len()"
cars = ['bmw', 'audi', 'toyota', 'subaru']
print("\n" + str(len(cars)))