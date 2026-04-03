from collections import Counter
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        count=Counter(nums)
        for x in count.keys():
            if count[x]>=2:
                return x

        
        