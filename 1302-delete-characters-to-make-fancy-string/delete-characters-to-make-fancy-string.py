class Solution:
    def makeFancyString(self, s: str) -> str:

        if len(s)<3:
            return s

        x=s[0]

        for i in range(1,len(s)-1):
            if s[i]==s[i-1] and s[i]==s[i+1]:
                continue
            else:
                x=x+s[i]

        x+=s[len(s)-1]

        return x

        