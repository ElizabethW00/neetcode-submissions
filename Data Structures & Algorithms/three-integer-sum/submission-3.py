class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        n = len(nums)

        for i in range(n):
            target = -nums[i]
            j = i + 1
            k = n - 1

            while j < k:
                if nums[j] + nums[k] < target:
                    j+= 1
                elif nums[j] + nums[k] > target:
                    k-=1
                else:
                    if [nums[i], nums[j], nums[k]] in res:
                        j+= 1
                        k -= 1
                        continue
                    res.append([nums[i], nums[j], nums[k]])
                    j+= 1
                    k -= 1
                    

        return res