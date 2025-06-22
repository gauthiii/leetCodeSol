class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        x=[]

        if len(s)>100 or k>100 or not(s.islower()) or not(fill.islower()):
            return x
        
        while s!="":
            if len(s)>=k:
                x.append(s[:k])
                s=s[k:]
            else:
                x.append(s[:len(s)]+((k-len(s))*fill))
                s=s[len(s):]
        
        return x
        