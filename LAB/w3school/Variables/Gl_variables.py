x = "awesome"

def myfunc1():
  print("Python is " + x)

myfunc1()


x = "awesome"

def myfunc2():
  x = "fantastic"
  print("Python is " + x)

myfunc2()

print("Python is " + x)


def myfunc3():
  global x
  x = "fantastic"

myfunc3()

print("Python is " + x)


x = "awesome"

def myfunc4():
  global x
  x = "fantastic"

myfunc4()

print("Python is " + x)