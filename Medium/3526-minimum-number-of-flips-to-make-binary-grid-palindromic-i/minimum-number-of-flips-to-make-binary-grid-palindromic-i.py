class Solution:
    def minFlips(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
    
        def count_flips_to_palindromic_line(line):
            flips = 0
            left, right = 0, len(line) - 1
            while left < right:
                if line[left] != line[right]:
                    flips += 1
                left += 1
                right -= 1
            return flips

        min_row_flips = sum(count_flips_to_palindromic_line(row) for row in grid)

        min_col_flips = 0
        for col in range(n):
            col_flips = count_flips_to_palindromic_line([grid[row][col] for row in range(m)])
            min_col_flips += col_flips

        return min(min_row_flips, min_col_flips)