import sys
class Student:
    def __init__(self, name: str) -> None:
        self.name = name

    
class Admin:
    def __init__(self, name:str) -> None:
        self.name=name
        
class UniApp:
    session: Student | Admin | None
    def __init__(self, session=None) -> None:
        self.session= session

    def main(self):
        if type(self.session) is Admin:
            self.admin_menu()
        elif type(self.session) is Student:
            self.study()
        else:
            self.default_menu()

    def default_menu(self):
        while True:
            userchoice = input('University System: (A)dmin, (S)tudent, or X: ')
            match userchoice:
                case 'A':
                    self.session = Admin
                case 'S':
                    self.session = Student
                case 'X':
                    print('Thank you')
                    self.exit()
                    break  # 确保从循环中退出

    def student_login(self):
        print("Student login not implemented.")  # 提供一个基本实现

    def admin_menu(self):
        while True:
            userchoice = input('Admin System (c/g/p/r/s/x): ')

            
                
    def exit(self):
        sys.exit()

# 创建类的实例并调用方法

