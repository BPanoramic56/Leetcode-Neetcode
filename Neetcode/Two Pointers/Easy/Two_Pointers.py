# Completed: 01/15/2026

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(filter(str.isalnum, s.strip().lower()))

        if len(s) == 0:
            return True

        left_index = 0
        right_index = len(s) - 1

        while left_index <= right_index:
            if s[left_index] != s[right_index]:
                return False

            left_index+=1
            right_index-=1

        return True