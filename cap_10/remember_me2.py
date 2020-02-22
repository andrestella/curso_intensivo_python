import json

# Carrega o nome do usuário se já foi armazenado anteriormente.
# Caso contrário, pede que o usuário forneça o nome e armazena essa informação.
filename = 'username2.json'

try:
    with open(filename) as f_obj:
        username = json.load(f_obj)        
except FileNotFoundError:
    username = input("What is your name? ")
    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)
        print("We'll remember you when you come back, {}!".format(username))
else:
    print("Welcome back, {}!".format(username))