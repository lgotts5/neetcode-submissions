class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        numZero = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                numZero +=1
            else:
                product *= nums[i]
        output = []
        if numZero > 1:
            output = [0] * (len(nums))
            return output
        if numZero == 1:
            output = [0] * (len(nums))
            output[nums.index(0)] = product
            return output
        for i in range(len(nums)):
            output.append(product // nums[i])
        return output