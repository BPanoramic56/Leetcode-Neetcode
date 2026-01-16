# Completed: 01/13/2026

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        top_dict = {}
        for num in nums:
            if num in top_dict.keys():
                top_dict[num] += 1
            else:
                top_dict[num] = 1
        
        print(top_dict)
        sorted_items = sorted(top_dict.items(), key=lambda kv: kv[1], reverse=True)
        return [x[0] for x in sorted_items][:k]
