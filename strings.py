name = "Rachana"
age= 26

#Concatenation
#print('Hello, my name is ' + name)

#print('Hello, my name is ' + name + 'and I am ' + age) 
#We get a error message for this print statement as age is an int value and we can only concatinate strings
#hence  to use age we will change the type of age and convert it fron int to string

#Correct Statement
#print('Hello, my name is ' + name + ' and I am ' + str(age))


#string formatting


#Argument by position
#print('My name is {name} and I am {age}'.format(name=name, age=age))
#Using this method we dont have to do string casting 

#another method to do the same is using F-Strings (Only avaible in 3.6+ Vesrions)

#print (f'Hello, my name is {name}  and I am {age}')


#string Methods

s= 'hello world'

#Capatalise String
print(s.capitalize())

#Make all lower
print(s.lower())

#make all uppercase
print(s.upper())


#Swap Case
print(s.swapcase())


#Get Length
print(len(s))


#Replace
print(s.replace('world', 'everyone'))


#Count
sub= 'h'
print(s.count(sub))


#Starts with
print(s.startswith('hello'))


#Ends with
print(s.endswith('world'))

#Splint inti a list
print(s.split())


#Find position
print(s.find('r'))


#Is all alphanumeric
print(s.isalnum())


#Is all alphabetic
print(s.isalpha())



#Is all numeric
print(s.isnumeric())





