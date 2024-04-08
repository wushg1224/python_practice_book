def greet_user():
    """"显示简单问候语"""
    print("Hello!")

greet_user()

def greet_user(username):
    """"show simple greeting message"""
    print(f"Hello, {username.title()}!")

greet_user('jesse')
greet_user('sarah')




def get_formatted_name(first_name, last_name):
    """"返回整洁姓名 return formatted name"""
    full_name= f'{first_name} {last_name}'
    return full_name.title()

#infinite loop
while True:
    print("\nPlease tell me your name:")
    f_name = input("First name: ")
    l_name = input("Last name: ")

    formatted_name = get_formatted_name(f_name, l_name)
    print(f"\nHello, {formatted_name}!")


