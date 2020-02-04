def fibosum(n):
    a = 0
    b = 1
    suma = 0
    for i in range(n):
        c = a + b
        a = b
        b = c
        suma = suma + a
    return suma


print("Sum of the first 5 terms of the Fibonacci series:", fibosum(5))
print("Sum of the first 10 terms of the Fibonacci series:", fibosum(10))
