class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        #greedy back tracking vibe

        nums.sort()
        
        res=[]
        def backtrack(i,curPath,curSum):
            if curSum == target:
                res.append(curPath.copy())
                return
            
            #check if this is valid
            if i >= len(nums) or curSum > target:
                return

          #add this num, pop, add other number
            
            curPath.append(nums[i])
            backtrack(i, curPath, curSum + nums[i])
            curPath.pop()
            backtrack(i + 1, curPath, curSum)
        backtrack(0,[],0)
        return res