# Completed: 01/13/2026

class Solution:

    def encode(self, strs: List[str]) -> str:
        prefix = ""

        for word in strs:
            prefix += f"{len(word)}#{word}"
        
        return prefix

    def decode(self, s: str) -> List[str]:
        strs = []
        offset = 0

        while offset < len(s):
            current_size_str = ""
            current_size = 0
            number_length = 0

            for i in range(offset, len(s)):
                if s[i] == "#":
                    if not current_size_str:
                        break
                    current_size = int(current_size_str)
                    break
                else:
                    current_size_str += s[i]
                    number_length += 1
            
            total_offset = offset + number_length + 1
            strs.append(s[total_offset : total_offset + current_size])

            offset = total_offset + current_size

        return strs





                