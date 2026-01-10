#User function Template for python3

class Solution:
    def countOfElements(self, x, arr):
        # Code Here
        c = 0 
        for i in arr:
            if i <= x:
                c+=1
        return c

