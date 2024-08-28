class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        

        s = "".join(map(str, digits))
        s = str(int(s) + 1)
        return [int(c) for c in s]
        

        