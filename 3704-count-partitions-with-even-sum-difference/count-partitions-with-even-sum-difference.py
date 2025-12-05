class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        c=0

        for i in range(len(nums)-1):
            if abs(sum(nums[0:i+1])-sum(nums[i+1:len(nums)])) % 2 == 0:
                # print(nums[0:i+1],nums[i+1:len(nums)], abs(sum(nums[0:i+1])-sum(nums[i+1:len(nums)]))  )
                c+=1
        
        return c
        