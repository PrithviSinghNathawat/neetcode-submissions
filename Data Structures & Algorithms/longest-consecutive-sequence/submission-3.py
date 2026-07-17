class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        i=1
        hcount=1        
        if not nums:
            return 0
        else:
            snum=sorted(nums)
            
        for x,j in enumerate(snum):             
            
            if j==snum[0]:
                continue
            elif j == snum[x-1]:
                    continue
            elif j == snum[x-1]+1:                
                i+=1
                hcount = max(i,hcount)                
            else:
                i=1                
        return hcount