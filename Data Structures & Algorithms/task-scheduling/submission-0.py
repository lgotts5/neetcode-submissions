import heapq
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        mapDict = {}
        
        for task in tasks:
            if task in mapDict:
                mapDict[task] += 1
            else:
                mapDict[task] = 1
        frequent = []
        for value in mapDict.values():
            heapq.heappush(frequent,-value)
        queue = []
        cycleNum=0
        while frequent or queue:
           
            cycleNum += 1
            
            if frequent:
                count = heapq.heappop(frequent) + 1 #decreading count but its negative
                if count != 0:
                    queue.append((count, cycleNum + n))
            if queue and queue[0][1] == cycleNum:
                heapq.heappush(frequent, queue[0][0])
                queue.pop(0)
        return cycleNum
        


        