def slidingWindow(arr,k):
    n=len(arr)
    max_sum =curr_sum=sum(arr[:k])


    for i in range(n,k):
        max_sum += arr[i]-arr[i-k]
        max_sum=max(max_sum,curr_sum)
    return max_sum #this is for a fixed sliding window problem