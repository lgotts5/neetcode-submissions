class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #use binary search to find cut
        left, right = 0, len(nums)-1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid

            # left side sorted
            if nums[left] <= nums[mid]:
                # if target is contained in left sorted side, go left
                if nums[left] <= target <= nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1

            # right side sorted
            else:
                # if target is contained in right sorted side, go right
                if nums[mid] <= target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1

        return -1
