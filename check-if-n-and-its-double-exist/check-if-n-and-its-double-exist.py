class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        if len(arr)== 0 or len(arr)==1:
            return false
        for i in range(len(arr)):
            for j in range(1 + i,len(arr)):
                if arr[i] == 2*arr[j] or arr[j] == 2*arr[i]:
                    return True
        return False