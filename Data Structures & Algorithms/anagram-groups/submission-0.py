class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        for s in range(len(strs)):
            sorted_st = sorted(strs[s])
            key = tuple(sorted_st)
            if key not in groups:
                groups[key] = [strs[s]]  # start new list
            else:
                groups[key].append(strs[s])  # add to existing
        return list(groups.values())