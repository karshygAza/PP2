#List comprehension offers a shorter syntax when
#you want to create a new list based on the values of an existing list.

'''Example:
Based on a list of fruits, you want a new list,
containing only the fruits with the letter "a" in the name.
Without list comprehension you will have to write
a for statement with a conditional test inside'''
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)

#With list comprehension you can do all that with only one line of code
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x]

print(newlist)

#The Syntax
#newlist = [expression for item in iterable if condition == True]
#The return value is a new list, leaving the old list unchanged

#Condition
#The condition is like a filter that only accepts the items that evaluate to True.
newlist = [x for x in fruits if x != "apple"]

#With no if statement:
newlist = [x for x in fruits]

#Iterable
#The iterable can be any iterable object, like a list, tuple, set etc
newlist = [x for x in range(10)]

newlist = [x for x in range(10) if x < 5]

#Expression
newlist = [x.upper() for x in fruits]

newlist = ['hello' for x in fruits]

newlist = [x if x != "banana" else "orange" for x in fruits]