class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
            string=list(s)
            stack=[]
            for i,c in enumerate(string):
                if c=='(':
                    stack.append(i)
                elif c==')':
                    if stack:
                        stack.pop()
                    else:
                        string[i]=''
            
            while stack:
             string[stack.pop()]=''
            return ''.join(string)
            
            
