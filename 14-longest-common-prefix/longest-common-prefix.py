class Solution:
    def longestCommonPrefix(self, strs: [str]) -> str:
        n = len(strs)
        minimum = float('inf')
        ss = ''
        for i in range(n):
            minimum = min(minimum,len(strs[i]))
        print(minimum)
        for i in range(minimum):
            cur = ss+(strs[0])[i]
            for j in range(n):
                if cur != strs[j][0:len(cur)]:
                    return ss
            ss = cur
        return ss