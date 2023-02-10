

# How to convert a number from Decimal to Binary using recursion

def decimalToBinary(n):
    assert int(n) == n, 'Number must be an integer number'
    if n == 0:
        return 0
    else:
        return n%2 + 10 * decimalToBinary(int(n/2))

print(decimalToBinary(13.5))