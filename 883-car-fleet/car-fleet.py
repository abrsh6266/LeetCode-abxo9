class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        hours = {}
        for i in range(0 ,len(position)):
            d = target - position[i]
            if d>0:
                hours[position[i]] = d / speed[i]
        position.sort()
        cnt = 1
        hour=hours[position[-1]]
        for i in position[::-1]:
            if hours[i] > hour:
                hour = hours[i]
                cnt+=1
        return cnt