class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        carsEnum = enumerate(position)
        carsEnumSort = sorted(carsEnum, key=lambda x: x[1], reverse=True)
        time = []
        #monotonic decreasing stack to see which fleet its apart of
        for i,pos in carsEnumSort:
            time.append((target - pos)/speed[i])
        
        prevTime = time[0]
        res = 1
        for i in range(1,len(time)):
            if time[i] > prevTime:
                res +=1
                prevTime = time[i]
            else:
                time[i] = prevTime
        return res

