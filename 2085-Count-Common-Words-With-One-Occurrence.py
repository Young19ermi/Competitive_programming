class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        res= []
        for n in words1:
            if 1==words1.count(n) == words2.count(n):
                res.append(n)
                print(words1.count(n))
        return len(res)