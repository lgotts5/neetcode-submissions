class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #create a directed graph
        graph = {}
        for req in prerequisites:
            if req[0] not in graph:
                graph[req[0]] = [req[1]]
            else:
                graph[req[0]].append(req[1])
        
        #create curpath and visitied data structures
        visited =set()
        
        #hasCycle essentially a dfs that checks if cycle
        def hasCycle(node,curpath):
            visited.add(node)
            curpath.add(node)
        
            for neighbor in graph[node]:
                if neighbor in curpath: # cycle detected, no topo sort
                    return True
                if neighbor in visited:
                    continue
                if neighbor in graph:
                    if hasCycle(neighbor, curpath):
                        return True
                
            
            curpath.remove(node)
            
            return False

        for node in graph:
            if node not in visited:
                if hasCycle(node, set()):
                    return False # cycle detected, no topo sort
        return True

