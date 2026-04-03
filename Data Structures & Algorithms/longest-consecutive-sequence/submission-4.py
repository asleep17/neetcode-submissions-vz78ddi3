class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        arr=sorted(list(set(nums)))
        top=1
        bottom=0
        max_count=1
        count=1
        if len(nums)==0:
            return 0
        while bottom<len(arr)-1:
            if arr[top]-arr[bottom]==1:
                count+=1
            else:
                count=1
            if count>max_count:
                max_count=count
            top+=1
            bottom+=1
        return max_count
        
               
