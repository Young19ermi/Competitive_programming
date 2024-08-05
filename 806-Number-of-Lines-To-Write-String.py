class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        current_width = 0
        lines = 1

        for n in s:
            c_width = widths[ord(n)-ord('a')]
            if c_width + current_width> 100:
                lines += 1
                current_width = c_width
            else:
                current_width += c_width    
        return [lines, current_width]