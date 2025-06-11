#2. Conditional Statements Exercise
# Given an integer, n, perform the following conditional actions:

# If n is odd, print Weird
# If n is even and in the inclusive range of 2 to 5, print Not Weird
# If n is even and in the inclusive range of 6 to 20, print Weird
# If n is even and greater than 20, print Not Weird
def check_weird(n):
    if n % 2 != 0:
        print("Weird")
    elif 2 <= n <= 5:
        print("Not Weird")
    elif 6 <= n <= 20:
        print("Weird")
    elif n > 20:
        print("Not Weird")

n = int(input("Enter an integer: "))
check_weird(n)

#3.Given two integer numbers a and b. Find even numbers between this numbers. a and b are inclusive. Don't use loop.

def even_numbers_with_if_else(a, b):
    if a % 2 != 0:
        a += 1
    if b % 2 != 0:
        b -= 1
    if a > b:
        return []
    return list(range(a, b + 1, 2))

# Example usage
print(even_numbers_with_if_else(3, 10))  # Output: [4, 6, 8, 10]

def even_numbers_without_if_else(a, b):
    start = a + (a % 2)
    end = b - (b % 2)
    return list(range(start, end + 1, 2)) if start <= end else []

# Example usage
print(even_numbers_without_if_else(3, 10))  # Output: [4, 6, 8, 10]

#1. 

def is_leap(year):
    leap = False
    
    # Write your logic here
    if year%400==0 :
        leap = True
    elif year%4 == 0 and year%100 != 0:
        leap = True
    return leap

year = int(input())
print(is_leap(year))



