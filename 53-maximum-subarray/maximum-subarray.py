class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ma = nums[0]
        cur = 0
        for n in nums:
            if cur < 0:
                cur = 0
            cur += n
            ma = max(ma,cur)
        return ma
        