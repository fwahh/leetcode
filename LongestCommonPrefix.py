from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        for i in range(len(strs[0])):
            if len(set(w[i:i+1] for w in strs)) != 1:
                return strs[0][:i]
        return strs[0]
    
strs = ["flower","flow","flight"]
print(Solution().longestCommonPrefix(strs))

strs = ["dog","racecar","car"]
print(Solution().longestCommonPrefix(strs))

strs = ["flow","flower","flowers"]
print(Solution().longestCommonPrefix(strs))