#You can loop through the list items by using a for loop
listDa = ["ananas", "banana", "strawberry"]
for x in listDa:
    print(x)
    
#You can also loop through the list items by referring to their index number.
#Use the range() and len() functions to create a suitable iterable.
listDa = ["ananas", "banana", "strawberry"]
for i in range(len(listDa)):
    print(listDa[i])
    
'''You can loop through the list items by using a while loop.
Use the len() function to determine the length of the list, 
then start at 0 and loop your way through the list items by referring to their indexes.
Remember to increase the index by 1 after each iteration.'''
listDa = ["ananas", "banana", "strawberry"]
i = 0
while i < len(listDa):
    print(listDa[i])
    i += 1
    
#A short hand for loop that will print all items in a list:
listDa = ["ananas", "banana", "strawberry"]
[print(x) for x in listDa]