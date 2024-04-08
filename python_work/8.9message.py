def show_messages(msgs):
    """"giving simple msgs"""
    for msg in msgs:
        print(msg)

messages=["have you eaten?","how are you", "i am fine"]
show_messages(messages)


def send_messages(msgs, sent_messages):
    """"print msgs and transfer msg to sent message"""
    while msgs:
        current_msg = msgs.pop()
        print(current_msg)
        sent_messages.append(current_msg)

sent_messages = []
send_messages(messages[:], sent_messages)
print(messages)
print(sent_messages)