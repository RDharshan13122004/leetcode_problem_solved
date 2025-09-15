# 211. Design Add and Search Words Data Structure

**Difficulty**: Medium  
**Acceptance Rate**: 44.8%  
**Problem Link**: [LeetCode #211](https://leetcode.com/problems/design-add-and-search-words-data-structure/)

## Problem Description

Design a data structure that supports adding new words and finding if a string matches any previously added string.

Implement the `WordDictionary` class:

- `WordDictionary()` Initializes the object.
- `void addWord(word)` Adds `word` to the data structure, it can be matched later.
- `bool search(word)` Returns `true` if there is any string in the data structure that matches `word` or `false` otherwise. `word` may contain dots `'.'` where dots can be matched with any letter.

## Examples

### Example 1:
```
Input
["WordDictionary","addWord","addWord","addWord","search","search","search","search"]
[[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]

Output
[null,null,null,null,false,true,true,true]

Explanation
WordDictionary wordDictionary = new WordDictionary();
wordDictionary.addWord("bad");
wordDictionary.addWord("dad"); 
wordDictionary.addWord("mad");
wordDictionary.search("pad"); // return False
wordDictionary.search("bad"); // return True
wordDictionary.search(".ad"); // return True (matches "bad", "dad", "mad")
wordDictionary.search("b.."); // return True (matches "bad")
```

## Constraints

- `1 <= word.length <= 25`
- `word` in `addWord` consists of lowercase English letters.
- `word` in `search` consist of `'.'` or lowercase English letters.
- There will be at most `2` dots in `word` for `search` queries.
- At most `10^4` calls will be made to `addWord` and `search`.

## Key Insights

1. **Trie Data Structure**: Perfect for prefix-based string operations
2. **Wildcard Support**: The `'.'` character can match any letter
3. **DFS with Backtracking**: Handle wildcard matching through recursive search
4. **Efficient Storage**: Trie provides space-efficient storage for overlapping prefixes

## Data Structure Choice: Trie (Prefix Tree)

A Trie is ideal because:
- Efficient prefix-based searching
- Natural support for character-by-character matching
- Easy to extend for wildcard matching
- Space-efficient for words with common prefixes

### Trie Node Structure:
```python
class TrieNode:
    def __init__(self):
        self.children = {}  # Dictionary to store child nodes
        self.is_end = False  # Mark end of word
```

## Implementation Approaches

### 1. Trie with DFS (Recommended)
```python
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()
    
    def addWord(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end = True
    
    def search(self, word: str) -> bool:
        return self._dfs_search(word, 0, self.root)
    
    def _dfs_search(self, word: str, index: int, node: TrieNode) -> bool:
        # Base case: reached end of word
        if index == len(word):
            return node.is_end
        
        char = word[index]
        
        if char == '.':
            # Try all possible characters
            for child in node.children.values():
                if self._dfs_search(word, index + 1, child):
                    return True
            return False
        else:
            # Regular character match
            if char not in node.children:
                return False
            return self._dfs_search(word, index + 1, node.children[char])
```

### 2. Alternative: List Storage with Linear Search
```python
class WordDictionary:
    def __init__(self):
        self.words = []
    
    def addWord(self, word: str) -> None:
        self.words.append(word)
    
    def search(self, word: str) -> bool:
        for stored_word in self.words:
            if self._match(word, stored_word):
                return True
        return False
    
    def _match(self, pattern: str, word: str) -> bool:
        if len(pattern) != len(word):
            return False
        
        for i in range(len(pattern)):
            if pattern[i] != '.' and pattern[i] != word[i]:
                return False
        return True
```

## Algorithm Walkthrough

### Adding Words:
For `addWord("bad")`:
```
Start at root
'b' → Create/move to child node
'a' → Create/move to child node  
'd' → Create/move to child node, mark is_end = True
```

### Searching with Wildcards:
For `search(".ad")`:
```
Start at root with index 0
'.' at index 0 → Try all children of root
  Try 'b' child:
    'a' at index 1 → Move to 'a' child of 'b'
    'd' at index 2 → Check if 'a' has 'd' child and is_end
    Found match: "bad"
  Return True
```

## Step-by-Step Example

Building the trie with words ["bad", "dad", "mad"]:

```
Root
├── b
│   └── a
│       └── d (end)
├── d  
│   └── a
│       └── d (end)
└── m
    └── a
        └── d (end)
```

Search operations:
- `search("pad")`: No 'p' child from root → False
- `search("bad")`: Follow b→a→d, find end marker → True
- `search(".ad")`: Try all root children, b→a→d works → True
- `search("b..")`: Follow b, try all 'a' children, find d → True

## Time and Space Complexity

### Trie Implementation:
- **addWord**: O(m) where m is length of word
- **search (no wildcards)**: O(m) where m is length of word
- **search (with wildcards)**: O(n × m) worst case, where n is number of nodes
- **Space**: O(ALPHABET_SIZE × N × M) where N is number of words, M is average length

### List Implementation:
- **addWord**: O(1)
- **search**: O(n × m) where n is number of words, m is average length
- **Space**: O(n × m)

## Edge Cases

1. **Empty dictionary**: Search returns false for any word
2. **Single character words**: `addWord("a")`, `search(".")` should work
3. **All wildcards**: `search("...")` matches any 3-letter word
4. **No matches**: Pattern doesn't match any stored word
5. **Exact matches**: No wildcards in search pattern
6. **Maximum length**: Words up to 25 characters
7. **Maximum wildcards**: Up to 2 dots in search queries

## Optimization Considerations

### Memory Optimization:
- Use arrays instead of dictionaries for fixed alphabet size
- Compress single-child paths in trie

### Performance Optimization:
- Early termination in DFS when no matches possible
- Cache frequently searched patterns

## Follow-up Questions

1. **What if wildcards can match multiple characters?** Need different algorithm (regex matching)
2. **What about case-insensitive matching?** Convert all to lowercase
3. **Support for other special characters?** Extend wildcard logic
4. **Memory constraints for large datasets?** Consider compressed tries or external storage

## Related Problems

- **208. Implement Trie (Prefix Tree)**: Basic trie implementation
- **212. Word Search II**: Board-based word search with trie
- **79. Word Search**: Single word search on board
- **10. Regular Expression Matching**: Advanced pattern matching

## Common Mistakes

1. **Forgetting to mark word end**: Must set `is_end = True` when adding words
2. **Not handling empty string**: Edge case for search function
3. **Incorrect wildcard logic**: Must try ALL possible characters for '.'
4. **Memory leaks**: Not properly managing trie nodes in some languages

## Tags
- Hash Table
- String
- Depth-First Search
- Design
- Trie