
# concept of stack

class Stack():
    def __init__(self):
        self.items=[]

    def push(self,data):
        self.items.append(data)

    def pop(self):
        return self.items.pop()
    def is_empty(self):
        return self.items==[]
    def get_stack(self):
        return self.items
    def peek(self):
        return self.items[-1]
ob=Stack()
ob.push("A")
ob.push("B")
ob.push(1)
print("Elements of stack are :",ob.get_stack())
ob.pop()
print("Elements after popping:",ob.get_stack())
print("top of stack",ob.peek())