class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        freq={}
        sol=[]
        for num in nums:
            if num in freq:
                freq[num]+=1
            else:
                freq[num]=1
        for x in freq.keys():
            if freq[x]> len(nums)/3:
                sol.append(x)
        return sol
