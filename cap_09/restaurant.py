class Restaurant():
    """ Modelando um restaurante simples. """


    def __init__(self, restaurant_name, cuisine_type):
        """ Inicializa uma instância da classe 'Restaurant'. """
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type


    def describe_restaurant(self):
        """ Exibe as informações básicas do restaurante. """
        print("O restaurante {} trabalha com a cozinha {}."
            .format(self.restaurant_name.title(), self.cuisine_type))


    def open_restaurant(self):
        """ Exibe a informação de que o restaurante encontra-se aberto. """
        print("O restaurante {} está aberto!".format(self.restaurant_name.title()))


restaurant = Restaurant('stella', 'italiana')
print(restaurant.restaurant_name.title())
print(restaurant.cuisine_type.title())
restaurant.describe_restaurant()
restaurant.open_restaurant()

print("\n")

restaurant2 = Restaurant('henri', 'americana')
restaurant2.describe_restaurant()
restaurant3 = Restaurant('nádia', 'brasileira')
restaurant3.describe_restaurant()
restaurant4 = Restaurant('maria', 'paulista')
restaurant4.describe_restaurant()