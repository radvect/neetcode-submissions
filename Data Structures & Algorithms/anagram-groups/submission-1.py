class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import defaultdict

        anagrams = defaultdict(list)
        
        for i in strs:
            ls =[0]*26
            for j in i:
                ls[ord(j) - ord("a")]+=1
            key = tuple(ls)
            anagrams[key].append(i)
        #print(list(anagrams.values()))

        return list(anagrams.values())

        


