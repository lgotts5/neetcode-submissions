class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numsDict = {}
        res = []
        for num in nums:
            if num in numsDict:
                numsDict[num] +=1
            else:
                numsDict[num] = 1
        nDsorted =sorted(numsDict.items(), key = lambda item: item[1], reverse = True)
        for i in range(k):
            res.append(nDsorted[i][0])
        return res
        