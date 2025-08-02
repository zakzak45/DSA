from collections import deque


class Queue:
    def __init__(self):
         self.data =deque()
                  
    def enqueue(self,val:int)->None:
        self.data.append(val)
        
    def dequeue(self)->int:
        if not self.data:
            raise IndexError("Dequeue from empty queue")
        return self.data.appendleft()
    
    
    def front(self)->int:
        if not self.data:
            raise IndexError("queue is empty ")
        return self.data[0]
        
        
    def is_empty(self)->bool:
        return len(self.data)==0
    
    def size(self)->int:
        return len(self.data)