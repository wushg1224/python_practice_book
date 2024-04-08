class Restaurant:
    """"一次收集餐馆的尝试"""
    def __init__(self, name, cuisine_type):
        """"初始化属性 name 和 type"""
        self.name = name
        self.cuisine_type = cuisine_type
        self.number_served = 0
    def describe_restaurant(self):
        """描述餐馆"""
        describe_res = f'{self.name}{self.cuisine_type}'
        return describe_res
    def open_restaurant(self):
        ''''餐馆在营业'''
        print(f"{self.name} is open now!")
    def set_number_served(self, number):
        ''''设置就餐人数'''
        self.number_served = number   
    def increment_number_served(self, number):
        ''''将用餐人数递增'''
        self.number_served += number
    def read_number_served(self):
        """"打印餐馆人数信息"""
        print(f"{self.describe_restaurant()} can serve {self.number_served}")

class IceCreamStand(Restaurant):
    ''''冰激凌店'''
    def __init__(self, name, cuisine_type):
        ''''
        初始化父类属性
        再初始化冰激凌店'''
        super().__init__(name, cuisine_type)
        self.flavors = ['strawberry','macha','chocolate']

    def describe_icecream(self):
        ''''打印一条显示冰激凌口味的消息'''
        print(f'This restraunt has {self.flavors} taste')

a_res = Restaurant('边城记忆', '湘菜')

a_res.open_restaurant()
b_res = Restaurant('hubert', 'french')
c_res = Restaurant('沙县小吃', '福建菜')
print(b_res.describe_restaurant())
print(c_res.describe_restaurant())

print(a_res.describe_restaurant())
a_res.read_number_served()
a_res.set_number_served(10)
a_res.read_number_served()
a_res.increment_number_served(20)
print(f"I think {a_res.describe_restaurant()} can maximumly serve {a_res.number_served} people")

my_iceshop = IceCreamStand('icekirinbar', 'icecream')
print(my_iceshop.describe_restaurant())
my_iceshop.describe_icecream()