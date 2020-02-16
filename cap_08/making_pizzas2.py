# Importando funções específicas
from pizza import make_pizza
# Podemos importar mais de uma função de um módulo separando o nome de cada
# função com uma vírgula:
# from 'nome_do_módulo' import 'função_0', 'função_1', 'função_2'

# Com essa sintaxe não precisamos usar a notação de ponto (.) ao chamar uma função
make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')