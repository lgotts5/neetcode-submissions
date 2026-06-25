class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = { i : [] for i in range(n)}
        visited = set()
        for edge in edges:
           
            graph[edge[0]].append(edge[1])
        
            graph[edge[1]].append(edge[0])
        
        def dfs(node):
            visited.add(node)
            print(visited)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    dfs(neighbor)
        
        count = 0

        for node in graph.keys():
            if node not in visited:
                dfs(node)
                count+=1
                print(count)
        
        return count