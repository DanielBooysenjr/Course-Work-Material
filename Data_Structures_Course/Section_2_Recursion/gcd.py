

# How to find GCD (Greatest Common Divisor) of two numbers using recursion?
    # GCD is the largest positive integer that divides the numbers without a remainder

def gcd(a,b): # Recursive case -  The Flow
    assert int(a) == a and int(b) == b, 'The numbers must be an integer number' # Unintentional Case - The Constraint
    if a < 0: # Unintentional Case - The Constraint
        a = -1 * a # Unintentional Case - The Constraint
    if b < 0: # Unintentional Case - The Constraint
        b = -1 * b # Unintentional Case - The Constraint
    if b == 0: # Base Case
        return a # Base Case
    else: # Recursive case -  The Flow
        return gcd(b, a%b) # Recursive case -  The Flow

print(gcd(48,1.8)) # Recursive case -  The Flow


def fib(n):

    fib(n) vat 'n getal en roep fib(n-1) + fib(n-2)

    so fib(3) = fib(3-1) + fib(3-2)
    fib(3) = fib(2) + fib(1)

    en fib(2) = fib(1) + fib(0)
    en fib(1) = 1
    en fib(0) = 1

    so fib(2) is dan 2
    en fib(1) is dan 1

    en fib(3) = fib(2) + fib(1) = 3