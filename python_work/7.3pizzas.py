prompt ="\n Tell me what pizza ingredients you want to add: "
prompt +="\nEnter 'quit' to end the program."

message = ""
while message!= 'quit':
    message = input(prompt)
    if message != 'quit':
        print(f"\nWe will add {message} in your pizza!")
    
   