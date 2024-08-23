class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack=[]

        res=[]
        def backTrack(open ,close):
            if open ==close ==n:
                res.append("".join(stack))

            if open < n:
                stack.append("(")
                backTrack(open+1 ,close)
                stack.pop()
            if close < open:
                stack.append(")")
                backTrack(open ,close+1)
                stack.pop()

        
        backTrack(0,0)
        return res


        