# A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).

people = ['ABC', 'CDE', 'FGH', 'XYZ']

# # Simple for loop
for person in people:
  print(f'Current Person: {person}')
##Output Current Person: XYZ

# Break
for person in people:
  if person == 'FGH':
    break
  print(f'Current Person: {person}')
# #Output 
# Current Person: ABC
# Current Person: CDE


# Continue
for person in people:
  if person == 'FGH':
    continue
  print(f'Current Person: {person}')
##Output 
Current Person: ABC
Current Person: CDE
Current Person: XYZ


# range
for i in range(len(people)):
  print(people[i])
##Output ABC

for i in range(0, 11):
  print(f'Number: {i}')
##Output 
# Number: 0
# Number: 1
# Number: 2
# Number: 3
# Number: 4
# Number: 5
# Number: 6
# Number: 7
# Number: 8
# Number: 9
# Number: 10

# While loops execute a set of statements as long as a condition is true.

count = 0
while count < 10:
  print(f'Count: {count}')
  count += 1
# #Output 
# Count: 0
# Count: 1
# Count: 2
# Count: 3
# Count: 4
# Count: 5
# Count: 6
# Count: 7
# Count: 8
# Count: 9


