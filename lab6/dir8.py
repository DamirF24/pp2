import os

file = input("Write file to delete: ")

if os.path.exists(file) and os.access(file, os.F_OK):
   os.remove(file)
   print("File succesfully deleted")
else:
   print("No such file or directory")