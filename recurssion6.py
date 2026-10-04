# program to find sum of all list elements using recurssion
l = [1,2,3,4,5]
def sumoflist(n):
    if n == 0:
        return l[0]
    else:
        return l[n] + sumoflist(n-1)
print(sumoflist(len(l)-1))



# def sumoflist(l1):
#     if len(l1) == 0:
#         return 1
#     else:
#         return l1[0] + sumoflist(l1[1:])
    
# l1 = [1,2,3,4,5]
# print(sumoflist(l1))