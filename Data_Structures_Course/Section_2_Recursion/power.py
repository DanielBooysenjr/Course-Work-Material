
# Question 2 -  How to calculate the power of the number using recursion?

def power(base, exp): # Recursive case -  The Flow
    assert int(exp) == exp, 'The exponent must be an integer number' # Unintentional Case - The Constraint
    if exp == 0: # Base Case
        return 1 # Base Case
    elif exp < 0:
        return 1/base * power(base,exp+1) # Unintentional Case - The Constraint (For negative number)
    return base * power(base,exp-1) # Recursive case -  The Flow

print(power(4,-1)) # Recursive case -  The Flow