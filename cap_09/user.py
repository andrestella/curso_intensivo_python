class User():
    """ Modelando um usuário do sistema. """


    def __init__(self, first_name, last_name, age, occupation):
        """ Inicializa cada usuário com suas informações básicas. """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.occupation = occupation


    def describe_user(self):
        """ Exibe as informações do usuário do sistema. """
        print("O usuário {} {} com idade de {} anos, trabalha na área de {}."
            .format(self.first_name.title(), self.last_name.title(),
             self.age, self.occupation))


    def greet_user(self):
        """ Exibe uma saudação ao usuário do sistema. """
        print("Seja bem-vindo {} {}!"
            .format(self.first_name.title(), self.last_name.title()))


usuario_0 = User('andré', 'alexandre', 40, 'computação')
usuario_0.describe_user()
usuario_0.greet_user()
usuario_1 = User('henri', 'stella', 30, 'finanças')
usuario_1.describe_user()
usuario_1.greet_user()
usuario_2 = User('nádia', 'stella', 35, 'recursos humanos')
usuario_2.describe_user()
usuario_2.greet_user()