#1. is_prime(n) funksiyasi

def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True
print(is_prime(7))
#2. digit_sum(k) funksiyasi

def sum_digits3(n):
   r = 0
   while n:
       r, n = r + n % 10, n // 10
   return r
print(sum_digits3(155))
#3. Ikki sonning darajalari

def print_powers_of_two(N):
    k = 2
    while k <= N:
        print(k, end=' ')
        k *= 2
N = int(input("Enter N : "))
print_powers_of_two(N)







