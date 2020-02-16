# Passando uma lista para uma função
def greet_users(names):
    """ Exibe uma saudação simples a cada usuário da lista. """
    for name in names:
        msg = "Hello, " + name.title() + "!"
        print(msg)

usernames = ['hannah', 'ty', 'margot']
greet_users(usernames)

greet_users('andré stella') # aqui fatiamos a string em cada um de seus caracteres