

#printing  1 to N without loops 

def loops(n):
    if n>0:
     print(n,end=" ")
     loops(n-1)

    
    
loops(10)


