class Solution:
    def isValid(self, s: str) -> bool:
        opening = {'(', '{', '['}
        d = {')': '(', '}': '{', ']': '['}
        stack = []

        for i in s:
            if i in opening:
                stack.append(i)
            else:
                if len(stack) > 0:
                    op = stack.pop()
                    if d[i] != op:
                        return False
                else:
                    return False

        if len(stack) > 0:
            return False

        return True