class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i = 0
        j = len(heights) - 1
        curMax = 0
        while i < j:
            volume = (j -i) * min(heights[j], heights[i])
            if volume > curMax:
                curMax = volume
            if heights[j] < heights[i]:
                j = j - 1
            else:
                i = i +1
        return curMax