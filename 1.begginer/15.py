#Lists Tuples and Sets

#lists
from termios import VREPRINT


variables = ['a', 'b', 'c', 'd', 'e']
print(variables[2])
print(variables)
print(variables[::-1])
print(variables[0:2]) #means start at zero index, print till index not including 2
print(len(variables))
print(variables[1:]) #prints all after 1st index
print(variables[:4]) #prints all till (4-1)th index

variables.append('f')
variables.insert(1, 'g')
print(variables)

variables.remove('e')
print(variables)
variables.pop()
print(variables)

variables.reverse()
print(variables)


variables.sort()
print(variables)


x_variables = '-'.join(variables)
print(x_variables)