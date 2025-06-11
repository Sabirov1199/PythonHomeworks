#1. Write a Python script to sort (ascending and descending) a dictionary by value

my_dic={'one':1, 'three':3,'five':5,'two':2,'four':4}
a=sorted(my_dic.items(), key=lambda x:x[1], reverse=True)

print (a)
#2.Write a Python script to add a key to a dictionary.

d1={0: 10, 1: 20}
d1.update({2:30})
print(d1)
#3. Write a Python script to concatenate the following dictionaries to create a new one.

dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}
dic4={}
for d in (dic1,dic2,dic3):
    dic4.update(d)
print(dic4)
#4. Write a Python script to generate and print a dictionary that contains a number (between 1 and n) in the form (x, x*x).

 
d=dict()
for x in range (1,5+1):
    d[x]=x*x
print(d)
#5. Write a Python script to print a dictionary where the keys are numbers between 1 and 15 (both included) and the values are the square of the keys.

d=dict()
for x in range (1,16):
    d[x]=x**2
print(d)
#1. Write a Python program to create a set.

n=set([0,1,2,3,4,5])
print(n)
#2. Write a Python program to iterate over sets.

num_set=set([0,1,2,3,4,5])
for n in num_set:
    print(n)
#3. Write a Python program to add member(s) to a set.

color_set=set()
color_set.add('Red')
print(color_set)
color_set.update(['Blue', 'Green'])
print (color_set)
#4. Write a Python program to remove item(s) from a given set.

num_set= set([0,1,2,3,4,5])
num_set.pop()
print(num_set)
#5. Write a Python program to remove an item from a set if it is present in the set.

num_set= set([0,1,2,3,4,5])
num_set.discard(3)
num_set.remove(1)
print(num_set)


