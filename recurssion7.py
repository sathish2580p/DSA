# reverse the given string using recurssion

def reverse_str(s1):
    if len(s1) == 1:
        return s1
    else:
        return s1[-1] + reverse_str(s1[:-1])

print(reverse_str('python coding is awesome'))




    