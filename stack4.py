# alex is trying to modify this many library to arrange the books in a proper manner
# so write a program to arrange the program in books rack assuminng it is a stack,
# once it is reached limited size automatically push the book to new stack
# it should contains a functionlitys like 
# isfull(),push(),display(),pop(),popAt(),peek(),peekAt(),pushAt()

class STACK:
    def __init__(self,maxsize):
        self.maxsize = maxsize
        self.s1 = []



    def push(self,val):
        if len(self.s1) > 0 and len(self.s1[-1]) < self.maxsize:
            self.s1[-1].append(val)
        else:
            self.s1.append([val])

    def display(self):
        print(self.s1)

    def pop(self):
        if len(self.s1) == 0:
            print('stack is empty')
        else:
            if len(self.s1[-1]) > 1:
                self.s1[-1].pop()
            else:
                self.s1.pop()

    def popAt(self,st_num):
        if st_num <= len(self.s1):
            self.s1[st_num-1].pop()
        else:
            print("stack num dosen't exists")

st = STACK(4)
st.push('js')

