class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:

        freq_counter = {}
        for x in nums:
            if x in freq_counter:
                freq_counter[x] += 1
            else:
                freq_counter[x] = 1
        
        sorted_items = sorted(freq_counter.items(), key=lambda item: item[1], reverse=True)
        result = []
        for i in range(k):
            result.append(sorted_items[i][0])
            
        return result
        