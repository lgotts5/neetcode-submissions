class Solution:
    def isPalindrome(self, s: str) -> bool:
        stack = []
        #"".join(s.split(sep = None))
        #print(s)
        for c in s:
            if c.isalnum():
                stack.append(c.lower())
        for c in s:
            c = c.lower()
            if c.isalnum():
                if c != stack[-1]:
                    return False
                else:
                    stack.pop()
        return len(stack) == 0
