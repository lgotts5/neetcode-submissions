class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        nums = hand
        nums.sort()
       
        while nums:
            start = nums[0]
            for i in range(groupSize):
                if start + i not in nums:
                    return False
                nums.remove(start+i)
        return True

                



        