arr =[1,3,4,6,7,8,9,2,5]


def linearSearch(arr,target):
   
    for i in range(len(arr)):
        if arr[i]==target:
            print("found")
            return True
    print("not found")
    return False
    
linearSearch(arr,99)