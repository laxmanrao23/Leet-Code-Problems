class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals = sorted(intervals, key = lambda x :x[1])
        countDeleted = 0
        ending = intervals[0][1]
        for start, end in intervals[1:]:
            if  start >= ending:
                ending = end
            else:
                countDeleted += 1
                
        return countDeleted
            