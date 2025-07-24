#optimzed solution to the valid parethensis problem 

def isValid(s: str) -> bool:
    stack = []
    mapping = {')': '(', '}': '{', ']': '['}
    
    for char in s:
        if char in mapping:  
            top = stack.pop() if stack else '#'  
            if mapping[char] != top:
                return False
        else:  
            stack.append(char)
    
    return not stack 