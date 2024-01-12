class Solution:
    def intToRoman(self, num: int) -> str:
        s = str(num)
        roman = {
            1:"I",
            5:"V",
            10:"X",
            50:"L",
            100:"C",
            500:"D",
            1000:"M",
        }
        rom = ''
        i,j=0,(10**len(s))/10
        while i<len(s):
            if int(s[i])*j+j == j*5:
                rom += roman[j]+roman[j*5]
                j /= 10
                i += 1
            elif int(s[i])*j+j == j*10:
                rom += roman[j]+roman[j*10]
                j /= 10
                i += 1
            else:
                t,u = 0,0
                if (int(s[i]))>=5:
                    rom += roman[5*j]
                    u = (int(s[i]))-5
                else:
                    u = (int(s[i]))
                rom += u*roman[j]
                j /= 10
                i += 1
        return rom