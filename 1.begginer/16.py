variables = ['a', 'b', 'c', 'd', 'e']
variables2 = variables
variables.append('f')

print(variables)
print(variables2)


#this is because in list in python they are simply both the same mutable object
#to avoid this we use tuple

#immutable

tuple_1 = (1, 2, 3, 4, 5)
print(tuple_1)
tuple_2 = tuple_1
print(tuple_2)

#tuples have limited attributes compared to lists
