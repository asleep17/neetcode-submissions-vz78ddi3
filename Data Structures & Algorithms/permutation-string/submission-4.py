from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
         l=0
         length=len(s1)
         while l <= len(s2)-length:
            if Counter(s2[l:l+length]) == Counter(s1):
                return True
            else:
                l+=1
         return False

