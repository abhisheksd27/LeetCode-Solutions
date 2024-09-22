class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        def countSteps(prefix, n):
            """ Count how many numbers exist starting with the given prefix up to n. """
            steps = 0
            current = prefix
            next_prefix = prefix + 1
            while current <= n:
                steps += min(n + 1, next_prefix) - current
                current *= 10
                next_prefix *= 10
            return steps
        
        current = 1
        k -= 1  # Since the first number is already 1
        
        while k > 0:
            steps = countSteps(current, n)
            
            if steps <= k:
                # If the number of steps under this prefix is less than or equal to k,
                # move to the next prefix (next sibling).
                current += 1
                k -= steps
            else:
                # Otherwise, go down to the next level (append 0 to the current prefix).
                current *= 10
                k -= 1
        
        return current