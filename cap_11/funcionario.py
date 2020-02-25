class Employee():
    """ Modelando os dados básicos de um funcionário. """


    def __init__(self, first_name, last_name, annual_salary):
        """ Inicializa os atributos essenciais de um funcionário. """
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.annual_salary = annual_salary


    def give_raise(self, value=5000):
        """ 
        Soma um adicional anual no salário do funcionário, sendo
        5 mil dólares o valor padrão. 
        """
        self.annual_salary += value