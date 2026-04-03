from collections import defaultdict
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        seen={}
        for i in range(len(numbers)):
            b=target - numbers[i]
            if b in seen:
                return [seen[b]+1,i+1]
            seen[numbers[i]]=i
        