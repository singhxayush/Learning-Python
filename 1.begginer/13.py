message = 'bobby\'s world'
print(message)
print(len(message))
print(message.find('world'))
print(message.count('b'))
message = message.replace('bobby\'s','hello')
print(message)
message = message[::-1] #to reverse string
print(message)

greeting = 'hello'
name = 'mike'
message = '{}, {}. Welcome!'.format(greeting, name) #string formatting
#or u can also use f string method of formatting
message = f'{greeting}, {name}. Welcome!'
print(message)

 
print(dir(message)) #shows all the attributes/functionality availabe
print(help(str)) #shows all the print functions and what they do : documentation of print function