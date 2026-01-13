#1.Write  a function to convert temperature from celsius to faranit
   #c/5 = (f-32)9
def Temberature(c):
    f = (c * 9/5) + 32
    return f

print(Temberature(25))

        

# 2.write a function to count how many times each digit appears: (Digit frquescy count) for given number.
  #Given number : 546632567
  #out put: 1:0
          # 2:1

def frequency(num):
    freq = {}

    # initialize 0–9 with 0
    for i in range(10):
        freq[i] = 0

    for digit in str(num):
        freq[int(digit)] += 1

    for i in range(10):
        print(f"{i}: {freq[i]}")

frequency(546632567)


# 3.write a  function to print prime number between given range 
#for i in range (20):
 # print (i);
def prime(n):
    if n <= 1:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def primes(start, end):
    for num in range(start, end + 1):
        if prime(num):
            print(num)

primes(1,20)


#4. write a function to print Fibonacci number for given range 
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        print(a)
        a, b = b, a + b

fibonacci(10)

# 5.write a function to check the given 2 strings are palindrom or not.
def palindrome(num):
    return str(num) == str(num)[::-1]

print(palindrome(121))  # True
print(palindrome(123))  # False

#6. Method-Based Calculator English
#     create  separate methods for
  #     Addition
        #Subraction 
        #Multiplication
        #Division
#then use a loop-driven menu to run the calaulator.

a=2
b=3

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b
