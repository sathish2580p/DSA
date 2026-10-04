# sum of n natural numbers without using loops

def sumofnumbers(n):
    if n == 1:
        return 1
    else:
        return n  + sumofnumbers(n-1)

n = int(input('Enter the number :'))
print(sumofnumbers(n))


