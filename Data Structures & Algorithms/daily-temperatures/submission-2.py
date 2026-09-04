class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        mt = [0]*len(temperatures)
        stack=[]
        for y, x in enumerate(temperatures):
            while stack and temperatures[stack[-1]]<x:
                i=stack.pop()
                mt[i] = y-i
            stack.append(y)
        return mt