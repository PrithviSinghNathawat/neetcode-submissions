class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:        
        x=[]
        nums.sort()
        n=len(nums)
        for i in range(0,n-2):   
            if nums[i] >0:
                break            
            if i>0 and nums[i]==(nums[i-1]):
                continue
            l = i+1
            r = n-1
            while l<r:
                sum = nums[i] + nums[l] + nums[r]
                if sum>0:
                    r-=1
                elif sum<0:
                    l+=1
                else:
                    x.append([nums[i],nums[r],nums[l]])
                    l+=1
                    r-=1
                    while(l<r and nums[l] == nums[l-1]):
                        l+=1
                    while(l<r and nums[r] == nums[r+1]):
                        r-=1
        return x        
                    
            
        
        
                
