class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3 or arr[0] >= arr[1]:
            return False
        for i in range(len(arr)-1):
            if arr[i] == arr[i+1] or (len(arr)-2 == i and arr[i] < arr[i+1]):
                return False
            elif  arr[i] > arr[i+1]:
                for j in range(i,len(arr)-1):
                    if arr[j] <= arr[j+1]:
                        return False
        return True
                
                
                