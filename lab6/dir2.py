import os

paths = './'
contents = os.listdir(paths)
print("All paths: ")
for element in contents:
    print(element,'\n')
path = input("Choose the path: ")
def isPathOk(path):
   if path in contents:
        print("Existence: ",os.access(path, os.F_OK))
        print("Readiblity: ",os.access(path, os.R_OK)) 
        print("Writability: " ,os.access(path, os.W_OK)) 
        print("Executability: " , os.access(path, os.X_OK))
   else:
        print("No such path found")
   

isPathOk(path)