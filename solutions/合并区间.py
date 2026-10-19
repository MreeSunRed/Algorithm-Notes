class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        res = []
        i = 0
        intervals.sort()
        while i < len(intervals):
            val1 = intervals[i]
            temp = [val1[0], val1[1]]
            j = i
            while j < len(intervals):
                val2 = intervals[j]
                if temp[1] >= val2[0] and temp[1] <= val2[1] or val2[1] <= temp[1]:
                    temp[1] = max(val2[1], temp[1])
                    i = j
                j += 1
            res.append([temp[0], temp[1]])
            i += 1
        return res
