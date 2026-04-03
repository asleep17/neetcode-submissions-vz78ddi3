class Solution:
    def isPalindrome(self, s: str) -> bool:
        s="".join(char.lower() for char in s if char.isalnum())
        mid=len(s)//2
        j=len(s)-1
        i=0
        while i < mid:
            if s[i] != s[j]:
                return False
            j-=1
            i+=1
                
        return True