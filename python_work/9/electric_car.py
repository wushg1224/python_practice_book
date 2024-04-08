from car import Car
class Battery:
    ''''一次模拟电动车电池的简单尝试'''
    def __init__(self, battery_size=75):
        ''''初始化电池属性'''
        self.battery_size = battery_size

    def describe_battery(self):
        ''''打印一条电池容量的消息''' 
        print(f'This car has a {self.battery_size}-kwh battery.')

    def get_range(self):
        '''''打印一条消息，指出电瓶车的续航里程'''
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315
        print(f'This car can go {range} miles on a full charge')
    def upgrade_battery(self):
        ''''check battery size'''
        if self.battery_size != 100:
            self.battery_size = 100

class ElectricCar(Car):
    '''电动汽车独特之处'''
    def __init__(self, make, model, year):
        """
        初始化父类的属性
        再初始化电动汽车特有的属性
        """
        super().__init__(make, model, year)
        self.battery = Battery()
    

    def fill_gas_tank(self):
        ''''电动汽车没有邮箱'''
        print("This car doesnt need a gas tank!")
    





my_tesla = ElectricCar('tesla', "model s", '2019')
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()

my_xiaomi = ElectricCar('xiaomi','su7','2024')
print(my_xiaomi.get_descriptive_name())
my_xiaomi.battery.describe_battery()
my_xiaomi.battery.get_range()
my_xiaomi.battery.upgrade_battery()
my_xiaomi.battery.get_range()