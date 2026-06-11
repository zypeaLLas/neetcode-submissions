class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        s = ""
        count=0
        for i in range(min(len(word1), len(word2))):
            s+=(word1[i])
            s+=(word2[i])
            count +=1
        s+=word1[count:]
        s+=word2[count:]
        return s