class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        S=set()
        l=0
        res=0

        for i in range(len(s)):
            while s[i] in S:
                S.remove(s[l])
                l+=1
            S.add(s[i])
            res=max(res,i-l+1)

        return res

        
        