import os
guest_filename = os.path.join(os.path.dirname(__file__),'guest.txt')
answer_filename =  os.path.join(os.path.dirname(__file__),'answer.txt')

def save_username():
    print("\nEnter 'q' to quit anytime")
    while True:
        username = input("Please tell me Username: ").strip()  # 清除输入前后的空白字符
        if username == 'q':  # 先检查是否退出
            break
        with open(guest_filename, 'a') as file_object:
            file_object.write(username + '\n')  # 写入文件
        print(f"Thank you, {username} is added to the database.")  # 确认写入后感谢
        #问用户原因
        print(f"{username.title()} why do you love coding?")
        reason = input(" ")
        with open(answer_filename, 'a') as file_object:
            file_object.write(reason + '\n')

save_username()

