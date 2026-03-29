class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        result = defaultdict(list)

        for i in strs:
            sorted_s = "".join(sorted(i))
            result[sorted_s].append(i)
        return list(result.values()) 