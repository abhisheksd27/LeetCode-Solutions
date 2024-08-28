class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s)==Counter(t)

        # return sorted(s)==sorted(t)


        # if len(s) != len(t):
        #     return False

        # a={}
        # b={}

        # for i in range(len(s)):
        #     a[s[i]]=1+ a.get(s[i],0)
        #     b[t[i]]=1+b.get(t[i],0)

        # for i in a:
        #     if a[i] != b.get(i,0):
        #         return False
        
        # return True
            
        

        