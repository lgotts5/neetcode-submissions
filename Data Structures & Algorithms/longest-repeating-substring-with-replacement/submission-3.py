from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count  = defaultdict()
        i,j = 0,0
        alpha = ['A','B', 'C', 'D', 'E', 'F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
        maxLen = 0
        for char in alpha:
            count[char] = 0
        maxChar = 'A'
        count[s[0]] += 1
        #window loop
        while j < len(s):
            windowLen = j-i +1
            #find max
            for key in count.keys():
                if count[key] > count[maxChar]:
                    maxChar = key
            if windowLen - count[maxChar] > k:
                count[s[i]] -=1
                i+=1
            else:
                j+=1
                if j < len(s):
                    count[s[j]] +=1
                if windowLen > maxLen:
                    maxLen = windowLen
        windowLen = j-i
        if windowLen > maxLen:
            maxLen = windowLen
        return maxLen





        