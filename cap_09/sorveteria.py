class Restaurant():
    """ Modelando um restaurante simples. """


    def __init__(self, restaurant_name, cuisine_type):
        """ Inicializa uma instância da classe 'Restaurant'. """
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0


    def describe_restaurant(self):
        """ Exibe as informações básicas do restaurante. """
        print("O restaurante {} trabalha com a cozinha {}."
            .format(self.restaurant_name.title(), self.cuisine_type))


    def open_restaurant(self):
        """ Exibe a informação de que o restaurante encontra-se aberto. """
        print("O restaurante {} está aberto!".format(self.restaurant_name.title()))


    def set_number_served(self, number):
        """ Modifica o número de clientes atendidos pelo restaurante. """
        self.number_served = number


    def increment_number_service(self, number):
        """ Incrementa o número de clientes atendidos pelo restaurante. """
        self.number_served += number


class IceCreamStand(Restaurant):
    """ Modelando uma simples sorveteria. """


    def __init__(self, restaurant_name, cuisine_type="sorveteria"):
        """ Inicializa um carrinho de sorvete. """
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = []


    def show_flavors(self):
        """ Exibe os sabores disponíveis de sorvete. """
        for flavor in self.flavors:
            print("- " + flavor)


sorveteria = IceCreamStand("stella")
sorveteria.describe_restaurant()
sorveteria.flavors = ['creme', 'napolitano', 'chocolate', 'morango']
sorveteria.show_flavors()