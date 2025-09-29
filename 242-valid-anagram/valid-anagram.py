class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s)!=len(t):
            return False

        hashmap={}

        for i in range(len(s)):
            hashmap[s[i]]=hashmap.get(s[i],0)+1
            hashmap[t[i]]=hashmap.get(t[i],0)-1

        return all(value == 0 for value in hashmap.values()) 
        