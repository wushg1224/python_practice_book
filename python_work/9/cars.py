
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


my_new_car = Car('audi', 'a4', 2019)
print(my_new_car.get_descriptive_name())
my_new_car.odometer_reading = 23
my_new_car.read_odometer()



ceci_new_car = Car('xiaomi','su7','2024')
ceci_new_car.update_odometer(24)
print(ceci_new_car.get_descriptive_name())
ceci_new_car.read_odometer()

my_used_car = Car('subaru', 'outback', '2015')
print(my_new_car.get_descriptive_name())

my_used_car.update_odometer(23_500)
my_used_car.read_odometer()

my_used_car.increment_odometer(100)
my_used_car.read_odometer()