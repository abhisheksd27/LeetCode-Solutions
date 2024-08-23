class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSub=nums[0]
        currentSum= 0

        for i in nums:
            if currentSum<0:
                currentSum=0
            currentSum+=i
            maxSub = max(maxSub , currentSum)
        return maxSub
        