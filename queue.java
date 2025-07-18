 



public class queue {
  private int[] arr;
  private int front;
  private int back;
  private int size;
  private int capacity;


  queue(int capacity){
  this.capacity =capacity;
  arr = new int[capacity];
  front=0;
  back=-1;
  size=0;
  }


  void enqueue(int item){
  if(isFull()){
    System.out.println("cannot add more stuff it is full");
    return;
  }else{
  back =(back+1)% capacity;
  arr[back]=item;
  size++;
  };

 public void dequeu(){

  }



  }




  boolean isEmpty(){
    return size ==0;
  }


  boolean isFull(){
    return size == capacity;
  }
}
