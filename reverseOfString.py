# concept of reverse of string using stack
#from StackData import Stack
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

def string_reverse(stack,input_str):
    for i in range(len(input_str)):
        stack.push(input_str[i])
    rev=""
    while not stack.is_empty():
        rev=rev+stack.pop()
    return rev
stack=Stack()
input_str="hello"
print(string_reverse(stack,input_str))