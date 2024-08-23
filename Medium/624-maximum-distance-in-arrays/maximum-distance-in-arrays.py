class Solution:
    def maxDistance(self, arrays):
        max_val, min_val, mx = float("-inf"), float("inf"), 0

        for i in arrays:
            mx = max(mx, max(max_val-i[0],i[-1]-min_val))
            max_val = max(max_val,i[-1])
            min_val = min(min_val,i[0])

        return mx

        