#string functions

s = "cp is the best thing there is !"

print(len(s));

print(s.upper()); #prints the given string in upper case

print(s.find('t')) #will return the index of the first occurance of the character to be found
# if not found it will return -1

# if we try to find the whole string instead of 1 character, it will return the starting index of the string
print(s.find("best"))


#we can also replace a char or a sequence of chatacters & that is by using replace
print(s.replace("b", "t"))

print(s.replace("best", "bestest ever"))


#to check the presence by return boolean method
print('best' in s) #that's it and it will check is best keyword is present or not in s and so will return T/F

print(s.title()) #will upper case the first character of all the occuirng word