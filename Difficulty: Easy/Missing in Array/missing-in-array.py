class Solution:
    def missingNum(self, arr):
        # code here
        n = len(arr) + 1
        s = n*(n+1)/2
        s2 = sum(arr)
        return int(s - s2)
                