

def readfile(filename):
    with open(filename) as file_object:
        for line in file_object:
            line = line.replace('Python', 'C')
            print(line.rstrip())

readfile('learning_python.txt')



    