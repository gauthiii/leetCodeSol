class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        y=[]

        for i in range(len(words)):
            if x in words[i]:
                y.append(i)
        
        return y
        