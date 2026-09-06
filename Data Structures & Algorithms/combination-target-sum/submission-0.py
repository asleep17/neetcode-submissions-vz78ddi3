class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
       res=[]
       def dfs(i,currentlist,total):
            if total==target:
                res.append(currentlist.copy())
                return
            elif total>target or i >=len(nums):
                return 
            currentlist.append(nums[i])
            dfs(i,currentlist,total+nums[i])
            currentlist.pop()
            dfs(i+1,currentlist,total)
       dfs(0,[],0)
       return res

            

