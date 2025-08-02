


def twoSum(arr,target):
    for i in range(len(arr)):
        for j in  range(i+1, len(arr)):
             if arr[i]+arr[j]==target:
                 return [i,j]
 


arr =[1,3,5,7,8,8,6,4,3,2,5,6]
target =10

twoSum(arr,target)



