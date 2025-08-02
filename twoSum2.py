


def twoPointer(arr, target):
    left ,right =0,len(arr)-1

    while left<right:
        sum = arr[left]+arr[right]

        if sum<target:
            left++
        else:
            right--