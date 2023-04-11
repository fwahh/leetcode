from collections import Counter
from typing import List

class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        counts = Counter(words)

        length = 0
        same_char_words = 0
        for word in list(counts.keys()):
            if counts[word] == 0:
                continue
            if word[0] == word[1]:
                div, remainder = divmod(counts[word], 2)
                if remainder:
                    same_char_words += 1
                length += 4 * div
            else:
                reversed = word[::-1]
                if reversed in words:
                    removed = min(counts[word], counts[reversed])
                    length += 4 * removed
                    counts[word] = 0
                    counts[reversed] = 0

        if same_char_words:
            length += 2

        return length
    
for words in [["lc","cl","gg"],  
              ["ab","ty","yt","lc","cl","ab"], 
              ["cc","ll","xx"]]:
    print(Solution().longestPalindrome(words))