class Solution:
    def isValid(self, s: str) -> bool:
      stack=[]
      for c in s:
         if c == '(' or c =='{' or c =='[':
            stack.append(c)
         else:
            if not stack:
               return False

            elif self.compare(c,stack):
               stack.pop()
            else:
               return False
        
      if stack:
         return False
      else:
         return True
    def compare(self,ch,stack):
            ope = stack[-1]
            if ope=='(' and ch ==')':
               return 1
            elif ope =='{' and ch =='}':
               return 1
            elif ope =='[' and ch ==']':
               return 1
            else:
               return 0
            
      
