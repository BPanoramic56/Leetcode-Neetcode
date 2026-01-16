# Completed: 01/15/2026

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        sorted_nums = sorted(set(nums))
        longest_length = 1
        current_length = 1
        last = sorted_nums[0]

        for i in range(1, len(sorted_nums)):
            current = sorted_nums[i]
            if current - 1 == last:
                current_length += 1
            else:
                current_length = 1
            if current_length > longest_length:
                longest_length = current_length

            last = current
            
        return longest_length
                
