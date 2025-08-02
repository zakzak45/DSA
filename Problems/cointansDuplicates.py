


def  HasDuplicates(arr):
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i] ==arr[j]:
                return True
    return False




arr =[1,4,5,6,6,7]
arr1=[4,6,8,9,10]

print(HasDuplicates(arr))