def true_or_false (bool):
    if bool == True:
        print('It is True!')
    elif bool == False:
        print('It is False!')
    else:
        print('Neither True or False')
true_or_false(True)
true_or_false(False)


def is_hungry (bool):
    if bool == True:
        print('Feed me!')
    elif bool == False:
        print('I am full')
    else:
        print('What is food?')
is_hungry(True)


def name_function (name):
    if name == 'Johnny':
        print('Hello Johnny')
    elif name == 'Jeshua':
        print('Hello Jeshua')
    else: 
        print('Nice to meet you ' + name)
name = 'Johnny'
name2 = 'Angie'
name_function(name)
name_function(name2)

