x = 21
y = 20

# Comparison Operators (==, !=, >, <, >=, <=) - Used to compare values

# # Simple if
# if x > y:
#   print(f'{x} is greater than {y}')
# ## Outpit 21 is greater than 20

# # If/else
# if x > y:
#    print(f'{x} is greater than {y}')
# else:
#    print(f'{y} is greater than {x}') 
# #Output 21 is greater than 20 

# # elif
# if x > y:
#   print(f'{x} is greater than {y}')
# elif x == y:
#   print(f'{x} is equal to {y}')  
# else:
#   print(f'{y} is greater than {x}')  
# #Output 21 is greater than 20

# # Nested if
# if x > 2:
#   if x <= 30:
#     print(f'{x} is greater than 2 and less than or equal to 30')
# #Output 21 is greater than 2 and less than or equal to 30
    

# # Logical operators (and, or, not) - Used to combine conditional statements

# # and
# if x > 2 and x <= 30:
#     print(f'{x} is greater than 2 and less than or equal to 30')
# #Output 21 is greater than 2 and less than or equal to 30


# # or
# if x > 2 or x <= 21:
#     print(f'{x} is greater than 2 or less than or equal to 21')
# #Output 21 is greater than 2 or less than or equal to 21
# # not
# if not(x == y):
#   print(f'{x} is not equal to {y}')
# #Output 21 is not equal to 20

# # Membership Operators (not, not in) - Membership operators are used to test if a sequence is presented in an object

numbers = [1,2,3,4,5,21]

# # #  in
# if x in numbers:
#  print(x in numbers)


# # # not in
# if x not in numbers:
#   print(x not in numbers)
# #Output True


# # Identity Operators (is, is not) - Compare the objects, not if they are equal, but if they are actually the same object, with the same memory location:

# # is
if x is y:
  print(x is y)


# # is not
if x is not y:
  print(x is not y)
#Output True