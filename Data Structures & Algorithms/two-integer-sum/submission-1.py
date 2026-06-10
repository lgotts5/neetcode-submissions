class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        enumerated_nums = sorted((val,index) for index, val in enumerate(nums))
        i = 0
        j = len(nums) - 1
        curSum = enumerated_nums[i][0] + enumerated_nums[j][0]
        while curSum != target:
            if i == j:
                continue
            if curSum > target:
                j = j-1
            if curSum < target:
                i = i + 1
            curSum = enumerated_nums[i][0] + enumerated_nums[j][0]
        return sorted([enumerated_nums[i][1], enumerated_nums[j][1]])
        