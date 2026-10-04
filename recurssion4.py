# WAP to display even and odd numbers from 1 to 10 by using recurssion

#1)
def even(n):
    if n==2:
        print(n)
    else:
        if n%2==0:
            print(n)
        even(n-1)
even(10)

#2)
def evennums(n):
    if n <= 10:
        print(n,end=' ')
        evennums(n+2)

evennums(2)