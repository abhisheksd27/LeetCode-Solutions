class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        cnt1, n = sum(nums), len(nums)
        ans = steps = cnt1 - sum(nums[:cnt1])
        for i in range(cnt1, n + cnt1):
            steps += nums[i - cnt1] - nums[i % n]
            ans = min(steps, ans)
        return ans