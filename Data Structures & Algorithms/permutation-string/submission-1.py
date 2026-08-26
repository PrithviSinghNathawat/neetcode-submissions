class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1d={val : s1.count(val) for val in s1}
        l,r=0,len(s1)
        s2d={}
        for x in s2[:len(s1)]:
            if x in s2d:
                s2d[x]+=1
            else:
                s2d[x]=1                
        if s1d==s2d:
            return True           
        while r<len(s2):                             
            if s2[r] in s2d:
                s2d[s2[r]]+=1
            else:
                s2d[s2[r]]=1
            r+=1
            s2d[s2[l]]-=1
            if s2d[s2[l]] == 0:
                del s2d[s2[l]]
            l+=1            
            if s1d==s2d:
                return True   
            
        return False
