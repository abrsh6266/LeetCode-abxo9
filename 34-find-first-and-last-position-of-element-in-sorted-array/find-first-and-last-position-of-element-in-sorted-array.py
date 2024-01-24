class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l,r = 0, len(nums)-1
        val = [-1]*2
        while l<=r:
            mid = (l+r)//2
            if nums[mid] == target:
                ll,rr = mid-1,mid+1
                val = [mid,mid]
                while ll>=0 and nums[ll] ==target:
                    val[0] = ll
                    ll -= 1
                while rr < len(nums) and nums[rr] == target:
                    val[1] = rr
                    rr += 1
                return val
            elif  nums[mid] < target:
                l = mid+1
            else:
                r = mid-1
        return val