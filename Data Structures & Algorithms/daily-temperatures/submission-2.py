class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        count=1
        res=[]
        for i in range(len(temperatures)):
            j=i+1
            count=1
            while j < len(temperatures):
                if temperatures[j]>temperatures[i]:
                    break
                count+=1
                j+=1
            if j == len(temperatures):
                count=0
            res.append(count)

        return res