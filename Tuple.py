# Tuple - 20CE073

# a) Write a Python program to create a tuple with different data types.
'''
tuple1 = ( 15 , 100.01 , "ABCD" , {25 , 50 , 100} , {1: 10, 2: 20} )
x = 0
for k in tuple1:
    print(type(tuple1[x]))
    x = x + 1
'''


# b) Write a Python program to create a tuple with numbers and print one item.
''''
num = 0
tuple1 = ()
while True:
    i = input("Enter text Number(Press enter to exit): ")
    if not i:
        break
    tuple1 = tuple1+(i,)
print(tuple1)
'''

# c) Write a Python program to add an item in a tuple.
'''
tuple1 = (1, 2, 3, 4, 5, 6, 7)
tuple1 = tuple1+(8,)
print(tuple1)'''

# d) Write a Python program to convert a tuple to a string
'''
str = ''
tuple = ('a','b','c','d')
for item in tuple:
    str = str + item
print(str)'''

# e) Write a Python program to find the length of a tuple.
'''
len = 0
tuple = ('a', 'b', 'c', 3.33)
for k in tuple:
    len = len + 1
print("Nuber of Elements in tuple is:", len)
'''