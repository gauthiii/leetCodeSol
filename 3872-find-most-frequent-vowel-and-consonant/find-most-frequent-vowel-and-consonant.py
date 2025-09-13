class Solution:
    def maxFreqSum(self, s: str) -> int:
        s=Counter(s)

        m1=0
        m2=0

        for i,j in s.items():
            if i in ['a','e','i','o','u']:
                if j>m1:
                    m1=j
            else:
                if j>m2:
                    m2=j

        return m1+m2

        