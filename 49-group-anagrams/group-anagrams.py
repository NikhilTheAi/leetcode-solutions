class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        groups = {}

        for word in strs:
            freq = [0] * 26

            for ch in word:
                pos = ord(ch) - ord('a')
                freq[pos] += 1

            freq = tuple(freq)

            if freq not in groups:
                groups[freq] = []

            groups[freq].append(word)

        return list(groups.values())