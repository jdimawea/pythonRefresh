# ----- LISTS -----
my_list = [1, 2, 3]
my_list = ['String', 100, 23.2]
print(len(my_list))

my_list = ['one', 'two', 'three']
print(my_list[1:])
another_list = ['four', 'five']
concat_list = my_list + another_list
print(concat_list)
new_list = concat_list
new_list[0] = 'ONE ALL CAPS'
print(new_list)

# .append() (place any item at the end of a list)
new_list.append('six')
print(new_list)

new_list.append('seven')
print(new_list)

# .pop() (Removes any item at the end of a list)
new_list.pop()
print(new_list)

# Save .pop() item
popped_item = new_list.pop()
print(popped_item)

# .pop(x) at a certain index
new_list.pop(0)
print(new_list)

letter_list = ['a', 'e', 'x', 'y', 'b', 'c']
num_list = [3, 1, 6, 2, 5, 4]

# .sort() won't return anything, it just sorts the list, call the variable again
letter_list.sort()
my_sorted_letter_list = letter_list
print(my_sorted_letter_list)

# .reverse()
num_list.sort()
num_list.reverse()
my_reversed_list = num_list
print(my_reversed_list)
