# WAP to check the given paranthesis is balanced or not using stack
# class Balanced:
#     def __init__(self):
#         self.stack = []

#     def is_balnced(self,s1):
#         for i in s1:
#             if i == '{' or '(' or '[':
#                 self.stack.append(i)
#             elif i == ')':
#                 if self.stack[-1] == i:
#                     self.stack.pop()
#                 else:
#                     return 'imbalanced'

#             elif i == '}':
#                 if self.stack[-1] == i:
#                     self.stack.pop()
#                 else:
#                     return 'imbalanced'

#             elif i == ']':
#                 if self.stack[-1] == i:
#                     self.stack.pop()
#                 else:
#                     return 'imbalanced'
#         if len(self.stack) == 0:
#             return 'balanced'
# b1 = Balanced()
# s1 = '({[]})'
# print(b1.is_balnced(s1))


    # def display(self):
    #         if self.IsEmpty():
    #             print('No elements in stack')
    #         else:
    #             for i in range(len(self.s1)-1,-1,-1):
    #                 print(self.s1[i])
    
    # def IsFull(self):
    #         if len(self.s1) == self.maxsize:
    #             return True
    #         else:
    #             return False
    
    #     def IsEmpty(self):
    #         if len(self.s1) == 0:
    #             return True
    #         else:
    #             return False
            
    #     def push(self,val):
    #         if self.Isfull():
    #             print('Stack is Full')
    #         else:
    #             self.s1.append(val)
    
    #     def pop(self):
    #         if self.IsEmpty():
    #             print('No elements to pop')
    #         else:
    #             self.s1.pop()
    
    #     def peek_ele(self):
    #         if self.IsEmpty():
    #             print('No elements to peek')
    #         else:
    #             print('Top ele in stack :',self.s1[-1])



# def is_balanced(s1):
#     stack = []
#     d1 = {
#         ')' : '(',
#         ']' : '[',
#         '}' : '{'
#     }
#     for char in s1:
#         if char in '([{':
#             stack.append(char)
#         elif char in ')]}':
#             if not stack or stack.pop() != d1[char]:
#                 return False
#     return len(stack) == 0

# s1 = '({{}})'
# if is_balanced(s1):
#     print('Balanced')
# else:
#     print('Not Balanced')








