# x = list(range(1, 10))
# print(x)


print(list(range(1, 10))) # doesnt include 10
print(list(range(10)))


sentance = ''
sentance.join(['Hi', 'my', 'name', 'is', 'Ayush'])
print(sentance) #NOTE : will give no output since join return a complete new list


# but this will work
sentance = '-'
sentance = sentance.join(['Hi', 'my', 'name', 'is', 'Ayush'])
print(sentance)

print('-'.join(['Hi', 'my', 'name', 'is', 'Ayush']))

# NOTE - LEARN MORE FROM PYTHON DOCS "https://docs.python.org/3/tutorial/datastructures.html"




#######? LIST UNPACKING ########

a, b, c, *other, d = [1, 2, 3, 4, 5, 6, 7, 8];
print(a)
print(b)
print(c)
print(other)
print(d)


#######? NONE DATA TYPE ########

