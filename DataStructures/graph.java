import java.util.*;

public class graph {
    private Map<String, List<String>> adjList = new HashMap<>();  

    public void addVertex(String label) {
        adjList.putIfAbsent(label, new ArrayList<>());
    }

   
    public void addEdge(String src, String dest) {
        adjList.get(src).add(dest);
        adjList.get(dest).add(src); 

  
    public void printGraph() {
        for (String vertex : adjList.keySet()) {
            System.out.println(vertex + " -> " + adjList.get(vertex));
        }
    }
}

