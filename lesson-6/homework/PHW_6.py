#1. Given a string txt, insert an underscore (_) after every third character. If a character is a vowel or already has an underscore after it, shift the underscore placement to the next character. No underscore should be added at the end.

word = input("Enter a word: ")
new_word = ""
vowels = "aeiouy"

for letter in word:
    if letter in vowels:
        new_word += '_'
    else:
       new_word += letter

print(new_word)

#2.Integer Squares Exercise
l = []

for i in range(5):
    l.append(i * i)
print(l)
#3. 
i = 1
while i <= 10:
    print(i)
    i += 1
x = 0
s = 0
while (x <= 10):
     s = s + x
     x = x + 1
else :
     print('The sum of first 10 integers : ',s)    

#4.Print multiplication table of a given number

l = []

for i in range(11):
    l.append(i * 2)
print(l)
#5. Display numbers from a list using a loop

numbers = [12, 75, 150, 180, 145, 525, 50]

for num in numbers:
    if num % 5 == 0 and 50 <= num <= 150:
        print(num)

#6.Count the total number of digits in a number

n=int(input("Enter number:"))
count=0
while(n>0):
    count=count+1
    n=n//10
print("The number of digits in the number are:",count)
#7. 
rows = 5

for i in range(rows, 0, -1):
    for j in range(i, 0, -1):
        print(j, end=" ")
    print()

#8. 

list1 = [10, 20, 30, 40, 50]

# Using a loop to print in reverse order
for i in range(len(list1) - 1, -1, -1):
    print(list1[i])

#9. Display numbers from -10 to -1 using a for loop

i = -10
while i <= -1:
    print(i)
    i += 1
#10. Display message “Done” after successful loop execution

numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)
for x in numbers:
    if x ==5:
        break
print ('Done')
#12. # Number of terms
n = 10

# First two terms
a, b = 0, 1

print("Fibonacci series up to 10 terms:")
for _ in range(n):
    print(a, end=" ")
    a, b = b, a + b








