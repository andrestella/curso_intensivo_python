""" Uma classe que pode ser usada para representar usuários do sistema. """


class User():
    """ Modelando um usuário do sistema. """


    def __init__(self, first_name, last_name, age, occupation):
        """ Inicializa cada usuário com suas informações básicas. """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.occupation = occupation
        self.login_attempts = 0


    def describe_user(self):
        """ Exibe as informações do usuário do sistema. """
        print("O usuário {} {} com idade de {} anos, trabalha na área de {}."
            .format(self.first_name.title(), self.last_name.title(),
             self.age, self.occupation))


    def greet_user(self):
        """ Exibe uma saudação ao usuário do sistema. """
        print("Seja bem-vindo {} {}!"
            .format(self.first_name.title(), self.last_name.title()))


    def increment_login_attempts(self):
        """ Incrementa em uma unidade as tentativas de login. """
        self.login_attempts += 1


    def reset_login_attempts(self):
        """ Reinicia o valor das tentativas de login com zero. """
        self.login_attempts = 0