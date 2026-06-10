class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)-1
        def bin(left,right,target):
            if (left > right):
                return -1
            if(left == right):
                return left if nums[left] == target else -1
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            if target < nums[mid]:
                return bin(left,mid,target)
            if target > nums[mid]:
                return bin(mid+1,right,target)
        return bin(left,right,target)
        