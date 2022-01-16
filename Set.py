# Set - 20CE073

#a. Write a Python program to add member(s) in a set and clear a set
'''
newset = set()
while True:
    i = input("Enter anything(Press enter to exit): ")
    if not i:
        break
    newset.add(i)
print(newset)
'''


# b. Write a Python program to remove an item from a set if it is present in the set.
'''
set = {1, 2, 3, 4}
print("Original set is:", set)
set.discard(1)
print("After discarding 1 new set is:", set)
set.discard(6)
print("After discarding 2 new set is:", set)
'''

# c. Write a Python program to create an intersection, Union, difference of sets.
'''set1 = {'a', 'b', 'c', 'd', 'e'}
set2 = {'b', 'c'}

# union
print("Union of Set1 and Set2 is:", set1 | set2)

# intersection
print("Intersection of Set1 and Set2 is:", set1 & set2)

# difference
print("Difference of Set1 and Set2 is:", set1 - set2)'''


# d. Write a Python program to find maximum and the minimum value in a set.
'''
set = {1, 2, 3, 4}
max = max(set)
min = min(set)
print("Maximum value in set is:", max)
print("Minimum value in set is:", min)'''


#Write a Python program to find the most common elements and their counts from list, tuple, dictionary.

#  For List
List = [1, 2, 3, 2, 1, 3]
counter = 0
num = List[0]
for i in List:
    curr_frequency = List.count(i)
    if (curr_frequency > counter):
        counter = curr_frequency
        num = i

print("For List:", List)
print("Most common elements is : ", num)
print("Most repeted number is: ", counter)

# For Tuple
tuple = (1, 2, 4, 5, 6, 6, 3, 6, 8, 3, 6)
L = list(tuple)
count = 0
num1 = L[0]
for i in L:
    curr_frequency = L.count(i)
    if(curr_frequency > count):
        count = curr_frequency
        num1 = i
print("For Tuple-", tuple)
print("Number which is repeted most: ", num1)
print("Most repeted number is: ", count)


#  For Dictionary
dic = {
    1: '100',
    2: '200',
    3: '200',
    4: '400',
    5: '400',
    6: '500'
}
value = dic.values()
l1 = list(value)
count = 0
name = list(l1[0])
for i in l1:
    curr_frequency = l1.count(i)
    if(curr_frequency > count):
        count = curr_frequency
        name = i
print("For Dictionary-", dic)
print("Name which is repeted most: ", name)
print("Most repeted name is: ", count)