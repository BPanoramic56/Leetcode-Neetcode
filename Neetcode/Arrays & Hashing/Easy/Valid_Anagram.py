# Completed: 01/11/2026

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        total = s + t
        for letter in total:
            if s.count(letter) != t.count(letter):
                return False
        return True