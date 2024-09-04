class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        # Initialize position and direction
        x, y, direction = 0, 0, 0
        # Convert obstacles to a set for O(1) lookups
        obstacle_set = set(map(tuple, obstacles))
        # Initialize max distance
        max_distance = 0
        
        # Process each command
        for command in commands:
            if command == -1:  # Turn right
                direction = (direction + 1) % 4
            elif command == -2:  # Turn left
                direction = (direction - 1) % 4
            else:  # Move forward
                for _ in range(command):
                    # Calculate next position
                    next_x = x + directions[direction][0]
                    next_y = y + directions[direction][1]
                    # Check if next position is an obstacle
                    if (next_x, next_y) in obstacle_set:
                        break
                    # Update position
                    x, y = next_x, next_y
                    # Update max distance
                    max_distance = max(max_distance, x*x + y*y)
        
        return max_distance