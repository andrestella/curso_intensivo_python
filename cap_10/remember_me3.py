# Refatoração do programa 'remember_me2.py'

import json

def get_stored_username():
    """ Obtém o nome do usuário já armazenado se estiver disponível. """
    filename = 'username4.json'
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        return None
        # Essa é uma boa prática: uma função deve devolver o valor esperado
        # ou 'None'. Isso nos permite fazer um teste simples com o valor de
        # retorno da função.
    else:
        return username

def get_new_username():
    """ Pede um novo nome de usuário. """
    username = input("What is your name? ")
    filename = 'username4.json'
    with open(filename, 'w') as f_obj:
            json.dump(username, f_obj)
    return username

def check_username(username):
    """ Verificar se o nome do usuário está correto. """
    # Inclusão da função para evitar as instruções 'if' aninhadas da
    # versão anterior.
    correct = input("Are you {}? (yes/no) ".format(username))
    if correct == 'yes':
        return username

def greet_user():
    """ Saúda o usuário pelo nome. """
    username = get_stored_username()
    if username:
        username = check_username(username)
    if username:        
        print("Welcome back, {}!".format(username))
        return
    username = get_new_username()
    print("We'll remember you when you come back, {}!".format(username))
    
greet_user()