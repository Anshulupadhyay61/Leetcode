class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        ans = 0
        i = 0
        n = len(s) - 2

        while i < n:
            if s[i] == s[i+1] or s[i+1] == s[i+2] or s[i] == s[i+2]:
                i += 1
            else:
                ans += 1
                i += 1
        return ans
