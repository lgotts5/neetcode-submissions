class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #can't use sorting because its 0(n) time

        # if you use hashmap should work because lookup is O(1)

        # make a hashset of keys and only stat counting if we know the number is the lowest in the set, meaning n-1 is not in the set
        numSet = set(nums)
        longest = 0
        for num in numSet:
            length = 0
            if num-1 not in numSet:
                length = 1
                while num+length in numSet:
                    length+=1
            if length > longest:
                longest = length
        return longest