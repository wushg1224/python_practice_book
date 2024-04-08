class User:
    """"一次建立用户类的简单尝试"""
    def __init__(self, first_name, last_name, *user_info):
        """"初始化属性 firstname和lastname和其他属性"""
        self.first_name = first_name
        self.last_name = last_name
        self.user_info = user_info
        self.login_attempts = 0

    def describe_user(self):
        """"打印用户信息摘要"""
        print({self.first_name},
              {self.last_name},{self.user_info})
    
    def greeter_user(self):
        """"向用户发出个性化问候"""
        print(f"Good morning {self.first_name.title()}!")

    def increment_login_atttempts(self):
        self.login_attempts += 1
    
    def reset_login_attempts(self):
        self.login_attempts = 0

class  Admin(User):
    def __init__(self, first_name, last_name, *user_info):
        super().__init__(first_name, last_name, *user_info)
        self. privileges = Privileges()
      
   

class Privileges:
    ''''user privileges'''
    def __init__(self, privileges= ['can add post','can delete post','can ban user']) :
        self.privileges = privileges
    def show_privileges(self):
        ''''show admin privileges'''
        print(f'This user have {self.privileges} privileges')

user_1 = User('cecilia', 'gao', 'age=24','hobbit=games' )
user_1.describe_user()
user_1.greeter_user()

user_1.increment_login_atttempts()
print(user_1.login_attempts)
user_1.increment_login_atttempts()
print(user_1.login_attempts)
user_1.increment_login_atttempts()
print(user_1.login_attempts)
user_1.reset_login_attempts()
print(user_1.login_attempts)

ceci=Admin('ceci','gao')
ceci.privileges.show_privileges()

lusi = Admin('lusi','zhao')
lusi.privileges.show_privileges()