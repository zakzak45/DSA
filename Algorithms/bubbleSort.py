


def BubbleSort(arr):
    n=len(arr)
    for i in range(n):
         swapped=False
         print(f"Pass {i + 1}:")
         for j in range(0, n-i-1):
         
             if arr[j]>arr[j+1]:
                 arr[j],arr[j+1]=arr[j+1],arr[j]
                 swapped=True
         print(arr[j])   
         if not swapped:
            print("No swaps happened. Array is sorted early.")
            break
    return arr
             
             
arr =[2,4,5,6,7,9,676,2,4]


print(BubbleSort(arr))

