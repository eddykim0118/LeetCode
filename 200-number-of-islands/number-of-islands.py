class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """
        Count the number of islands using DFS approach.
        
        Args:
            grid: 2D binary grid where '1' = land, '0' = water
        
        Returns:
            Number of islands (connected components of land)
        """
        if not grid or not grid[0]:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        island_count = 0
        
        def dfs(row, col):
            """
            Depth-First Search to mark all connected land cells as visited.
            """
            # Base cases: out of bounds or water/already visited
            if (row < 0 or row >= rows or 
                col < 0 or col >= cols or 
                grid[row][col] == '0'):
                return
            
            # Mark current cell as visited by changing '1' to '0'
            grid[row][col] = '0'
            
            # Explore all 4 adjacent cells (up, down, left, right)
            dfs(row - 1, col)  # up
            dfs(row + 1, col)  # down
            dfs(row, col - 1)  # left
            dfs(row, col + 1)  # right
        
        # Scan the entire grid
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == '1':  # Found unvisited land
                    island_count += 1
                    dfs(row, col)  # Mark entire island as visited
        
        return island_count


class SolutionBFS:
    def numIslands(self, grid: List[List[str]]) -> int:
        """
        Count the number of islands using BFS approach.
        """
        if not grid or not grid[0]:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        island_count = 0
        
        def bfs(start_row, start_col):
            """
            Breadth-First Search to mark all connected land cells as visited.
            """
            queue = deque([(start_row, start_col)])
            grid[start_row][start_col] = '0'  # Mark as visited
            
            directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # up, down, left, right
            
            while queue:
                row, col = queue.popleft()
                
                # Explore all 4 adjacent cells
                for dr, dc in directions:
                    new_row, new_col = row + dr, col + dc
                    
                    # Check bounds and if it's unvisited land
                    if (0 <= new_row < rows and 
                        0 <= new_col < cols and 
                        grid[new_row][new_col] == '1'):
                        
                        grid[new_row][new_col] = '0'  # Mark as visited
                        queue.append((new_row, new_col))
        
        # Scan the entire grid
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == '1':  # Found unvisited land
                    island_count += 1
                    bfs(row, col)  # Mark entire island as visited
        
        return island_count


class SolutionWithSeparateVisited:
    def numIslands(self, grid: List[List[str]]) -> int:
        """
        Count islands using separate visited array (doesn't modify input).
        """
        if not grid or not grid[0]:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        visited = [[False] * cols for _ in range(rows)]
        island_count = 0
        
        def dfs(row, col):
            if (row < 0 or row >= rows or 
                col < 0 or col >= cols or 
                visited[row][col] or 
                grid[row][col] == '0'):
                return
            
            visited[row][col] = True
            
            # Explore 4 directions
            dfs(row - 1, col)
            dfs(row + 1, col)
            dfs(row, col - 1)
            dfs(row, col + 1)
        
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == '1' and not visited[row][col]:
                    island_count += 1
                    dfs(row, col)
        
        return island_count