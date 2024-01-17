class Solution:
    def maxArea(self, height: [int]) -> int:
        i,j = 0,len(height)-1
        area = 0
        while j != i:
            if height[i]<height[j]:
                current = height[i]*(j-i)
                area = max(current,area)
                i += 1
            else:
                current = height[j]*(j-i)
                area = max(current,area)
                j -= 1
        return area
                