class Solution:
    def calculateFriendliness(self, arr):
        # code here
        s = 0
        
        for i in range(0,len(arr)):
                s += abs(arr [i-1]-arr[i])
        return s
            
