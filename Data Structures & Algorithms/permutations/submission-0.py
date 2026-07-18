class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        sub = []
        def r():
            if len(sub) == len(nums):
                res.append(sub.copy())
                return

            for n in nums:
                if n in sub:
                    continue
                sub.append(n)
                r()
                sub.pop()

        r()
        return res