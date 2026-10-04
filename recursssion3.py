# WAP using recurssion to find the sum of given number
# 1)
def numsum(n):
    if n<10:
        return n
    else:
        a = n%10
        return a + numsum(int(n/10))
    
n= int(input('Enter the number :'))
print(numsum(n))

#2)
def numsum(n):
    if n == 0:
        return 0
    else:
        return (n%10) + numsum(n//10)
    
n= int(input('Enter the number :'))
print(numsum(n))

#3)

def numsum(n):
    return 0 if n == 0 else (n%10) + numsum(n//10)
print(numsum(123456))