users=[]
if users:
    for user in users:
        if user == 'admin':
            print(f"Hello, {user}, would you like to see a status report.")
        else:
            print("Hello Jaden, thank you for logging in agian")
else:
    print("We need to find some users!")

current_users=['andy','brian','clara','dog','ella']
new_users=['fransis','gao','andy','brian','zoe']
for new_user in new_users:
    if new_user in current_users:
        print("need another username")
    else:
        print(f"{new_user} is not used before")
              
