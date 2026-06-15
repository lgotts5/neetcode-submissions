class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        result = []
        for interval in intervals:
        # If result is empty or no overlap with the last interval in result
            if not result or result[-1][1] < interval[0]:
                result.append(interval)  # Add the interval as is
            else:
                # Merge overlapping intervals
                result[-1][1] = max(result[-1][1], interval[1])
    
        return result
        