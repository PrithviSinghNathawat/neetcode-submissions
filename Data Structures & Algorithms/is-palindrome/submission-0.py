class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1
        y=s.lower()
        while left <= right: 
            if not y[left].isalnum():
                left += 1
                continue
            if not y[right].isalnum():
                right -= 1
                continue
            if y[left] != y[right]:
                return False
            left+=1
            right-=1
        return True


            

