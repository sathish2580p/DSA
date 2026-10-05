# Linear QUEUE

class QUEUE:
    def __init__(self,maxsize):
        self.maxsize = maxsize
        self.q1 = []

    def IsFull(self):
        if len(self.q1) == self.maxsize:
            return True
        else:
            return False

    def IsEmpty(self):
        if len(self.q1) == 0:
            return True
        else:
            return False

    def display(self):
        if self.IsEmpty():
            print("queue is empty")
        else:
            print(self.q1)

    def Enqueue(self,val):
        if self.IsFull():
            print("queue is full")
        else:
            self.q1.append(val)

    def Dequeue(self):
        if self.IsEmpty():
            print("queue has no element")
        else:
            self.q1.pop(0)

    def peek_ele(self):
        if self.IsEmpty():
            print("queue is empty")
        else:
            print(self.q1[0])

q = QUEUE(5)

q.display()
q.Enqueue(5)
q.display()  