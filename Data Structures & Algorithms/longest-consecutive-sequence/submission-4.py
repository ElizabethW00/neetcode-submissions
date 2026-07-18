class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
         count = 0
         maxCount = 0
         d = {}
         uniqueNums = set(nums)
         uniqueNums = sorted(uniqueNums)
         
         if len(nums) == 0:
             return 0

         for i in uniqueNums:
            if i + 1 in uniqueNums:
                count += 1
            else:
                count = 0
            print(count)
            maxCount = max(maxCount, count)
         return maxCount + 1



