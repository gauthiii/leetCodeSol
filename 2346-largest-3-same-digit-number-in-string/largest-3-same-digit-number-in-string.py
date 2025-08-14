class Solution:
    def largestGoodInteger(self, num: str) -> str:
        l=[]

        if len(num)<3:
            return ""

        # if len(num)==3:
        #     return num

        for i in range(1,len(num)-1):
            if num[i-1]==num[i] and num[i]==num[i+1]:
                l.append(int(num[i]))

        if len(l)<1:
            return ""

        return str(max(l))+str(max(l))+str(max(l))


        