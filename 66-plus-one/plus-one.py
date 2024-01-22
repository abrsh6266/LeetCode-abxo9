class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        res = [0]*(len(digits)+1)
        if (digits[len(digits)-1]+1)//10==0:
            res[len(digits)] = digits[len(digits)-1]+1
            c = 0
        else:
            res[len(digits)] = 0
            c =1
        for i in range(len(digits)-1,0,-1):
            if c == 0:
                res[i] = digits[i-1]
            else:
                if (digits[i-1]+1)//10==0:
                    res[i] = digits[i-1]+1
                    c = 0
                else:
                    res[i] = 0
                    c = 1
        if c==1:
            res[0] = 1
        else:
            return res[1:]
        return res