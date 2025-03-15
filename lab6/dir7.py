import os
print(os.getcwd())
with open("/Users/farkhatovdamir/Desktop/python/lab6/text.txt",'r') as f:
  copy = f.read()
  
 
with open("/Users/farkhatovdamir/Desktop/python/lab6/newfile2.txt",'w') as f:
  f.write(copy)
  
print(copy)

