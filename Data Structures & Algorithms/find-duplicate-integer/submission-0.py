class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        numbers = {}
        for num in nums:
            if num in numbers:
                return num
            else:
                numbers[num] = 1
        