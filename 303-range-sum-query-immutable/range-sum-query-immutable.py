class NumArray:
    def __init__(self, nums: List[int]):
        self.nums = nums
	# we must right+1, as we know when we slice [left: right]-> it returns elemenst of  left -(to) right-1(right exclusive)
	# That's why we return the sum of left to right+1(now right inclusive). It's simple.
    def sumRange(self, left: int, right: int) -> int:
        return sum(self.nums[left: right+1])


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)