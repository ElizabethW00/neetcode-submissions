class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:     
        res = []
        sub = []
        res.append(sub)
        def r(i):
            if i >= len(nums):
                return
            sub.append(nums[i])
            res.append(sub.copy())
            r(i+1)
            sub.pop()
            r(i+1)
        r(0)
        return res