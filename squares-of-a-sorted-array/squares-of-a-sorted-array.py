from typing import List

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        l,r = 0, n-1
        val = [0]*n
        i = n-1
        while l<=r:
            lv = nums[l]**2
            rv = nums[r]**2
            if lv>=rv:
                val[i] = lv
                l += 1
            else:
                val[i] = rv
                r -=1
            i -=1
        return val