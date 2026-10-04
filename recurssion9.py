# WAP using recurssion to convert first character in each word to upper_case in the given list

def capitilize(l1):
    res = []
    if len(l1) == 0:
        return res
    res.append(l1[0].title())
    return res + capitilize(l1[1:])

l1 = ['kapil','got','placed','in','jp morgon']
print(capitilize(l1))


