class Solution:
    def search(self, arr, x):
        # code here
        try:
            return arr.index(x)
        except:
            return -1