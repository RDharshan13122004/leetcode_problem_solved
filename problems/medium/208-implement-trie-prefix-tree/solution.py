class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False
class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        Current = self.root

        for character in word:
            if character not in Current.children:
                Current.children[character] = TrieNode()
            Current = Current.children[character]
        Current.isEnd = True

    def search(self, word: str) -> bool:
        Current = self.root
        for character in word:
            if character not in Current.children:
                return False
            Current = Current.children[character]
        if Current.isEnd == True:
            return True
        else:
            return False

    def startsWith(self, prefix: str) -> bool:
        Current = self.root
        for char in prefix:
            if char not in Current.children:
                return False
            Current = Current.children[char]
        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)