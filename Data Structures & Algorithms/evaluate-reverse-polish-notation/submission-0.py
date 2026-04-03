class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operator=[]
        for i in range(len(tokens)):
            op=tokens[i]
            if op.isdigit() or (len(op) > 1 and op[1:].isdigit()):
                operator.append(int(op))
            else:
                b = operator.pop()
                a = operator.pop()
                if op=='+':
                    res=a+b
                elif op=='-':
                    res=a-b
                elif op=='*':
                    res=a*b
                else:
                    res=int(a/b)
                operator.append(res)
        return operator[0]