class Solution:
    def maxArea(self, height: List[int]) -> int:

        a=0
        i=0
        j=len(height)-1

        while j-i>=0:
            h = min(height[i],height[j])
            a=max(a,((j-i)*h))
            # print(i,j,h,a)
            if h == height[i]:
                i+=1
            else:
                j-=1
            

        

        return a
        