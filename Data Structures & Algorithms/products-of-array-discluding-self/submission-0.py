class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        outl = [1] * len(nums)
        for i in range(1, len(nums)):
            outl[i] *= outl[i-1]*nums[i-1]
        #[1,1,2,8]
        
        outr = [1]*len(nums)
        for i in range(len(nums)-2, -1, -1):
            outr[i] *= outr[i+1]*nums[i+1]
            # out[-i] *= out[i]*nums[i]
        out = [1] *len(nums)
        for i in range(len(nums)):
            out[i] = outl[i]*outr[i]
        
        return out
            