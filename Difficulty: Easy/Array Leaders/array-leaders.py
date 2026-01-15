class Solution:
    def leaders(self, arr):
        l = [arr[-1]]
        n = len(arr)
        mx = arr[-1]
        for i in range(n-2, -1, -1):
            if (arr[i]>=mx):
                l.append(arr[i])
                mx= arr[i]
        l.reverse()
        return l