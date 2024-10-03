from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # Get the number of rows and columns
        rows, cols = len(grid), len(grid[0])
        
        # Initialize the queue for BFS
        queue = deque()
        fresh_oranges = 0  # Keep track of the number of fresh oranges
        minutes_passed = 0  # To count the minutes it takes for all oranges to rot
        
        # Step 1: Initialize the queue with all the rotten oranges and count fresh oranges
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r, c))  # Add rotten orange positions to the queue
                elif grid[r][c] == 1:
                    fresh_oranges += 1  # Count the fresh oranges
        
        # If there are no fresh oranges initially, return 0
        if fresh_oranges == 0:
            return 0
        
        # Step 2: BFS to process the grid level by level (minute by minute)
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # 4-directional movement (right, left, down, up)
        
        while queue and fresh_oranges > 0:
            minutes_passed += 1  # Each iteration of BFS corresponds to 1 minute
            # Process all oranges in the queue (all rotten at the current minute)
            for _ in range(len(queue)):
                r, c = queue.popleft()
                
                # Check all 4-directionally adjacent cells
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    # If the adjacent cell is in bounds and has a fresh orange, rot it
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                        grid[nr][nc] = 2  # Rot the fresh orange
                        fresh_oranges -= 1  # Reduce the count of fresh oranges
                        queue.append((nr, nc))  # Add this new rotten orange to the queue
        
        # Step 3: Check if there are any remaining fresh oranges
        if fresh_oranges == 0:
            return minutes_passed
        else:
            return -1  # There are still fresh oranges that couldn't be rotted
