# Completed: 01/13/2026

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_dict = {}

        for word in strs:
            sorted_word = "".join(sorted(word))
            
            if sorted_word in anagram_dict.keys():
                anagram_dict[sorted_word] += [word]
            else:
                anagram_dict[sorted_word] = [word]

        return [x for x in anagram_dict.values()]