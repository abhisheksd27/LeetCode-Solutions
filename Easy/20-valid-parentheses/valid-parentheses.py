class Solution:
    def isValid(self, s: str) -> bool:
        Stack=[]

        hashMap ={
            ")":"(", "]":"[","}":"{"
        }


        for i in s:
            if i in hashMap:
                if Stack and Stack[-1]== hashMap[i]:
                    Stack.pop()
                else:
                    return False
            else:
                Stack.append(i)

        if Stack:
            return False
        return True
        