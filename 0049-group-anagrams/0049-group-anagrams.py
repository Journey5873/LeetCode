from collections import defaultdict

class Solution(object):
    def groupAnagrams(self, strs):
        anagrams = defaultdict(list)

        for word in strs:
            anagrams["".join(sorted(word))].append(word)
        return list(anagrams.values())