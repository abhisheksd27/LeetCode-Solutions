class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        h={}
        
        for i,n in enumerate(numbers):
            diff= target-n
            if diff in h:
                return [h[diff],i+1]
            h[n]=i+1
        return 