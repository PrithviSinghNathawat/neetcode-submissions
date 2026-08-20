class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l=0
        checkset=set()
        count=0
        for x in s:
            while x in checkset:
                checkset.remove(s[l])
                l+=1
            checkset.add(x)
            count=max(count,len(checkset))
        return count
