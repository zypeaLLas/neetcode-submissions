class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        """
        TWO POINTERS
        SOL
        """
        i,j = 0, 0
        s=[]
        while i < len(word1) and j < len(word2):
            s.append(word1[i])
            s.append(word2[j])
            i+=1
            j+=1
        s.append(word1[i:])
        s.append(word2[j:])
        return "".join(s)
        # s = ""
        # i=0
        # while i < min(len(word1), len(word2)):
        #     s+=(word1[i])
        #     s+=(word2[i])
        #     i +=1
        # s+=word1[i:]
        # s+=word2[i:]
        # return s