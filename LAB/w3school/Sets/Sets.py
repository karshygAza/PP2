#Set
thisset = {"apple", "banana", "cherry"}
print(thisset)
#Duplicates Not Allowed,duplicate values will be ignored
#True and 1 is considered the same value
#False and 0 is considered the same value
thisset = {"apple", "banana", "cherry", "apple"}
print(thisset)
#Get the Length of a Set
thisset = {"apple", "banana", "cherry"}
print(len(thisset))
#Set Items - Data Types
set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}
#A set can contain different data types
set1 = {"abc", 34, True, 40, "male"}
#type()
myset = {"apple", "banana", "cherry"}
print(type(myset))
#The set() Constructor
thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset)