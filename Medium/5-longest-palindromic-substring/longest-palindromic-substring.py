class Solution:
    def pal(self, palStr: str) -> bool:
        return palStr == palStr[::-1]

    def longestPalindrome(self, s: str) -> str:
        maxLen = 0
        longestPal = ""
        
        for i in range(len(s)):
            for j in range(i, len(s)):
                palstr = s[i: j + 1]
                if self.pal(palstr):
                    if len(palstr) > maxLen:
                        maxLen = len(palstr)
                        longestPal = palstr
        
        return longestPal
