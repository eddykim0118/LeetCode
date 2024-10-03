class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0
        
        # Dimensions of the grid
        rows, cols = len(grid), len(grid[0])
        num_islands = 0
        
        # Helper function for DFS
        def dfs(r, c):
            # Base case: If out of bounds or the cell is water (0), return
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == '0':
                return
            # Mark the current cell as visited by changing it to '0' (water)
            grid[r][c] = '0'
            
            # Explore all four directions (up, down, left, right)
            dfs(r - 1, c)  # Up
            dfs(r + 1, c)  # Down
            dfs(r, c - 1)  # Left
            dfs(r, c + 1)  # Right
        
        # Loop through each cell in the grid
        for r in range(rows):
            for c in range(cols):
                # If we find a land cell (1), start a DFS to explore the entire island
                if grid[r][c] == '1':
                    num_islands += 1  # Increment the island count
                    dfs(r, c)  # Perform DFS to mark all connected lands
        
        return num_islands
