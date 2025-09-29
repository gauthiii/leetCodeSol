class Solution:

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        for s in strs:
            freq = [0] * 26
            for ch in s:
                freq[ord(ch) - ord('a')] += 1   # assumes lowercase a–z
            groups[tuple(freq)].append(s)        # tuple is hashable & safe
        return list(groups.values())

    def groupAnagrams1(self, strs: List[str]) -> List[List[str]]:
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



        