motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

# Modificando elementos de uma lista
motorcycles[0] = 'ducati'
print(motorcycles)

# Concatenando elementos no final da lista
motorcycles.append('honda')
print(motorcycles)

# Inserindo elementos em qualquer posição da lista
motorcycles.insert(0, 'bmw')
print(motorcycles)

motorcycles.insert(-1, 'yamaha') # insere o elemento uma posição antes do último da lista
# motorcycles.insert(len(motorcycles), 'yamaha') # insere o elemento no final da lista
print(motorcycles)

# Removendo um item usando a instrução "del"
# - posição do item conhecida
# - não podemos mais acessar o valor que foi removido
del motorcycles[0]
print(motorcycles)

del motorcycles[1]
print(motorcycles)

# Removendo um item com o método "pop()"
# - remove o último item da lista
# - permite que você trabalhe com esse item depois da remoção
popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)
last_owned = motorcycles.pop()
print("The last motorcycle I owned was a {}.".format(last_owned.title()))

# Removendo itens de qualquer posição em uma lista com o método "pop()"
first_owned = motorcycles.pop(0)
print("The first motorcycle I owned was a {}.".format(first_owned.title()))
print(motorcycles)

#Removendo um item de acordo com o valor com o método "remove()"
# - o método "remove()" apaga apenas a primeira ocorrência do valor
motorcycles = ['honda', 'ducati', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)

motorcycles.remove('ducati')
print(motorcycles)

# Trabalhando com o item depois de utilizar o método "remove()"
too_expensive = 'suzuki'
motorcycles.remove(too_expensive)
print(motorcycles)
print("A {} is too expensive for me.".format(too_expensive.title()))