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


restaurant = Restaurant('stella', 'italiana')
print(restaurant.restaurant_name.title())
print(restaurant.cuisine_type.title())
restaurant.describe_restaurant()
restaurant.open_restaurant()

print("Número de clientes servidos: {}".format(restaurant.number_served))
restaurant.number_served = 10
print("Número de clientes servidos: {}".format(restaurant.number_served))
restaurant.set_number_served(20)
print("Número de clientes servidos: {}".format(restaurant.number_served))
restaurant.increment_number_service(10)
print("Número de clientes servidos: {}".format(restaurant.number_served))