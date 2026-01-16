#User function Template for python3

class Solution:
    def rotate(self, arr):
        arr[:] = arr[-1:]+arr[:-1]
    
