class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        island_count = 0
        island_moves = [(0,1), (1,0), (0,-1), (-1,0)]
        m = len(grid)
        n = len(grid[0])

        def discover_island(x, y):
            island_stack = [(x,y)]

            while island_stack:
                curr_x, curr_y = island_stack.pop()

                
                for move in island_moves:
                    next_x = curr_x + move[0]
                    next_y = curr_y + move[1]
                    
                    if 0 <= next_x < m and 0 <= next_y < n and grid[next_x][next_y] == "1":
                        island_stack.append((next_x, next_y))

                grid[curr_x][curr_y] = "0"

        for x in range(m):
            for y in range(n):
                if grid[x][y] == "1":
                    discover_island(x, y)
                    island_count += 1


        return island_count