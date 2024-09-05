class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        m = len(rolls)
        total_sum = mean * (n + m)
        missing_sum = total_sum - sum(rolls)

        # Check if it's possible to distribute missing_sum within the bounds
        if missing_sum < n or missing_sum > 6 * n:
            return []

        # Calculate the base value for all the rolls and the remainder
        avg = missing_sum // n
        remainder = missing_sum % n

        # Start with a list of avg repeated n times
        res = [avg] * n

        # Distribute the remainder by adding 1 to the first 'remainder' rolls
        for i in range(remainder):
            res[i] += 1

        return res