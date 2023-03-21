""" """ """ TUPLES """ """ """

tuple1 = (1, 2, 3, 4, 5, 4, 5)
print(tuple1)
print(tuple1[2])


# NOTE : tupples are immutable also they are less flexible than list
# NOTE : tupples can't be sorted or reversed
# NOTE : but they are usually faster than list
# tuple1[1] = 3 #!TypeError: 'tuple' object does not support item assignment


#? A tupple has only 2 mehtods : count & index


# NOTE : returns the index of first occurance of value
print(tuple1.index(2))
print(tuple1.index(4))
print(tuple1.index(5))
# print(tuple1.index(7)) #! ValueError: tuple.index(x): x not in tuple

# NOTE : return thr freq of the value entered if not present return 0
print(tuple1.count(2))
print(tuple1.count(5))
print(tuple1.count(7))

