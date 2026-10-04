# check given string is pallindrome or not

def is_palindrome(s1):
    if len(s1) == 0:
        return "string is pallindrome"
    elif s1[0] != s1[-1]:
        return "string is not pallindrome"
    else:
        return is_palindrome(s1[1:-1])

print(is_palindrome('madam'))




