public class Array<T>{
    Object[] data;
    int size;
    int capacity;


   public Array(int capacity){
     this.capacity =capacity;
     data = new Object[capacity];
     this.size =0;
    }

    public void add(T element){
      data[size]= element;
      size++;
    }
     
    public T get(int index){
        if(index<0 || index>=size){
            throw new IndexOutOfBoundsException("Index: " + index + ", Size: " + size); 
        };
        return (T) data[index];
    }
  public int Size(){
    return size;
  }
    public void Capacity(){
      if (size == data.length){
       Object [] newdata = new Object[data.length*2];
       for(int i=0;i<size;i++){
          newdata[i]=data[i];
       }
        data=newdata;
      }
    }x  


}