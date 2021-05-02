# # Create function
# def sayHello(name):
#     print(f'Hello {name}')

# sayHello('Rachana Kumari') ##in case the defaukt parameter is missing, the output throws an error message saying missing 1 required argument
# ##Output Hello Rachana Kumari

def sayHello(name='Rachana'):
    print(f'Hello {name}')

sayHello()
##Output Hello Rachana

# Return values
def getSum(num1, num2):
     total = num1 + num2
     return total
num = getSum(3,4)
print(num)
##Output 7


# # A lambda function is a small anonymous function.
# # A lambda function can take any number of arguments, but can only have one expression. Very similar to JS arrow functions

getSum = lambda num1, num2 : num1 + num2
print(getSum(10, 3))
##Output 13
