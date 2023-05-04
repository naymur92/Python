# Global variable example
x = 'World'   # This is global variable

def myfunc():
  print('Hello ' + x)

myfunc()

# Global & Local variable example
x = 'awosome'   # This is global variable
def myfunc1():
  x = 'fantastic'   # This is local variable
  print('Python is ' + x)

myfunc1()   # Print with local variable

print('Python is ' + x)   # Print with global variable