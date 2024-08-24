class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        last_occurrence = {char: idx for idx, char in enumerate(s)}
        visited = set()
        stack = []

        for i in range(len(s)):
            if s[i] in visited:
                continue
            
            while stack and s[i] < stack[-1] and i < last_occurrence[stack[-1]]:
                visited.remove(stack.pop())
                
            stack.append(s[i])
            visited.add(s[i])

        return "".join(stack)
