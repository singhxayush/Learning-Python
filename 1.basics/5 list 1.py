# List are mutable

arr = [1, 2, 3, 4, 5, 5]

arr.append(6)
arr1 = arr
print(arr1)

arr.insert(3, 8)

print(arr)

arr.pop() # normal pop from back

print(arr)

arr.pop(0) # pops at index

print(arr)


# .remove to rm a value - removes only one occurance

arr.remove(5)
print(arr)
arr.remove(5)
print(arr)

arr1 = arr.clear()

# pop returns a value that is being popped

print(arr1) # NOTE : gives none as clear func doesnt return a value, its NULL, its none
print(arr)