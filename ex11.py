# Check Primality Functions


def get_number():
    return int(input("Enter the value to check prime:"))


def is_prime(num):
    if num > 1:
        if num == 2:
            return True
        else:
            divisors = [x for x in range(2, num) if num % x == 0]
            return len(divisors) == 0
    else:
        return False


a = get_number()

if is_prime(a):
    print("%d is prime" % a)
else:
    print("%d is not prime" % a)
