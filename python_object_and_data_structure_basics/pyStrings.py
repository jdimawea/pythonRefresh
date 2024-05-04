# print("Hello World!")

# # \n is a new line
# print("Hello \nWorld!")

# # \t is a tab (tab = 4 spaces)
# print("Hello \tWorld!")

# # len() checks the length of string
# myWord = "this is a length test"
# print(len(myWord))

# # Indexing l in world
# myString = "Hello World"
# print(myString[9])

# # Reverse Indexing l in world
# print(myString[-2])

# # Slicing from c to the end (x: indicates after value of x to the end)
# myString = 'abcdefghijk'
# print(myString[2:])

# # Slicing from a to h (:x indicates from start to before value of x)
# print(myString[:8])

# # Slicing from d to f
# print(myString[3:6])

# # Slicing from b to c
# print(myString[1:3])

# # Slicing from begining to the end with hops (a, c, e, g, i, k)
# print(myString[::2])

# # Reversing a string
# print(myString[::-1])

# # ------- IMMUTABILITY -------
# name = "Sam"
# last_letters = name[1:]
# print(last_letters)
# # Called string concatination
# print("P" + last_letters)

# x = "Hello World!"
# print(x + " it is beautiful outside!")

# letter = 'z'
# print(letter * 10)

# x = 'Hello World'
# print(x.upper())
# x = 'Hi this is a string'
# print(x.split())
# print(x.split('i'))

# .format()
print('This is a string {}'.format('inserted'))
print('The {0} {0} {0}'.format('fox', 'brown', 'quick'))
print('The {2} {1} {0}'.format('fox', 'brown', 'quick'))
print('The {} {} {}'.format('fox', 'brown', 'quick'))
print('The {q} {b} {f}'.format(f='fox', b='brown', q='quick'))

# float formatting "{value:width.precision f}"
result = 100/777
result = 104.12345 
# gives me decimals places
print("The result was {r:1.3f}".format(r=result))

# f string method
name = "Jose"
print(f'Hello, his name is {name}')

name = "Sam"
age = 3
print(f'{name} is {age} years old.')