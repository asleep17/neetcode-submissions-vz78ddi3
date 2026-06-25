class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        left,right=len(word1),len(word2)
        i,j=0,0
        newword=[]
        while i<left or j < right:
            if i < left:
                newword.append(word1[i])
            if j<right:
                newword.append(word2[j])
            i+=1
            j+=1
        return "".join(newword)
    

