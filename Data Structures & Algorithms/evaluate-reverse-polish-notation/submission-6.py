class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stacky = []
        print("tokens", tokens)
        ops = ["+","-","*","/"]
        for elem in tokens:
            if elem not in ops:
                stacky.append(int(elem))
            else:
                op1 = stacky.pop()
                op2 = stacky.pop()
                
                if elem=='+':
                    res = op1+op2
                elif elem=='-':
                    res = op2-op1
                elif elem=='*':
                    res = op2*op1
                else:
                    res = int(op2/op1)
                stacky.append(res)
        return stacky.pop()
        