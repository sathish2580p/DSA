# stack implementation without limited size

class STACK:
    def __init__(self):
        self.s1 = []
        
    def display(self):
        if len(self.s1) == 0:
            print('No element in stack')
        else:
            for i in range(len(self.s1)-1,-1,-1):
                print(self.s1[i])
    def push(self,val):
        self.s1.append(val)

    def pop(self):
        self.s1.pop()

    def peek_ele(self):
        print('top element in stack :',self.s1[-1])

st = STACK()
st.push(10)
st.push(20)
st.push(30)
st.display()

print()
st.pop()

print()

    