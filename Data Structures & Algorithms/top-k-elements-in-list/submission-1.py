class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        for i in nums:
            d[i] = d.get(i, 0) + 1
        
        sorted_items = sorted(d.items(), key = lambda x:x[1], reverse = True)
        return [num for num,freq in sorted_items[:k]]