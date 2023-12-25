class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ev = 0;
        for i in range(n):
            if(nums[i]%2 == 0):
                nums[i],nums[ev] = nums[ev],nums[i]
                ev += 1
        return nums