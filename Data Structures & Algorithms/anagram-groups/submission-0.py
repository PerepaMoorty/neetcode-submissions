class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list)

        for i in range(len(strs)):
            key = str(sorted(strs[i]))
            hashmap[key].append(i)

        result = []
        keys = list(hashmap.keys())
        for key in keys:
            index_list = hashmap[key]
            temp = []
            for index in index_list:
                temp.append(strs[index])
            result.append(temp)

        return result