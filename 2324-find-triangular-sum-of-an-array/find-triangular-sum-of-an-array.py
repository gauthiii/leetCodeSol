class Solution:
    def triangularSum(self, nums: List[int]) -> int:

        # print(nums, sum(nums))

        while len(nums)!=1:

            x=[]

            for i in range(len(nums)-1):

                x.append((nums[i]+nums[i+1])%10)
                i+=1
            
            # print(x, sum(x))
            nums=x

        return nums[0]

        