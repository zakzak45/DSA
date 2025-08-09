
from collections import deque

#BFS

def BFS(start,graph):
    
    visited =set();
    queue =deque[start]#initilizes queue
    visited.add(start)
    
    while queue:
        node = queue.popleft()
        print( node ,end=" ")
    
    for neighbor in graph[node]:
        if neighbor not in visited:
            visited.add(neighbor)
            queue.append(neighbor)