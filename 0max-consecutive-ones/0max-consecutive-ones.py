class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_num = 0;
        current_num = 0
        for num in nums:
            if num == 1:
                current_num +=1
                max_num = max(max_num,current_num)
            else:
                current_num = 0
        return max_num