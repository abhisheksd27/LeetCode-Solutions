class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        length=0
        is_char=False

        for i in range(len(s)-1,-1,-1):
            if s[i]!=" ":
                length+=1
                is_char =True
            elif is_char:
                break

        return length


        