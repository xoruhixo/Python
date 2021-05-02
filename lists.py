#Create List
numbers = [1,2,3,4,5]
fruits=['Apple' , 'Oranges' ,  'Grapes', 'Pears']

#Another way to create a list
numbers2 = list((1,2,3,4,5)) #(Using a constructor)
#print(numbers,numbers2)
#Output [1, 2, 3, 4, 5] [1, 2, 3, 4, 5]

#Get a value from list
print(fruits[1])
#output Oranges
#This is because like any array list also considers the value start from 0


#Get lenghth
print(len(fruits))
#Output 4

#Append to list
fruits.append('Mango')
print(fruits)
#Output ['Apple', 'Oranges', 'Grapes', 'Pears', 'Mango']


#Remove from list
fruits.remove('Grapes')
print(fruits)
#Output ['Apple', 'Oranges', 'Pears', 'Mango']

#Insert into position
fruits.insert(2, 'Strawberries')
print(fruits)
#Output ['Apple', 'Oranges', 'Strawberries', 'Pears', 'Mango']

#Remove with Pop
fruits.pop(2)
print(fruits)
#Output ['Apple', 'Oranges', 'Pears', 'Mango']

#Reverse List
fruits.reverse()
print(fruits)
#Output ['Mango', 'Pears', 'Oranges', 'Apple']


#Sort Alphabetically
fruits.sort()
print(fruits)
#Output ['Apple', 'Mango', 'Oranges', 'Pears']


#Reverse Sort
fruits.sort(reverse=True)
print(fruits)
#Output ['Pears', 'Oranges', 'Mango', 'Apple']

#Change Value
fruits[0]='Blueberries'
print(fruits)
#Output ['Blueberries', 'Oranges', 'Mango', 'Apple']









