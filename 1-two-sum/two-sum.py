class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        for j in range(n-1):
            for i in range(j+1,n):
                if (nums[j]+nums[i]) == target:
                    return sorted([i,j])
        return []