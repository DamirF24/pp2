import os


write = input("Enter your lines with comma: ")
sentences = write.split(",")
with open("lab6/lines.txt",'w') as f:
    f.writelines([word + "\n" for word in sentences])

