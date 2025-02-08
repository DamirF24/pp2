x = 5


print(type(var))

var = 8
#isnt right

carname = "Chevrolet Cobalt"


x = y = z = "Chevrolet Cobalt"


fruits = ['apple', 'banana', 'cherry']
a, b, c = fruits
print(a)

a = 4
b = 3
print(a + b)



x = 'awesome'
def myfunc():
  x = 'fantastic'
myfunc()
print('Python is ' + x)


x = 'awesome'
def myfunc():
  global x
  x = 'fantastic'
myfunc()
print('Python is ' + x)


#difference between this two is that x is defined as global in second
