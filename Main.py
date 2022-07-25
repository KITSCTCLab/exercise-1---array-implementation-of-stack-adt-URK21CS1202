import os
class Stack:
    def __init__(self, size):
        self.items = []
        self.size = size

    def is_empty(self):
        return self.top ==-1

    def is_full(self):
        return self.top==self a-1

    def push(self, data):
        if not self.is_full():
            print ("the stack is full")
        else:
            self.top==-1
            x=int(input("enter the data to inserted"))
            self.st[self.top]=x

    def pop(self):
        if not self.is_empty():
            print("the stack is empty")
        else:
            y=self.st(self.top)
            del self.st(self.top)
            self.top-=1
            return y

    def status(self):
        for in self.st:
            print(i)

# Do not change the following code
size, queries = map(int, input().rstrip().split())
stack = Stack(size)
for line in range(queries):
    values = list(map(int, input().rstrip().split()))
    if values[0] == 1:
        stack.push(values[1])
    elif values[0] == 2:
        stack.pop()
stack.status()
