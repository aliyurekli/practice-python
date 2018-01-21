# Divisors

value = int(input("Enter the number to find the divisors:"))

divisors = [1]
trials = range(2, int(value / 2) + 1)

for i in trials:
    if value % i == 0:
        divisors.append(i)

divisors.append(value)

print(divisors)
