class Stack():
    def __init__(self):
        self.data=[]
    
    
    
    def push(self,val:int)->None:
         self.data.append(val)
    
    
    def pop(self)->int:
        if not self.data:
            raise IndexError("empty array ")
        return self.data.pop()
    
    
    
    def top(self)->int:
        if not self.data:
            raise IndexError("to from empty stack")
        return self.data[-1]
    
    
    def is_empty(self)->bool:
        return len(self.data)==0;
    
    
    def size(self)->int:
        return len(self.data)
        
    
    
    
    
    