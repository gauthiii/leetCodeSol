class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        a=[]

        for i in strs:
            lis=[0]*26
            for j in i:
                index = ord(j) - ord('a')
                lis[index]+=1
            a.append(lis)

        hashmap={}
        
        for i in range(len(a)):
            hashmap[f"{a[i]}"]=hashmap.get(f"{a[i]}",[]) + [strs[i]]

        sol = []

        for i in hashmap.values():
            sol.append(i)
        
        return sol



        