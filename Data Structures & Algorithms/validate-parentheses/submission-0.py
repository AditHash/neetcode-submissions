class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {"]": "[", "}": "{", ")": "("}

        for ch in s:
            if ch in pairs:
                if len(stack) == 0:
                    return False

                if stack[-1] == pairs[ch]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(ch)

        return len(stack) == 0