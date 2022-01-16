# Dictionary - 20CE073

#a) Write a Python script to check whether a given key already exists in a dictionary.
'''
def checkKey(dict,Key):

    if Key in dict.keys():
        print("Key",Key,"is Present and the value is",dict[Key])
    else:
        print("Key",Key,"is not Present.")

dict = {'q':200 , 'w':300 , 'e':400}

Key = 'q'
checkKey(dict, Key)
Key = 'e'
checkKey(dict, Key)
'''

#b) Write a Python script to merge two Python dictionaries.
'''
dict1 = { 'a':100,'b':200,'c':300 }
dict2 = { 'x':400,'y':500,'z':600 }

print(dict1 | dict2)

# Another method using update() method
def Merge(dict1, dict2):
    return(dict1.update(dict2))

Merge(dict1, dict2)

# changes made in dict2
print(dict1)
'''


#C) Write a Python program to sum all the items in a dictionary.
'''
sum = 0  #For Storing value of Sum of Dictionary

dict1 = { 'a': 100,'b': 200,'c': 300 , 'd': 400 }

for k in dict1:
    sum += 1

print(sum)
'''



#d) Write a Python script to add a key to a dictionary.
'''
dict1 = { 'a': 100,'b': 200,'c': 300 }

dict1['d'] = 400

print(dict1)
'''




#e) Write a Python script to concatenate the following dictionaries to create a new one.
'''
dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}
dic4 = {}

for k in (dic1,dic2,dic3):
    dic4.update(k)

print(dic4)
'''