class Solution:
    def nextPermutation(self, arr):
        n = len(arr)
        pivot = -1
        for i in range(n-2, -1, -1):
            if arr[i] < arr[i+1]:
                pivot = i
                break
        if pivot == -1:
            return arr.reverse()
        for j in range(n-1, pivot, -1):
            if arr[j]>arr[pivot]:
                arr[j], arr[pivot] = arr[pivot], arr[j]
                break
        l = pivot+1
        r = n-1
        while(l<r):
            if arr[l]>arr[r]:
                arr[l], arr[r] = arr[r],arr[l]
            l += 1
            r -= 1
        return arr