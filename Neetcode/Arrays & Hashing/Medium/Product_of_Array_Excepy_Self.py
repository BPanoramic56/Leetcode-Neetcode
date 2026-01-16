# Completed: 01/13/2026

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l = len(nums)
        final_list = [0] * l

        for i in range(l):
            total = 1
            for j in range(l):
                if i == j:
                    continue
                total *= nums[j]
            final_list[i] = total
        return final_list