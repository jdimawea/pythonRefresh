# my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# for num in my_list:
#     print(num) 

# # num could be any name
# for diffname in my_list:
#     print(diffname)

# # Function that can tell if the number is even or odd
# def is_even_or_odd (num_list):
#     for num in num_list:
#         if num % 2 == 0:
#             print(f'Even: {num}')
#         else:
#             print(f'Odd: {num}')
# is_even_or_odd(my_list)

# # Getting sum of the numers
# list_sum = 0

# for num in my_list:
#     list_sum = list_sum + num
# print(list_sum)

# # Function that sums a list
# def list_sum (sum_list):
#     sum = 0
#     for num in sum_list:
#         sum = sum + num
#     print(f'The sum is: {sum}')    
# list_sum(my_list)

# # Function that iterates and returns each letter in a string
# def return_string (my_string):
#     for letter in my_string:
#         print(letter)
# return_string('This is a test')

# tup = (1, 2, 3)

# for item in tup:
#     print(item)


my_list = [(1,2), (3,4), (5,6), (7,8)]
# print(len(my_list))

for (a, b) in my_list:
    print(a) # print first item in the tuple that is inside the list
    print(b) # print second item in the tuple that is inside the list

my_list = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]

for (a, b, c) in my_list:
    print(a, c)

my_dict = {'k1':1, 'k2':2, 'k3':3, 'k4':4, 'k5':5}

# printing out key value pairs
for item in my_dict.items():
    print(item)

# printing out either key or value (.items())
for key, value in my_dict.items():
    print(key)
    print(value)

# printing out just the value (.values())
for value in my_dict.values():
    print(value)

# printing out just the key (.keys())
for key in my_dict.keys():
    print(key)