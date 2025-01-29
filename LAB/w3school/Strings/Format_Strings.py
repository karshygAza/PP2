'''To specify a string as an f-string,
simply put an f in front of the string literal,
and add curly brackets {} as placeholders for variables and other operations.'''
#F-Strings
age = 36
txt = f"My name is John, I am {age}"
print(txt)

#Placeholders and Modifiers
price = 59
txt = f"The price is {price} dollars"
print(txt)
#Display the price with 2 decimals
price = 59
txt = f"The price is {price:.2f} dollars"
print(txt)
#Perform a math operation in the placeholder, and return the result
txt = f"The price is {20 * 59} dollars"
print(txt)