file_path = "/Users/ceci/Documents/GitHub/python_practice_book/python_work/chapter10/text_files/filename.txt"
with open(file_path) as file_object:
    contents = file_object.read()
print(contents.rstrip())