#User function Template for python3

class Solution:
    
    #Function to search a given integer in a matrix.
    def searchMatrix(self,matrix, x): 
    	# code here 
    	z = any(x in row for row in matrix)
    	return z
    	
    	
