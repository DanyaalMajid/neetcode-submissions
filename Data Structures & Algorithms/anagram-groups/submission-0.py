class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)

        for str in strs:
            freqs = [0] * 26
            for char in str:
                freqs[ord(char) - ord("a")] += 1
            result[tuple(freqs)].append(str)

        return list(result.values())