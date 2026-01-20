#User function Template for python3
class Solution:
    # Function to find values in array equal to their indices
    
    def valueEqualToIndex(self, arr):
        l = []
        for i in range(1,len(arr)+1):
            if (i == arr[i-1]):
                l.append(i)
        return l
                