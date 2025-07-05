class Solution:
    def findLucky(self, arr: List[int]) -> int:
        a=Counter(arr)

        m=-1

        for i,j in a.items():
            if i==j and i>m:
                    m=i

        return m
        