class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for i in strs:
            if "".join(sorted(i)) not in d:
                d["".join(sorted(i))] = []
                d["".join(sorted(i))].append(i)
                continue
            d["".join(sorted(i))].append(i)
        ans = []
        for key,vals in d.items():
            ans.append(vals)
        return ans

        
        