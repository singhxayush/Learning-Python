""""""" DICTONARY """""""

dict = {
    'c' : 3,
    'a' : 1,
    'b' : 2,
    'd' : 4
}

print(dict)
print(dict['d'])
# print(dict['e']) # !will give keyerror

my_list = [
    {
        'a' : [1, 2, 3],
        'b' : 'hello',
        'x' : True
    },
    {
        'a' : [4, 5, 6],
        'b' : 'world!',
        'x' : False
    }
]

print(my_list[0]['b'], my_list[1]['b'])
print(my_list[0]['a'][2])
print(my_list[1]['x'])


dict1 = {
    True : 3,
    True : 1,
    True : 2,
}
print(dict1[True]) #? in case of multiple occurances, last instance is getting printed

# NOTE : A key must be immutable, i.e. a cannot change. for ex: a key cannot be a list
