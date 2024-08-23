class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r=0,len(nums)-1
        
        while l<=r:
            mid = (l+r)//2
            if nums[mid]==target:
                return mid

            #left direction
            elif nums[mid] >target:
                r=mid-1
            #right direction
            else:
                l=mid+1
        #ends when r<l
        return -1