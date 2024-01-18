class Solution:
        
    def combinationSum2(self, nums: List[int], target: int) -> List[List[int]]:
        
        def dfs(i, path, current_target):
            if(current_target == 0):
                ans.append(path[:])
            else:
                for j in range(i,len(nums)):
                    if(j!=i and nums[j-1] == nums[j]):
                        continue

                    if(current_target < nums[j]):
                        break

                    dfs(j+1, path + [nums[j]], current_target - nums[j])
            
        ans = []
        nums.sort()
        dfs(0,[],target)
        return ans