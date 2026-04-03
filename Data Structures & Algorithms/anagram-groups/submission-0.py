class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res=defaultdict(list)
        for word in strs:
            sorteds=''.join(sorted(word))
            res[sorteds].append(word)
        return list(res.values())

