from users import User
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
