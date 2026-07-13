class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d=defaultdict(int)
        for x in nums:
            d[x]+=1
        sol=[]
        sortd=dict(sorted(d.items(), key=lambda item:item[1], reverse=True))
        while k>0:
            k-=1
            sol.append(list(sortd.keys())[k])
        return sol

            