class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        #use bfs ro dfs and change to 0 after visited
        m, n = len(grid), len(grid[0])
        #visited = set()
        result = 0

        def explore(grid, i, j):
            if not (0 <= i < m and 0 <= j < n):
                return
            if grid[i][j] == '0':
                return
            grid[i][j] = '0'
            #result.append(matrix[i][j])  # process the cell

            # Explore neighbors (up, down, left, right)
            for deltaI, deltaJ in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                explore(grid, i + deltaI, j + deltaJ)

        
            
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    result+=1
                    explore(grid,i, j)
                        

        
        return result
