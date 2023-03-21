from array import array


print(3/2) #division -> float op
print(3//2) #floor division
print(3**2) #3^2
print(3**0.5) #3^2
#else rest are same

num = 1
num += (3>2)
print(num)

array = [1, 4, 2, 6, 7, 3, 2]
array.sort()
print(array)
array.sort(reverse=True)
print(array)


print(min(array))
print(max(array))

print(sum(array))

print(array)
print(array.index(2))

print(5 in array)
print(3 in array)


print('for loop for printing array')
for i in array : print(i)

#prints in pair starting from a given index 
for index, array in enumerate(array, start=0) : print(index, array)