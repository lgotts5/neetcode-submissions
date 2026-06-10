class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        i = 0
        j = len(s1)
        sub = s2[i:j]
        window = sorted(sub)
        target = sorted(s1)
        while j < len(s2)+1:
            if window == target:
                return True
            i = i+1
            j = j +1
            sub = s2[i:j]
            window = sorted(sub)
        

        return False

        