import collections


class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        res = []
        n = len(s)
        step = len(p)
        check = collections.Counter(p)
        window = collections.Counter(s[:step])
        if check == window:
            res.append(0)
        for i in range(0, n - step):
            window[s[i]] -= 1
            window[s[i + step]] += 1
            if window[s[i]] == 0:
                del window[s[i]]
            if check == window:
                res.append(i + 1)
        return res
