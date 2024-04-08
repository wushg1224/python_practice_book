''''一个用于表示汽车和电车的类'''
class Car:
    """"一次模拟汽车的简单尝试 """

    def __init__(self, make, model, year):
        """"初始化描述汽车的属性"""
        self.make = make
        self.model = model
        self. year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """"返回整洁的描述性信息"""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    def read_odometer(self):
        """"打印一条指出车的里程信息"""
        print(f"This car has {self.odometer_reading} "
              "miles on it")
    def update_odometer(self, mileage):
        """"
        将里程表读数设置成指定的值
        禁止将里程表读数回调
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You cant roll back an odometer!")
    def increment_odometer(self, miles):
        ''''将里程表增加特定的量'''
        self.odometer_reading += miles

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