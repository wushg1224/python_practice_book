from electric_car import ElectricCar as EC
my_tesla = EC('tesla','model s', 2019)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()

my_beetle = EC('Volkswagen', 'beetle', 2019)
print(my_beetle.get_descriptive_name())