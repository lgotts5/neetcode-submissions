import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        #max output is largest pile size
        left = 1
        right = max(piles)
        #get hours for this k value
        while left < right:
            mid = (left + right) // 2
            hours = 0
            for i in range(len(piles)):
                hours = hours + math.ceil(piles[i] / mid)
            if hours <= h:
                right = mid
            else:
                left = mid + 1
        return left


        