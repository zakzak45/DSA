import java.util.*;

public class Hashmap {
    public static void main(String args){
       Hashtable<Integer,String> table = new Hashtable<>(10);
           table.put(100,"spongebob");
           table.put(123,"alfred");
           table.put(134,"naruto");
           table.put(444,"rimuru");
           table.put(767,"goku");


        for (Integer key: table.keySet()){
            System.out.println(key +"\t"+table.get(key));
        }

    }
}
