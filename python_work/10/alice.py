import os
filename = os.path.join(os.path.dirname(__file__),'alice.txt')
try:
    with open(filename, encoding='utf-8') as f:
        contents = f.read()
except FileNotFoundError:
    print(f"sorry, the file {filename} does not exist")
else:
    worlds = 