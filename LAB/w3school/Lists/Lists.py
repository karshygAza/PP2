#Create a List
thislist = ["apple", "banana", "cherry"]
print(thislist)

#Lists allow duplicate values
thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)

#Print the number of items in the list
thislist = ["apple", "banana", "cherry"]
print(len(thislist))

#List items can be of any data type
list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]
#A list can contain different data types
list1 = ["abc", 34, True, 40, "male"]

#What is the data type of a list?
mylist = ["apple", "banana", "cherry"]
print(type(mylist))

#Using the list() constructor to make a List
thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)

"""Python Collections (Arrays)
There are four collection data types in the Python programming language:

List is a collection which is ordered and changeable. Allows duplicate members.
Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
Dictionary is a collection which is ordered** and changeable. No duplicate members.
"""