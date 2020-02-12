requested_topping = 'mushrooms'

if requested_topping != 'anchovies':
    print("Hold the anchovies!")

# Descobrindo se um valor em particular está em uma lista utilizando a 
# palavra reservada "in"
requested_toppings = ['mushrooms', 'onions', 'pineapple']
print('mushrooms' in requested_toppings)
print('pepperoni' in requested_toppings)

requested_toppings = ['mushrooms', 'extra cheese']

# Quando usar "if-elif-else" e quando usar uma série de instruções "if"?
# Se quiser que apenas um bloco de código seja executado, utilize uma
# cadeia "if-elif-else". Se mais de um bloco de código deve executar,
# utilize uma série de instruções "if" independentes.

if 'mushrooms' in requested_toppings:
    print("Adding mushrooms.")
if 'pepperoni' in requested_toppings:
    print("Adding pepperoni.")
if 'extra cheese' in requested_toppings:
    print("Adding extra cheese.")

print("Finished making your pizza!")