
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        r = k
        maxl = []
        win = deque()        
        for x in range(k):
            while win and nums[win[-1]] <= nums[x]:
                win.pop()
            win.append(x)
        maxl.append(nums[win[0]])        

        while r < len(nums):            
            if win and win[0] < r - k + 1:
                win.popleft()            
            while win and nums[win[-1]] <= nums[r]:
                win.pop()

            win.append(r)            
            maxl.append(nums[win[0]])
            r += 1
        return maxl