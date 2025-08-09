#DFS


def  DFS(graph,start):
    
    stack =[start]
    visited =set()
    visited.add(start)
    
    while stack:
        node = stack.pop()
        
    if node not in visited:
        print(node, end=" ")
        visited.add(node)
        
    for neighbor in reversed(graph[node]):
        stack.append(neighbor)