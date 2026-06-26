class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        ctn_s = {}
        ctn_t = {}

        for i in range(len(s)):
            ctn_s[s[i]] = ctn_s.get(s[i], 0) + 1
            ctn_t[t[i]] = ctn_t.get(t[i], 0) + 1
        return ctn_s == ctn_t