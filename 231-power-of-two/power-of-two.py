class Solution:
    def isPowerOfTwo(self, n: int) -> bool:

        if n==1:
            return True
        
        if n%2==1:
            return False

        for i in range(32):
            if n==(2**i):
                return True
        
        return False
        