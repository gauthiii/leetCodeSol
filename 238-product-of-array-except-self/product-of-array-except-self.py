class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        pre=1
        post=1

        x=[]

        #forward
        for i in range(len(nums)):
            if i==0:
                x.append(pre)
            else:
                x.append(nums[i-1]*x[i-1])

        print(x)

        #reverse
        for i in range(len(nums)-1,-1,-1):
            if i==len(nums)-1:
                x[i]=x[i]*post
            else:
                x[i]=post*x[i]
            post=nums[i]*post

        print(x)

        return x

        

        