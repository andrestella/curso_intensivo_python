# Importando um módulo em outro módulo
""" Um conjunto de classes usado para representar carros elétricos. """


from car2 import Car


class Battery():
    """ Uma tentativa simples de modelar uma bateria para um carro elétrico. """


    def __init__(self, battery_size=70):
        """ Inicializa os atributos da bateria. """
        self.battery_size = battery_size


    def describe_battery(self):
        """ Exibe uma frase que exibe a capacidade da bateria. """
        print("This car has a {}-kWh battery.".format(self.battery_size))


    def get_range(self):
        """ Exibe uma frase sobre a distância que o carro é capaz de percorrer
        com essa bateria. """
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270
        else:
            range = "Not specified"

        if range == "Not specified":
            message = "Battery not specified."
        else:
            message = "This car can go approximately " + str(range)
            message += " miles on a full charge."
        print(message)


    def upgrade_battery(self):
        """ Verifica a capacidade da bateria e faz um upgrade se o valor for diferente de 85. """
        if self.battery_size != 85:
            self.battery_size = 85
            print("Upgraded the battery to 85 kWh.")
        else:
            print("The battery is already upgraded.")


class ElectricCar(Car):
    """ Representa aspectos de um carro específicos de veículos elétricos. """


    def __init__(self, make, model, year):
        """
        Inicializa os atributos da classe pai.
        Em seguida, inicializa os atributos específicos de um carro elétrico.
        """
        super().__init__(make, model, year)
        self.battery = Battery()


    def fill_gas_tank(self):
        """ Carros elétricos não têm tanques de combustível. """
        print("This car doesn't need a gas tank!")