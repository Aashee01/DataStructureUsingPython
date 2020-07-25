
# Binary to Integer Conversion using Stack

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
def convert(dec_number):
    s=Stack()
    while dec_number>0:
       remainder=dec_number%2
       s.push(remainder)
       dec_number=dec_number//2
    bin_number=""
    while not s.is_empty():
        bin_number=bin_number+str(s.pop())
    return bin_number
print("Binary of 56 is:",convert(56))