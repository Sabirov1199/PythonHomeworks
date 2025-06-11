
#1. Write a Python program to ask for a user's name and year of birth, then calculate and display their age.

name= 'Alex'
age = 24

print (f'My name is {name} , and I am {age} years old')
#2. Extract car names from the following text

txt = 'LMaasleitbtui'

txt[1: :2]
#3. Extract car names from the following text:

txt = 'MsaatmiazD'

txt[-1::-2]
#4. Extract the residence area from the following text:

txt = "I'am John. I am from London"
x=txt.split('from')[1]
print(x)
#5. Write a Python program that takes a user input string and prints it in reverse order.

def my_function(x):
    return x [::-1]
mytxt = my_function("I wonder how this text looks like backwards")
print (mytxt)

#6. Write a Python program that counts the number of vowels in a given string

words=input(str('Enter the wrod here'))
vowels=('a','o','e','i','u')
number=0
for word in words:
    if word.lower() in vowels:
       number+=1
print(f"The number of vowels in {words} are {number}")

#7.Write a Python program that takes a list of numbers as input and prints the maximum value.

a = [10, 24, 76, 23, 12]

# Max() will return the largest in 'a'
largest = max(a)
print(largest)

#8. Write a Python program that checks if a given word is a palindrome (reads the same forward and backward).

def is_palindrome(word):
    """
    Checks if a word is a palindrome.

    Args:
      word: The word to check.

    Returns:
      True if the word is a palindrome, False otherwise.
    """
    processed_word = ''.join(filter(str.isalnum, word)).lower()
    return processed_word == processed_word[::-1]

# Example usage
word1 = "racecar"
word2 = "A man, a plan, a canal: Panama"
word3 = "hello"

print(f"'{word1}' is a palindrome: {is_palindrome(word1)}")
print(f"'{word2}' is a palindrome: {is_palindrome(word2)}")
print(f"'{word3}' is a palindrome: {is_palindrome(word3)}")

#9. Write a Python program that extracts and prints the domain from an email address provided by the user.

email = "user@example.com"

# Splitting the email string at the '@' symbol and accessing the second part (domain)
domain = email.split('@')[1]

print(domain)
#10. Write a Python program to generate a random password containing letters, digits, and special characters.

import random
import string

# Generate a random password of length 10 without duplicates
def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.sample(characters, length))


password = generate_password(10)
print(password)
