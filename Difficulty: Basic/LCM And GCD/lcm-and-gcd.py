import math
class Solution:
    def lcmAndGcd(self, a : int, b : int) -> List[int]:
        n1 = a
        n2 = b
        
        while (a%b != 0):
            rem = a%b
            a = b
            b = rem
        gcd = b
        lcm = (n1*n2)//gcd
        return [lcm,gcd]
        
            
            
                
            