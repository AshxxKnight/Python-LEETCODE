#Problem Number-14
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        pref = ''
        for i in zip(*strs):
            if len(set(i)) ==1:
                pref += i[0]
            else:
                break
                
        return pref
