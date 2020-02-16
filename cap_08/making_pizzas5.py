# Importando todas as funções de um módulo
from pizza import * # como todas as funções são importadas, podemos chamar
# qualquer função pelo nome, sem usar a notação de ponto (.)

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

# - É melhor não usar essa abordagem quando trabalhar com módulos maiores,
# que não foram escritos por você
# - A melhor abordagem é importar a função ou as funções que você quiser
# ou importar o módulo todo e usar a notação de ponto