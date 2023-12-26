class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        expected = sorted(heights)
        n = len(heights)
        ind = 0
        for i in range(n):
            if expected[i] != heights[i]:
                ind += 1
        return ind