class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # count={}

        # res=0
        # maxCount =0

        # for n in nums:
        #     count[n] =1+count.get(n,0)
        #     res = n if count[n] > maxCount else res
        #     maxCount = max(count[n] , maxCount)

        # return res

        count=0
        res=nums[0]

        for i in nums:
            if i==res:
                count+=1
            elif count==0:
                res=i
            else:
                count-=1
        return res



        