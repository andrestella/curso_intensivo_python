from car import Car

my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()

# Modificando o valor de um atributo diretamente
my_new_car.odometer_reading = 23
my_new_car.read_odometer()

# Modificando o valor de um atributo com um método
my_new_car.update_odometer(50)
my_new_car.read_odometer()

# Incrementando o valor de um atributo com um método
my_used_car = Car('subaru', 'outback', 2013)
print(my_used_car.get_descriptive_name())
my_used_car.read_odometer()

my_used_car.update_odometer(23500)
my_used_car.read_odometer()

my_used_car.increment_odometer(100)
my_used_car.read_odometer()
my_used_car.fill_gas_tank()