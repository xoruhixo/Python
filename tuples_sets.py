
#
fruits = ('Apples', 'Oranges', 'Grapes') # Create tuple

#fruits2 = tuple(('Apples', 'Oranges', 'Grapes')) # Using a constructor
#print(fruits, fruits2)
#Output ('Apples', 'Oranges', 'Grapes') ('Apples', 'Oranges', 'Grapes')


fruits2 = ('Apples')
print(fruits2, type(fruits2))
#Output Apples <class 'str'>




#Single value needs trailing comma
fruits2 = ('Apples',) 
print(fruits2, type(fruits2))
#Output ('Apples',) <class 'tuple'>

# Get value
print(fruits[1])
#Output Oranges


# for list you can change value but Can't change value in Tuples
#fruits[0] = 'Pears'
#Error message in output

# Delete tuple
#del fruits2
#print (fruits2)


# Get length
print(len(fruits))
#Output 3






# Create set
fruits_set = {'Apples', 'Oranges', 'Mango'} #Always in Curly Braces


# Check if in set
print('Apples' in fruits_set)
#Output True

# Add to set
fruits_set.add('Grape')
print(fruits_set)
#Output {'Apples', 'Oranges', 'Grape', 'Mango'}

# Remove from set
fruits_set.remove('Grape')
print(fruits_set)
#Output {'Apples', 'Oranges', 'Mango'}

# Add duplicate
fruits_set.add('Apples')
print(fruits_set)

# Clear set
fruits_set.clear()
print(fruits_set)
#Output set()

# Delete
del fruits_set
print(fruits_set) 
#Output gives error message saying that it is not defined meaning that it has been deleted


