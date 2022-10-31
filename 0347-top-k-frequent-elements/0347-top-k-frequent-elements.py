class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ''''m = {}
        for i in nums:
            if i not in m:
                m[i] = 1
            else:
                m[i] += 1
        print(m)
        l = []
        for key, value in m.items():
            if key >= k:
                l.append(value)
        return l'''
        count = {}
        freq = [[] for i in range(len(nums) + 1)]
        
        for n in nums:
            count[n] = 1 + count.get(n, 0)
            
        for n, c in count.items():
            freq[c].append(n)
            
        res = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res)  == k:
                    return res