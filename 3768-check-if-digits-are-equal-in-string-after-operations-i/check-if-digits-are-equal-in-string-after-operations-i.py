class Solution:
    def hasSameDigits(self, s: str) -> bool:

        

        while len(s)!=2:
            x=""

            for i in range(len(s)-1):
                x+=str((int(s[i])+int(s[i+1]))%10)
            
            print(x)
            s=x

        return s[0]==s[1]
        