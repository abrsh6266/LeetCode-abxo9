class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        first_max = second_max = third_max = float('-inf')
        for num in nums:
            if first_max<num:
                first_max, second_max, third_max = num,first_max,second_max
            elif second_max<num<first_max:
                second_max,third_max = num,second_max
            elif third_max<num<second_max:
                third_max = num
        if third_max == float('-inf'):
            return first_max
        return third_max