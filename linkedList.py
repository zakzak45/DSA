class LinkedNode:
    def __init__(self,val:int):
        self.val=val
        self.prev =None;
        self.next =None
        
class LinkedList:
    def __init__(self):
       self.head =None  
       
    def append(self,val:int)->None:
        new_node = LinkedNode(val)
        if not self.head:
            self.head =new_node
            new_node.next =new_node
            return
        curr =self.node
        while curr.next!=self.head:
              curr = curr.next
        curr.next = new_node
        new_node.next = self.head
        