mylist = [1, 2, 3]

for num in range(0, 11, 2): # (starting number, ending but not included number, count)
    print(num)

index_count = 0

for letter in 'abcde':
    # print('At index {} the letter is {}'.format(index_count, letter))
    print(f'At index {index_count} the letter is {letter}')
    index_count += 1


word = 'abcde'

# better version, returns a tuple 
for item in enumerate(word):
    print(item)

# better better version (we can unpack the tuple)
for index, letter in enumerate(word):
    print(index)
    print(letter)
    print('\n')

my_list_one = [1, 2, 3, 4, 5]
my_list_two = ['a', 'b', 'c']
my_list_three = [100, 200, 300]

# This doesnt work
print(zip(my_list_one, my_list_two))

for item in zip(my_list_one, my_list_two, my_list_three):
    print(item)