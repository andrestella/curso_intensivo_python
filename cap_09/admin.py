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


class Privileges():
    """ Modelando os privilégios dos usuário do sistema. """


    def __init__(self):
        """ Inicializa os atributos da classe 'Privileges'. """
        self.privileges = []


    def show_privileges(self):
        """ Exibe os privilégios dos usuários do sistema. """ 
        if self.privileges:
            for privilege in self.privileges:
                print("- " + privilege) 
        else:
            print("This user has no privileges.")  


class Admin(User):
    """ Modelando um administrador do sistema. """


    def __init__(self, first_name, last_name, age, occupation="system administrator"):
        """ Inicializando os atributos de um administrador do sistema. """
        super().__init__(first_name, last_name, age, occupation)
        self.privileges = Privileges()


administrador = Admin('andré', 'alexandre', 40)
administrador.describe_user()
administrador.privileges.privileges = [
    'can add post',
    'can delete post',
    'can ban user',
    ]
administrador.privileges.show_privileges()