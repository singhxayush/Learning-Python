# whatever typed inside termial is taken input as a string

birth_yr = input('birth year :')
print(type(birth_yr))
# age = 2022 - birth_yr #this will throw an error
age = 2022 - int(birth_yr) #typecasting string to int
print(type(age))
print(age)
# print('age : '+str(age))