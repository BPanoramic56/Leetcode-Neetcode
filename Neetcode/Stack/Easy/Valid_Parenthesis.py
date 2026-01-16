# Completed: 01/15/2026

# First "naive" submission
class Solution:
    def isValid(self, s: str) -> bool:
        if (len(s) == 0):
            return True

        stack = []

        for ch in s:
            if ch == "(" or ch == "[" or ch == "{":
                stack.append(ch)
            else:
                if len(stack) == 0:
                    return False
                current_last = stack.pop()
                if ch == ")" and current_last != "(":
                    return False
                elif ch == "]" and current_last != "[":
                    return False
                elif ch == "}" and current_last != "{":
                    return False

        return len(stack) == 0
      
# Second try, with a dictionary instead
class Solution:
    def isValid(self, s: str) -> bool:

        association_dict = {
            "(": ")",
            "{": "}",
            "[": "]"
        }

        opening = association_dict.keys()

        if (len(s) == 0):
            return True

        stack = []

        for ch in s:
            if ch in opening:
                stack.append(ch)
            else:
                if len(stack) == 0:
                    return False
                current_last = stack.pop()
                if ch != association_dict[current_last]:
                    return False

        return len(stack) == 0