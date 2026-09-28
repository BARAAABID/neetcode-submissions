class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Sliding Window Problem
        mp = {}
        l = 0 # Start of The Window
        res = 0 # Longest Length

        for r in range(len(s)):
            if s[r] in mp:
                l = max(mp[s[r]] + 1, l)
            mp[s[r]] = r
            res = max(res, r - l + 1)
        return res