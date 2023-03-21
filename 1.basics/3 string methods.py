print("Hello World!")
print('Hello World!\n')

print(type("123"))
print(type('123'), "\n")

long_string = '''

Hey there!

    How You Doinn! (in Joeys tone)
''' #for long sentences and paras...

print(long_string)

# Escape sequence ***
# weather = "It's "kind of sunny" sunny!"
weather = "It\'s \"kind of sunny\" sunny!"
print(weather)


# formatted  string
myName = 'Ayush'
favLan = 'C++'

# py2
print('\nHi! my name is {} & my fav programming Language is {}'.format(myName, favLan))
# py3
print(f'\nHi! my name is {myName} & my fav programming Language is {favLan}\n')


# accessing string

joeysays = 'How You Doinn!'
          # 0123456789
print(joeysays[3])

# String slicing
# [Start:Stop:Stepover] - defaults to [0:string end:1]
print(joeysays[0:7])
print(joeysays[0:7:2])
print(joeysays[:])
print(joeysays[0:7])
print(joeysays[::-1])


# Immutability - strings in python are immutable that is immutable i.e string objects does not support item assignment
# example

hello = "hello"
# hello[0] = 'H' # this wont work
hello = "123"