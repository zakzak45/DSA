#traverse a linked list 


class  Node:
    def __init__(self,value):
        self.value =value
        self.next =None
        






node  = Node(1)
node.next = Node(2)
node.next.next =Node(3)




def traverse(head):
    curr =head 
    while curr is not None:
        print(curr)
    curr.next 
    
 


