import numpy as np

#Algoritmo de divide y vencerás para multiplicar dos números grandes con la técnica de Karatsuba
def karatsuba(x, y):
    # Base case: if either x or y is a single digit, return their product
    if x < 10 or y < 10:
        return x * y

    # Calculate the number of digits in x and y
    n = max(len(str(x)), len(str(y)))
    n2 = n // 2

    # Split x and y into high and low parts
    high1, low1 = divmod(x, 10**n2)
    high2, low2 = divmod(y, 10**n2)

    # Recursive steps
    z0 = karatsuba(low1, low2)
    z1 = karatsuba((low1 + high1), (low2 + high2))
    z2 = karatsuba(high1, high2)

    # Calculate the final result using the Karatsuba formula
    return (z2 * 10**(2*n2)) + ((z1 - z2 - z0) * 10**n2) + z0


# Algoritmo de Schonhage-Strassen para multiplicar dos matrices 



    if __name__ == '__main__':
        # Test the Schonhage-Strassen algorithm
        x = 12345678
        y = 91011120
        result = schonhage_strassen(x, y)
        print(f"The result of {x} * {y} using Schonhage-Strassen is {result}")

if __name__ == '__main__':
    # Test the karatsuba algorithm
    x = 12345678
    y = 91011120

    result = karatsuba(x, y)
    print(f"The result of {x} * {y} using Karatsuba is {result}")