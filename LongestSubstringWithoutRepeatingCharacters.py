class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxlen = 0
        start = end = 0
        has_letters = set()
        cur_len = 0
        while end < len(s):
            if s[end] not in has_letters:
                has_letters.add(s[end])
                end += 1
                cur_len += 1
                maxlen = max(maxlen, cur_len)
            else:
                has_letters.remove(s[start])
                start += 1
                cur_len -= 1
        return maxlen