

arr =[3,4,5,6,6,7,4,9,8,23]
target =9


def TwoPointer(arr,target):
    l,r=0,len(arr)-1
    
    while l<r:
        current_sum =arr[l]+arr[r]
        
        if target == current_sum:
            return[l+1,r+1]
        elif current_sum<target:
            l=l+1
        else :
            r=r-1
    return [-1,-1]