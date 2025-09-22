from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0

        rows, cols = len(grid), len(grid[0])
        island_count = 0

        # Moves to each of the 4 neighboring cells (up, down, left, right)
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        def flood_fill(start_row: int, start_col: int) -> None:
            """
            Explore and mark the entire island starting from (start_row, start_col).
            Uses an explicit stack to implement Depth-First Search.
            """
            stack = [(start_row, start_col)]
            grid[start_row][start_col] = "0"  # mark the starting cell as visited

            while stack:
                row, col = stack.pop()

                for d_row, d_col in directions:
                    neighbor_row = row + d_row
                    neighbor_col = col + d_col

                    # Check bounds and look for unvisited land
                    if (0 <= neighbor_row < rows and
                        0 <= neighbor_col < cols and
                        grid[neighbor_row][neighbor_col] == "1"):
                        grid[neighbor_row][neighbor_col] = "0"  # mark visited
                        stack.append((neighbor_row, neighbor_col))

        # Scan the entire grid
        for row_index in range(rows):
            for col_index in range(cols):
                if grid[row_index][col_index] == "1":  # found a new island
                    flood_fill(row_index, col_index)
                    island_count += 1  # count this island

        return island_count
