<<<<<<< HEAD
public class Array{
    
=======
public class Array<T>{
    private T[] data;
    private int size;

    //first give the constructor a capacity and a size of the array is zero which means it starts at zero
    Array(int capacity){
     data = (T[]) new Object[capacity];
     size=0;
    }

   public void insert(T value){
    if(size<data.length){
        data[size++]=value;

    }else{
        System.out.println("arry is full")
    }
   }

>>>>>>> refs/remotes/origin/main
}