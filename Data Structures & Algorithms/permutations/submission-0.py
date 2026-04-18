class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        permutation=[[]]
        for num in nums:
            new_perm=[]
            for p in permutation:
                for i in range(len(p) +1):
                    perm_copy=p.copy()
                    perm_copy.insert(i,num)
                    new_perm.append(perm_copy)
            permutation=new_perm
        return permutation
        
    


        