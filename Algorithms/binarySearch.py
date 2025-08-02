arr =[2,4,5,7,8,9,10]


def binarySearch(arr,target):
    left=0
    right =len(arr)-1
    
    while left<right:
        mid =(left+right)//2
        
        if arr[mid]==target:
           print("found",mid)
           return True
        elif arr[mid]<target:
            left = mid+1
            
        else:
            right =mid-1
    print("not even in the damn thing")
    return False


binarySearch(arr, 7)