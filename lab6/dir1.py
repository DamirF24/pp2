import os

path = './' 
contents = os.listdir(path)

for element in contents:
    print(element)

choose = input("Choose which directory to open: ")

if choose in contents and os.path.isdir(choose):
        files = os.listdir(element)
        print(f"Here are your files: {', '.join(files)}")
else:
        print(f"No such directory")
