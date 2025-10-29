class Solution:
    def smallestNumber(self, n: int) -> int:
        s=0
        x=[]

        for i in range(10):
            s+=2**i
            x.append(s)

        for i in x:
            if i>=n:
                return i

        return s
        