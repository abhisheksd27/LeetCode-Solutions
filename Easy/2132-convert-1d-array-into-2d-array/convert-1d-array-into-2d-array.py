class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if m*n != len(original):
            return []
        ans = []
        it = [iter(original)] * n
        for row in zip(*it):
            ans.append(row)
        return ans