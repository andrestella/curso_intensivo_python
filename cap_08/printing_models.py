# Código sem utilizar funções:
# Começa com alguns designs que devem ser impressos
unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []

# Simula a impressão de cada design, até que não haja mais nenhum
# Transfere cada design para 'completed_models' após a impressão
while unprinted_designs:
    current_design = unprinted_designs.pop()
    # Simula a criação de uma impresssão 3D a partir do design
    print("Printing model: {}".format(current_design))
    completed_models.append(current_design)

# Exibe todos os modelos finalizados
print("\nThe following models have been printed:")
for completed_model in completed_models:
    print(completed_model)

print("\n")

# Código utilizando funções:
def print_models(unprinted_designs, completed_models):
    """
    Simula a impressão de cada design, até que não haja mais nenhum.
    Transfere cada design para 'completed_models' após a impressão.
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        # Simula a criação de uma impresssão 3D a partir do design
        print("Printing model: {}".format(current_design))
        completed_models.append(current_design)

def show_completed_models(completed_models):
    """ Exibe todos os modelos finalizados. """
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)

unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []

print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)

print("\n")

print(unprinted_designs)
print(completed_models)

print("\n")

# Evitando que uma função modifique uma lista
unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []

print_models(unprinted_designs[:], completed_models) # enviar uma cópia da lista para a função
show_completed_models(completed_models)

print("\n")

print(unprinted_designs)
print(completed_models)
# Apesar de poder preservar o conteúdo de uma lista passando uma cópia dela para suas funções,
# você deve passar a lista original para as funções, a menos que tenha um motivo específico
# para passar uma cópia. Para uma função, é mais eficiente trabalhar com uma lista existente
# a fim de evitar o uso de tempo e de memória necessários para criar uma cópia separada, em
# especial quando trabalhamos com listas grandes.