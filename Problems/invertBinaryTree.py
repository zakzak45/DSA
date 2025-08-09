


def invert(root):
    if not root :
        return
    
    stack=[root]
    
    while len(stack)>0:
        node = stack.pop()
        
        node.left,node.right = node.right ,node.left
        
        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)
    return root


#inverting a binary tree