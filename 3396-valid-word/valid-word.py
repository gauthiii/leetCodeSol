class Solution:
    def isValid(self, word: str) -> bool:
        vowel=['a','e','i','o','u','A','E','I','O','U']
        c=0
        v=0
        co=0

        if len(word)<3:
            return False

        for i in word:
            if i in vowel:
                v+=1
            elif (i not in vowel) and i.isalpha():
                co+=1

            if not(i.isalpha() or i.isdigit()):
                return False

        if v>=1 and co>=1:
            return True

        return False
        