class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ml=start=0
        for i in range(len(s)):
            if s[i] not in s[start:i]:
                ml=max(ml,i+1-start)
            else:
                start+=(1+s[start:i].index(s[i]))
        return max(ml,(len(s)-start))
