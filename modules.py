##Core Modules

# import datetime

# today = datetime.date.today()
# print(today)
# #Output 2021-05-03

# #Or
# import datetime
# from datetime import date

# today = date.today()
# print(today)
# #Output 2021-05-03 (Same but we have used builtin function named date directly)

# #Importing Time module
# import datetime
# from datetime import date
# import time

# today = date.today()
# timestamp = time.time()
# print(timestamp)
# #Output 1620041861.108753

# #For the same above mentioned code we can directly use the time function by importing it befor itself
# import datetime
# from datetime import date
# import time
# from time import time

# today = date.today()
# timestamp = time()
# print(timestamp)
# #Output 1620041938.674968

#Using pip module (Camelcase)
from camelcase import CamelCase

c = CamelCase()
print(c.hump('hello there world'))
##Output Hello There World

# Import custom module
import validator
from validator import validate_email

email = 'test#test.com'
if validate_email(email):
  print('Email is valid')
else:
  print('Email is bad')
