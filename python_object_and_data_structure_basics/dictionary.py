# keys should be a string
my_dictionary = {'key1':'value1', 'key2':'value2'}
print(my_dictionary)
# returns value1
print(my_dictionary['key1'])

def price_lookup(item):
    print(prices_lookup[item])

prices_lookup = {'apple': 2.99, 'oranges':1.99, 'milk':5.80}
price_lookup('oranges')

def get_value_from_list(key):
    print(d[key])
    
d = {'k1':123, 'k2':[0, 1, 2], 'k3':{'insideKey':100}}
get_value_from_list('k3')
# key inside key, returns value of 100
print(d['k3']['insideKey'])
# returns value of two
print(d['k2'][2])

dict = {'k1':['a', 'b', 'c']}
# grabs the list from 'k1'
mylist = dict['k1']
# grabs the letter at index 2
letter = mylist[2]
# makes the letter uppercase
print(letter.upper())

# or the better way
print(dict['k1'][2].upper())

# adding key:value pairs into a dictionary
dict = {'k1':100, 'k2':200}
dict['k3'] = 300
print(dict)

# setting new value
dict['k1'] = 'New Value'
print(dict)

dict = {'k1':100, 'k2':200, 'k3':300}
# returns the keys
print(dict.keys())
# returns the values
print(dict.values())
# returns the key:value pairs
print(dict.items())
