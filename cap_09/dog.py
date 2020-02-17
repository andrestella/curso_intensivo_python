# Criando a classe 'Dog'
class Dog(): # por convenção, nomes com a primeira letra maiúscula referem-se a classes em Python
    """ Uma tentativa simples de modelar um cachorro. """


    # O método '_init_' é um método especial que Python executa automaticamente
    # sempre que criamos uma nova instância baseada na classe 'Dog'
    def __init__(self, name, age): # dois underscores no início e dois no final
    # o parâmetro 'self' é obrigatório na definição do método e deve estar antes dos demais parâmetros
        """ Inicializa os atributos 'name' e 'age'. """
        self.name = name
        self.age = age
        # Qualquer variável prefixada com 'self' está disponível a todos os métodos da classe
        # Além disso, podemos acessar essas variáveis por meio de qualquer instância criada a partir da classe
        # Variáveis como essas, acessíveis por meio de instâncias, são chamadas de 'atributos'
        # Esse método não tem uma instrução 'return' explícita, mas Python devolve automaticamente uma instância


    def sit(self):
        """ Simula um cachorro sentando em resposta a um comando. """
        print("{} is now sitting.".format(self.name.title()))


    def roll_over(self):
        """ Simula um cachorro rolando em resposta a um comando. """
        print("{} rolled over!".format(self.name.title()))


# Criando uma instância a partir de uma classe
my_dog = Dog('willie', 6) # armazenamos a instância criada na variável 'my_dog'
# Acessando atributos
print("My dog's name is {}.".format(my_dog.name.title()))
print("My dog is {} years old.".format(my_dog.age))
# Chamando métodos
my_dog.sit()
my_dog.roll_over()
# Criando várias instâncias
your_dog = Dog('lucy', 3)
print("\nYour dog's name is {}.".format(your_dog.name.title()))
print("Your dog is {} years old.".format(your_dog.age))
# Chamando métodos
your_dog.sit()
your_dog.roll_over()

# Você pode criar tantas instâncias de uma classe quantas forem necessárias, desde que dê a cada instância
# um nome de variável único ou que ela ocupe uma única posição em uma lista ou dicionário