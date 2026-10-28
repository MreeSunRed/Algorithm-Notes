class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = dict()
        left = 0
        maxlen = 0
        for right in range(0, len(s)):
            if s[right] not in d:
                d[s[right]] = right
            else:
                if d[s[right]] >= left:
                    left = d[s[right]] + 1
                d[s[right]] = right
            maxlen = max(right - left + 1, maxlen)
        return maxlen
