from re import X


x = 'awosome'

def myfunc():
  global x
  x = 'fantastic'

myfunc()

print('Python is ' + x)