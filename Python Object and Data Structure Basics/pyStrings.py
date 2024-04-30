print("Hello World!")

# \n is a new line
print("Hello \nWorld!")

# \t is a tab (tab = 4 spaces)
print("Hello \tWorld!")

# len() checks the length of string
myWord = "this is a length test"
print(len(myWord))

# Indexing l in world
myString = "Hello World"
print(myString[9])

# Reverse Indexing l in world
print(myString[-2])

# Slicing from c to the end (x: indicates after value of x to the end)
myString = 'abcdefghijk'
print(myString[2:])

# Slicing from a to h (:x indicates from start to before value of x)
print(myString[:8])

# Slicing from d to f
print(myString[3:6])

# Slicing from b to c
print(myString[1:3])

# Slicing from begining to the end with hops (a, c, e, g, i, k)
print(myString[::2])

# Reversing a string
print(myString[::-1])