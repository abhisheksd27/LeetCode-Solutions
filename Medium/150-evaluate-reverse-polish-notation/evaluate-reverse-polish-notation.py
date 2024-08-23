class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        Stack=[]

        for s in tokens:
            if s== "+":
                res= Stack.pop() + Stack.pop()
                Stack.append(res)
            elif s=="-":
                a,b=Stack.pop() ,Stack.pop()
                res = b-a
                Stack.append(res)
            elif s=="*":
                res= Stack.pop() * Stack.pop()
                Stack.append(res)
            elif s=="/":
                a,b=Stack.pop() ,Stack.pop()
                res = int(b/a)
                Stack.append(res)
            else:
                Stack.append(int(s))

        return Stack[-1]
        