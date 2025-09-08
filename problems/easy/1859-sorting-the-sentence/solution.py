class Solution:
    def sortSentence(self, s: str) -> str:
        s = s.split(" ")
        sorting = sorted(s, key = lambda x: x[-1])
        return " ".join(word[:-1] for word in sorting)