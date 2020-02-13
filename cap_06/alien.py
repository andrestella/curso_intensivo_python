alien_0 = {'color': 'green', 'points': 5}

# Acessando valores em um dicionário
print(alien_0['color'])
print(alien_0['points'])

print(alien_0)

# Adicionando novos pares chave-valor
alien_0['x_position'] = 0
alien_0['y_position'] = 25

print(alien_0)

# Começando com um dicionário vazio:
alien_1 = {}

alien_1['color'] = 'red'
alien_1['points'] = 10
alien_1['x_position'] = 15
alien_1['y_position'] = 5

print(alien_1)

# Modificando valores em um dicionário:
alien_1['color'] = 'yellow'
print(alien_1)

# Removendo pares chaves-valor:
del alien_0['points']
del alien_1['points']
print(alien_0)
print(alien_1)