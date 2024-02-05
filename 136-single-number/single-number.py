class Solution:
    def singleNumber(self, num: list[int]) -> int:
        nums = sorted(num)
        print(nums)
        i=0
        n = len(nums)
        while i<n:
            if i == 0 and n>1 and nums[i] != nums[i+1]:
                return nums[i]
            if i==n-1:
                return nums[i]
            if nums[i] == nums[i+1] or nums[i-1] == nums[i]:
                i += 1
            else:
                return nums[i]
        return nums[n-1]