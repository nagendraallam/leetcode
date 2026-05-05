class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map = {}
        result = []

        for i, val in enumerate(strs):
            key = "".join(sorted(val))
            if key not in map.keys():
                map[key] = []

            map[key].append(val)

        for key,value in map.items():
            result.append(value)

        return result

        