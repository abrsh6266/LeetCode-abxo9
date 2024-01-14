class Solution:
    def topKFrequent(self, nums: [int], k: int) -> [int]:
        nn = {}
        current = 0
        nns = []
        for n in nums:
            if n in nn:
                nn[n] = nn[n]+1
            else:
                nn[n] = 1
        for i in range(k):
            maxi = max(nn,key = nn.get)
            nns.append(maxi)
            nn.pop(maxi)
        return nns