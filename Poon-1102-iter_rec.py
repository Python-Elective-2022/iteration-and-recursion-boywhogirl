'''Utilizing iterative power Power with variable bases and exponents 
 For each exponent value, set the result to 1, set the result to the time base, and then return the result.
 in a recursive function Power with variable bases and exponents Return the base if exponent equals one, else, 
 return the base time the result of the function with base and exponent minus 1.
'''
exp = 0
base = 0

def iterativePower(base, exp):
    result = 1
    for i in range(exp):
        result *= base
    return result

def recursivePower(base, exp):
    if exp == 1:
        return base
    else:
        return base*(recursivePower(base, exp - 1))

print('The result of RecuursivePower: ',recursivePower(10,10))
print('The result of iterativePower:', iterativePower(5,2))
