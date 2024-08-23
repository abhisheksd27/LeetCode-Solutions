class Solution:
    def romanToInt(self, s: str) -> int:
        H = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        res = 0
        prev_value = 0
        for n in s:
            current_value = H[n]
            if current_value > prev_value:
                res += current_value - 2 * prev_value
            else:
                res += current_value
            prev_value = current_value
        return res
