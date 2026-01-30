def pair_sum(arr, sum):
    # code here
    value=False
    for i in range(len(arr)-1):
        for j in range(i+1,len(arr)):
            if arr[i]+arr[j]==sum:
                value=True
    return value