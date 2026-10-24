class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        s = dict()
        for i in strs:
            t = "".join(sorted(i))
            if t in s:
                s[t].append(i)
            else:
                s[t] = [i]
        res = []
        for i in s.values():
            res.append(i)
        return res
