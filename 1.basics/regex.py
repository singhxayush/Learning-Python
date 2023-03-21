import re
import os

# phonenoregex = re.compile(r'(\(\d\d\d\)) (\d\d\d-\d\d\d\d)')

# mo = phonenoregex.search('My number is (415) 555-4242')

# print(mo.group())



endsWithNumber = re.compile(r'\d+$')
print(endsWithNumber.search('Your number is 421').group())


os.path('us')