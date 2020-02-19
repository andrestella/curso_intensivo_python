""" 
Um conjunto de classes usado para representar administradores
 e privilégios de um sistema.
"""


from user2 import User


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