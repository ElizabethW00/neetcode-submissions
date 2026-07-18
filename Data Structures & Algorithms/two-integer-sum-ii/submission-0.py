class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        out = []
        for i in range(len(numbers)):
            if target - numbers[i] in numbers[i+1:]:
                out = [i+1, numbers.index(target-numbers[i])+1]
                return out
        return out