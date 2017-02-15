primes=[]

def prime_factor():
    n = raw_input("Please enter your number, should be > 0: ")
    try:
        n = int(n)
    except ValueError:
        print("That's not an int!")
        return
    if n <= 0:
        print "I do not like your number, please try again!"
        return
    for num in find_all(n):
        print num
    return 

def find_all(n):
    prime_numbers = [num for num in range(2, n) if is_prime(num)]
    for num in prime_numbers:
        if n % num == 0:
            yield num
            
def is_prime(num):
    try:
        if primes.index(num) >= 0:
            return True
    except ValueError:
        for n in range(2, int(num**0.5)+1):
            if num % n == 0:
                return False
        primes.append(num)
        return True

prime_factor()
