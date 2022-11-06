class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        self.minheap, self.k = nums, k
        heapq.heapify(self.minheap)
        while len(self.minheap) > k:
            heapq.heappop(self.minheap)
            
        return self.minheap[0]