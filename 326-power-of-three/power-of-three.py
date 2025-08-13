class Solution:
    def isPowerOfThree(self, n: int) -> bool:

        if n<=0:
            return False

        if n==1:
            return True

        for i in range(30):
            if n==(3**i):
                return True

        return False

        
        