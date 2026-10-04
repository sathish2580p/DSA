# stack implementation with limited size

class STACK:
    def __init__(self,maxsize):
        self.maxsize = maxsize
        self.s1 = []

    def display(self):
        if self.IsEmpty():
            print('No elements in stack')
        else:
            for i in range(len(self.s1)-1,-1,-1):
                print(self.s1[i])

    def IsFull(self):
        if len(self.s1) == self.maxsize:
            return True
        else:
            return False

    def IsEmpty(self):
        if len(self.s1) == 0:
            return True
        else:
            return False
        
    def push(self,val):
        if self.Isfull():
            print('Stack is Full')
        else:
            self.s1.append(val)

    def pop(self):
        if self.IsEmpty():
            print('No elements to pop')
        else:
            self.s1.pop()

    def peek_ele(self):
        if self.IsEmpty():
            print('No elements to peek')
        else:
            print('Top ele in stack :',self.s1[-1])

st = STACK(5)
while True:
    print('--------------STACK OPERATIONS---------------------')
    print('1.IsFull\n2.IsEmpty\n3.push\n4.pop\n5.peek_ele\n6.display')
    opt = int(input('Enter your option :'))
    match opt:
        case 1:
            print('Is stack is full :-',st.IsFull)
        case 2:
            print('Is stack is empty :-',st.IsEmpty)
        case 3:
            val = input('Enter the ele :')
            st.push(val)
        case 4:
            st.pop()
        case 5:
            st.peak_ele()
        case 6:
            st.display()
        case _:
            print('In valid option')



