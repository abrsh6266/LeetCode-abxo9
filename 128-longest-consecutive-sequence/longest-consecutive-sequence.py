class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numy = sorted(nums)
        n = len(nums)
        l = 1
        g = 1
        if len(numy) == 0:
            return 0
        for i in range(1,n):
            if numy[i]== numy[i-1]:
                continue
            if numy[i] == numy[i-1]+1:
                l += 1
                g = max(l,g)
            else:
                l=1
        return g