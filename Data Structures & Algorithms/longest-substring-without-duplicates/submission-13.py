class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        i,j = 0,1
        if len(s) == 0:
            return 0
        if len(s) == 1:
            return 1
        while j <= len(s):
            cur = s[i:j]
            #next is dup
            
            if j != len(s) and s[j] in cur:
                if len(cur) > res:
                    res = len(cur)
                i+=1
            else:
                j+=1
            
        cur = s[i:j]  
        if len(cur) > res:
                    res = len(cur)
        return res