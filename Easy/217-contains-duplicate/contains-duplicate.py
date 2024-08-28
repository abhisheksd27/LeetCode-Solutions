class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        h={}
        for n in nums:
            if n in h:
                return True
            else:
                h[n]=1
        return False


        