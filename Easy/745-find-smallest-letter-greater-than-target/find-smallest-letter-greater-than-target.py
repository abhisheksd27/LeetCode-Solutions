class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        l, r = 0, len(letters) - 1
    
        # If the target is greater than or equal to the last element
        # the answer should be the first element in the array
        if target >= letters[-1]:
            return letters[0]
        
        while l <= r:
            mid = l + (r - l) // 2
            if letters[mid] > target:
                r = mid - 1
            else:
                l = mid + 1
        
        # l is the smallest index where letters[l] is greater than target
        return letters[l]
        