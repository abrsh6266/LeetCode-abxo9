class Solution:
    def threeSum(self, nums: [int]) -> [[int]]:
        res = []
        nums.sort()
        n = len(nums)
        for i in range(n - 2):
            l, r = i + 1, n - 1
            while l < r:
                v = nums[i] + nums[l] + nums[r]
                if v == 0:
                    res.append([nums[i], nums[l], nums[r]])
                    while l < r and nums[l] == nums[l + 1]:
                        l += 1
                    while l < r and nums[r] == nums[r - 1]:
                        r -= 1
                if v < 0:
                    l += 1
                else:
                    r -= 1
        return remove_duplicate_lists(res)
def remove_duplicate_lists(lists):
    unique_tuples = set(tuple(lst) for lst in lists)
    return [list(t) for t in unique_tuples]