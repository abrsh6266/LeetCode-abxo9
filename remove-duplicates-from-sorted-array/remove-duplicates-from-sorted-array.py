class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        length = 0
        ite = 0
        while ite < len(nums) and len(nums) != 0:
            if(nums[length]==nums[ite]):
                ite += 1
            else:
                length +=1
                nums[length]=nums[ite]
                ite +=1
        return length+1;