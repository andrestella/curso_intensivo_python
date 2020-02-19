from random import randint 

class Die():
    """ Modelando um simples dado de seis lados. """


    def __init__(self, sides=6):
        """ Inicializa os atributos que definem um dado. """
        self.sides = sides


    def roll_die(self):
        """ Exibe um número aleatório entre 1 e o número de lados do dado. """
        return randint(1, self.sides)


d6 = Die()
results = [d6.roll_die() for value in range(10)]
print("10 jogadas de um dado de 6 lados:")
print(results)

d10 = Die(sides=10)
results = [d10.roll_die() for value in range(10)]
print("\n10 jogadas de um dado de 10 lados:")
print(results)

d20 = Die(sides=20)
results = [d20.roll_die() for value in range(10)]
print("\n10 jogadas de um dado de 20 lados:")
print(results)