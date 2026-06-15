import math
class Solution:
    def isHappy(self, n: int) -> bool:
        nums = {}
        
        while True:
            square = 0
            while (n > 0):
                print(n)
                cur = n % 10
                square += math.pow(cur,2)
                n = n // 10
            if square == 1:
                return True
            if square in nums:
                return False
            nums[square] = 1
            n = square