class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        s = ""
        i=0
        while i < min(len(word1), len(word2)):
            s+=(word1[i])
            s+=(word2[i])
            i +=1
        s+=word1[i:]
        s+=word2[i:]
        return s