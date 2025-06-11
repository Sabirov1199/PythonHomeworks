### Homework

#1. Write a Python program to handle a ZeroDivisionError exception when dividing a number by zero.

try: 
    result=100/0
except ZeroDivisionError:
    print('Cannot divide by zero!')
#2. Write a Python program that prompts the user to input an integer and raises a ValueError exception if the input is not a valid integer.

try:
    x=float('hello')
except ValueError:
    print('The value has wrong format')
except:
    print('Smth else went wrong')
#3.Write a Python program that opens a file and handles a FileNotFoundError exception if the file does not exist.

import os 
if os.path.exists('test1.txt'):
    with open ('test1.txt', 'r') as file:
        content=file.read()
        print(content)
else:
    print ('File does not exist')
#4. Write a Python program that prompts the user to input two numbers and raises a TypeError exception if the inputs are not numerical.

l1=['word', 'Exist', 'Greek']
indices=[0,1,'2']
for item in range(len(indices)):
 try:
    print(l1[indices[item]])
 except TypeError:
    print('TypeError: Check list of indices')
#5. Write a Python program that opens a file and handles a PermissionError exception if there is a permission issue.

def open_file (filename):
    try:
        with open(filename, 'w') as file:
            contents=file.read()
            print('File contents:')
            print(contents)
    except PermissionError:
        print('Error: Permission denied to open the file. ')

file_name=input('input a file name:')
open_file(file_name)
#6. Write a Python program that executes an operation on a list and handles an IndexError exception if the index is out of range.

try:
    my_list=[1,2,3,4]
    print(my_list[5])
except IndexError:
    print('Index out of range!')
except ZeroDivisionError:
    print('Cannot divide by zero!')
#7. Write a Python program that prompts the user to input a number and handles a KeyboardInterrupt exception if the user cancels the input.

try: 
    n=int(input('Input a number:'))
    print('You entered:', n)
except KeyboardInterrupt:
    print('Input canceled by the user')
    

#8. Write a Python program that executes division and handles an ArithmeticError exception if there is an arithmetic error.

def division (dividend, divisor):
    try:
        result=dividend/divisor
        print('Result:', result)
    except ArithmeticError:
        print('Error: Arithmetic error occured!')
dividend=float(input('Inpu the dividend:'))
divisor=float(input('Input the divisor:'))
division(dividend, divisor)
#9. Write a Python program that opens a file and handles a UnicodeDecodeError exception if there is an encoding issue.

def open_file(filename):
    encoding= input('Input the encoding (ASCII, UTF-16, UTF-8) for the file:')
    try:
        with open(filename, "r", encoding=encoding) as file:
            contents=file.read()
            print('Filr contents:')
            print(contents)
    except UnicodeDecodeError:
        print('Error: Encoding issue occured while reading the file.')


file_name=input('input the file name:')
open_file(file_name)
#10.Write a Python program that executes a list operation and handles an AttributeError exception if the attribute does not exist.

def test_list_operations(nums):
    try: 
        r=len(nums)
        print('Length of the list :', r)
    except AttributeError:
        print('Error: The lsit does not have a length attribute.')
nums=[1,2,3,4,5]
test_list_operations(nums)
#11. Write a Python program to read an entire text file.

def file_read(fname):
    txt=open(fname)
    print(txt.read())
file_read('test.txt')
    
#12. Write a Python program to read first n lines of a file.

def file_read_head(fname, nlines):
    from itertools import islice
    with open(fname) as f:
        for line in islice(f, nlines):
            print(line)
file_read_from_head('test.txt', 2)
#13. Write a Python program to append text to a file and display the text.

def file_read(fname):
    from itertools import islice 
    with open (fname, "w") as myfile:
        myfile.write('Python Exercises\n')
        myfile.write('Java Exercises')
    txt=open(fname)
    print(txt.read())
file_read('abc.text')
#14. Write a Python program to read last n lines of a file.

import sys
import os
def file_read_from_tail(fname,lines):
        bufsize = 8192
        fsize = os.stat(fname).st_size
        iter = 0
        with open(fname) as f:
                if bufsize > fsize:
                        bufsize = fsize-1
                        data = []
                        while True:
                                iter +=1
                                f.seek(fsize-bufsize*iter)
                                data.extend(f.readlines())
                                if len(data) >= lines or f.tell() == 0:
                                        print(''.join(data[-lines:]))
                                        break

file_read_from_tail('test.txt',2)

#15.  Write a Python program to read a file line by line and store it into a list.



def file_read(fname):
        with open(fname) as f:
                #Content_list is the list that contains the read lines.     
                content_list = f.readlines()
                print(content_list)

file_read(\'test.txt\')

#16. Write a Python program to read a file line by line and store it into a variable.



def file_read(fname):
        with open (fname, "r") as myfile:
                data=myfile.readlines()
                print(data)
file_read('test.txt')

#17. Write a Python program to read a file line by line and store it into an array.

def file_read(fname):
        content_array = []
        with open(fname) as f:
                #Content_list is the list that contains the read lines.     
                for line in f:
                        content_array.append(line)
                print(content_array)

file_read('test.txt')

#18. Write a Python program to find the longest words.

 def longest_word(filename):
    with open(filename, 'r') as infile:
              words = infile.read().split()
    max_len = len(max(words, key=len))
    return [word for word in words if len(word) == max_len]

print(longest_word('test.txt'))

#19. Write a Python program to count the number of lines in a text file.

def file_lengthy(fname):
        with open(fname) as f:
                for i, l in enumerate(f):
                        pass
        return i + 1
print("Number of lines in the file: ",file_lengthy("test.txt"))

#20. Write a Python program to count the frequency of words in a file.

from collections import Counter
def word_count(fname):
        with open(fname) as f:
                return Counter(f.read().split())

print("Number of words in the file :",word_count("test.txt"))

#21. Write a Python program to get the file size of a plain file.

def file_size(fname):
        import os
        statinfo = os.stat(fname)
        return statinfo.st_size

print("File size in bytes of a plain file: ",file_size("test.txt"))

#22. Write a Python program to write a list to a file.

 color = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
with open('abc.txt', "w") as myfile:
        for c in color:
                myfile.write("%s\n" % c)

content = open('abc.txt')
print(content.read())

#23. Write a Python program to copy the contents of a file to another file.


from shutil import copyfile
copyfile('test.py', 'abc.py')

#24. Write a Python program to combine each line from the first file with the corresponding line in the second file.

with open('abc.txt') as fh1, open('test.txt') as fh2:
    for line1, line2 in zip(fh1, fh2):
        # line1 from abc.txt, line2 from test.txtg
        print(line1+line2)
		
#25. Write a Python program to read a random line from a file.

import random
def random_line(fname):
    lines = open(fname).read().splitlines()
    return random.choice(lines)
print(random_line('test.txt'))

#26. Write a Python program to assess if a file is closed or not.

 f = open('abc.txt','r')
print(f.closed)
f.close()
print(f.closed)

#27. Write a Python program to remove newline characters from a file.

def remove_newlines(fname):
    flist = open(fname).readlines()
    return [s.rstrip('\n') for s in flist]

print(remove_newlines("test.txt"))

#28. Write a Python program that takes a text file as input and returns the number of words in a given text file.

def count_words(filepath):
   with open(filepath) as f:
       data = f.read()
       data.replace(",", " ")
       return len(data.split(" "))
print(count_words("words.txt"))

#29. Write a Python program to extract characters from various text files and put them into a list.

import glob
char_list = []
files_list = glob.glob("*.txt")
for file_elem in files_list:
   with open(file_elem, "r") as f:
       char_list.append(f.read())
print(char_list)

#30. Write a Python program to generate 26 text files named A.txt, B.txt, and so on up to Z.txt.

import string, os
if not os.path.exists("letters"):
   os.makedirs("letters")
for letter in string.ascii_uppercase:
   with open(letter + ".txt", "w") as f:
       f.writelines(letter)

#31. Write a Python program to create a file where all letters of the English alphabet are listed with a specified number of letters on each line.



import string
def letters_file_line(n):
   with open("words1.txt", "w") as f:
       alphabet = string.ascii_uppercase
       letters = [alphabet[i:i + n] + "\n" for i in range(0, len(alphabet), n)]
       f.writelines(letters)
letters_file_line(3)














