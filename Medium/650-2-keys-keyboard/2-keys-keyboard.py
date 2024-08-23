class Solution:
    def minSteps(self, n: int) -> int:
        curr = 1
        curr_copied = 0
        ans = 0
        while curr < n:
            if n % curr == 0:
                curr_copied = curr
                ans += 1
            ans += 1
            curr += curr_copied
        return ans
        
        
        