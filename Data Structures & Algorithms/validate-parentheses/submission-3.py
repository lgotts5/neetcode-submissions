class Solution:
    def isValid(self, s: str) -> bool:
        #stack gets open
        stack = []
        if len(s) <= 1:
            return False
        for i in range(len(s)):
            if s[i] == "(" or s[i] == "{" or s[i] == "[":
                stack.append(s[i])
            if s[i] == ")":
                if len(stack) == 0 or stack[-1] != "(":
                    return False
                stack.pop()
            if s[i] == "]":
                if len(stack) == 0 or stack[-1] != "[":
                    return False
                stack.pop()
            if s[i] == "}":
                if len(stack) == 0 or stack[-1] != "{":
                    return False
                stack.pop()
        print(stack)
        return len(stack) == 0
        



        