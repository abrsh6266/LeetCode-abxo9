from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        
        if n <= 2:
            return 0
        
        left_max = [0] * n
        right_max = [0] * n
        
        left_max[0] = height[0]
        for i in range(1, n):
            left_max[i] = max(left_max[i - 1], height[i])
        
        right_max[n - 1] = height[n - 1]
        for i in range(n - 2, -1, -1):
            right_max[i] = max(right_max[i + 1], height[i])
        
        trapped_water = 0
        for i in range(1, n - 1):
            min_wall_height = min(left_max[i], right_max[i])
            trapped_water += max(0, min_wall_height - height[i])
        
        return trapped_water