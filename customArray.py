class Array:
    def __init__(self):
        self.data=[]
        
    def append(self, val:int)->None:
        self.data.append(val)
        
    def pop(self)->int:
        if not self.data:
            raise IndexError("empty array ");
        return self.data.pop()
    
    def get(self,index:int)->int:
        if index<0 or index>=len(self.data):
            raise IndexError("index out of bound")
        return self.data[index]
    
    def set(self,val:int,index:int)->int:
        if index <0  or index >=len(self.data):
            raise IndexError("index out of bound")
        self.data[index]=val
    
    def size(self)->int:
        return len(self.data)
    def __len__(self):
        return len(self.data)
    
    def isEmpty(self)->bool:
        return len(self.data)==0;
    
    
    
    
arr =Array();
    
arr.append(3)   
arr.append(10)
arr.append(45)
arr.append(23)



print(arr.get(1))
print(arr)


for i in range(len(arr)):
    print(arr())
    
    
    
    
    