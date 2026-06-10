class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        first = {}
        for i in range(len(s)):
            if s[i] in first:
                first[s[i]] = first[s[i]] + 1
            else:
                first[s[i]] = 1
        for i in range(len(t)):
            if not t[i] in first:
                return False
            if t[i] in first:
                if first[t[i]] == 1:
                    first.pop(t[i])
                else: first[t[i]] = first[t[i]] - 1
        return len(first) == 0


        