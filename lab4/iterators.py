#1task
def square_generator(N):
    for i in range(N + 1):
        yield i ** 2

N = int(input())
for num in square_generator(N):
    print(num, end=" ")
print("\n")

#2task
def even_generator(n):
    for i in range(0, n + 1, 2):
        yield i

n = int(input())

first = True  
for num in even_generator(n):
    if not first:
        print(",", end=" ")
    print(num, end="")
    first = False 
    
#3task
def divisible_by_3_and_4(n):
    for i in range(n + 1):
        if i % 3 == 0 and i % 4 == 0:
            yield i

n = int(input())
for num in divisible_by_3_and_4(n):
    print(num, end=" ")
print("\n")

# 4task
def squares(a, b):
    for i in range(a, b + 1):
        yield i ** 2

a = int(input())
b = int(input())
for num in squares(a, b):
    print(num, end=" ")
print("\n")

# 5task
def countdown(n):
    while n >= 0:
        yield n
        n -= 1

n = int(input())
for num in countdown(n):
    print(num, end=" ")
print("\n")