class Solution:
    def groupAnagrams(self, strs: [str]) -> [[str]]:
        strss = {}
        for s in strs:
            sortedd = ''.join(sorted(s))
            if sortedd in strss:
                strss[sortedd].append(s)
            else:
                strss[sortedd] = [s]
        return list(strss.values())