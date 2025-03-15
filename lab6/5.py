in1 = (True,True,True,False)
x = True
def isTrue(s):
 for val in s:
    if val == True:
        x = True
    else:
        x = False
 if x == True:
    print("True")
 else:
    print("False")


isTrue(in1)