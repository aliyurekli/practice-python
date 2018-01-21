# Fibonacci

cache = {1: 1, 2: 1}


def fibonacci(n):
    if n not in cache.keys():
        cache[n] = cache[n-1] + cache[n-2]


num = int(input("How many Fibonacci numbers do you want to create?"))

for i in range(3, num+1):
    fibonacci(i)

print(cache.values())

