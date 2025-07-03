class Tree:
    def __init__(self,data):
        self.data=data;
        self.left=None;
        self.right=None;
        
    def inorder(root):
        if root:
           inorder(root.left)
           print(root.data,end='')
           inorder(root.right)
    def preorder(root):
        if root:
         print(root.data)
         preorder(root.left)
         preorder(root.right)
         
    def postorder(root):
        if root:
            postorder(root.right)  
            print(root.data) 
            postorder(root.left)
            
           
            