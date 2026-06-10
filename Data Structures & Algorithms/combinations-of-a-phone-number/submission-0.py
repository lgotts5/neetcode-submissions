class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        nums = {}
        nums[2] = "abc"
        nums[3] = "def"
        nums[4] = "ghi"
        nums[5] = "jkl"
        nums[6] = "mno"
        nums[7] = "pqrs"
        nums[8] = "tuv"
        nums[9] = "wxyz"
        result = []
        def backtrack(digits,cur):
            if len(digits) == 0:
                result.append(cur)
                return
            for char in nums[int(digits[0])]:     
                #result.append(cur)                
                backtrack(digits[1:], cur + char)
                #result.pop()
        if len(digits) == 0:                                                                                                                                                       
            return [] 
        backtrack(digits, "")
        return result


