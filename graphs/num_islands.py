def numIslands(grid):
        # DFS Helper
        def explore(grid, row, col, seen):
            # Bound Checking
            rowInbound = (0 <= row) and (row < len(grid))
            colInbound = (0 <= col) and (col < len(grid[0]))
            if not rowInbound or not colInbound:
                return False
            
            # Check for Water
            if grid[row][col] == "0":
                return False

            pos = f"{row},{col}"
            
            if pos in seen:
                return False
            
            seen.add(pos)

            # Recursive Exploring
            explore(grid, row-1, col, seen)
            explore(grid, row+1, col, seen)
            explore(grid, row, col-1, seen)
            explore(grid, row, col+1, seen)

            return True

        # Driver Code
        seen = set()
        count = 0
        # Let's traverse through this grid graph
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if explore(grid, r, c, seen):
                    count += 1
        return count