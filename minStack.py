


class minStack:
    def __init__(self):
        self.stack =[]

    def pop(self):
       if self.isEmpty():
           raise ValueError("stack is empty")
       return self.stack.pop()
    
    def push(self,value):
        return self.stack.append(value)

    def peek(self):
       if self.isEmpty():
           raise ValueError("stack is empty ")
       return self.stack[-1]

    def size(self):
        return len(self.stack)

    def isEmpty(self):
        return len(self.stack) ==0
    





Stack =  minStack()


Stack.push(10)
Stack.push(20)
Stack.push(30)
Stack.push(40)
Stack.push(50)
Stack.push(60)




print(Stack.stack)
print(Stack.isEmpty())
print(Stack.peek())
print(Stack.size())
print(Stack.pop())





    