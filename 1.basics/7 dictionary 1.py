""""""" DICTONARY """""""

dict = {
    'c' : 3,
    'a' : 1,
    'b' : 2,
    'd' : 4
}

print(dict)
print(dict['d'])
dict.update({'f' : 11})

# print(dict['e']) # !will give keyerror
#? Incase a key doesn't exist and to avoid error we use get method of dictionary
print(dict.get('e')) #NOTE : will print None

# searching for a key
print('c' in dict) # Gives True o/p
print('e' in dict) # Gives False o/p
print(4 in dict.values())
print('a' in dict.keys())

print(dict.items()) # NOTE: this returns key and value as tuple

dict_copy = dict.copy()
print("below is the copied dict")
print(dict_copy)

print("below is the emptied dict")
dict.clear() # empties the dictionary
print(dict)



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

# NOTE : A key must be immutable, i.e. a cannot change. for ex: a key cannot be a list but tupples can be
