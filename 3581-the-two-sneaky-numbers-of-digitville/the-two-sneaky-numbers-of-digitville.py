class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:

        x=[] 

        for i,j in Counter(nums).items():
            if j>1:
                x.append(i)
        
        return x
        