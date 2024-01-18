class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if not s: return 0
        N=len(s)
        start=0
        c=Counter(s[0])
        for end in range(1,N):
            c[s[end]] += 1
            countOfMostCommonChar = c.most_common(1)[0][1]
            lengthOfWindow = end-start+1
            numOpsToMakeWindowValid = lengthOfWindow - countOfMostCommonChar
            if numOpsToMakeWindowValid > k:
                c[s[start]]-=1
                start+=1
                
        return N - start