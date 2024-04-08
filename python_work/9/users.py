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

