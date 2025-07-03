arr =[1,3,4,6,7,8,9,2,5]






def linearSearch(arr, target):
    n = len(arr)
    for i in range(n):
        if arr[i] == target:
            print("found")
            return True  # ✅ Return True when found
    return False  # ✅ Return False if not found


linearSearch(arr,7)