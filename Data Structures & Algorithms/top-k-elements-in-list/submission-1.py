class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count={}
        for n in nums:
            count[n]= 1 + count.get(n,0)

        heap=[]
        for n,f in count.items():
            heapq.heappush(heap,(f,n))
            if len(heap) > k:
                heapq.heappop(heap)
        
        r=[]
        for i in range(k):
            r.append(heapq.heappop(heap)[1])
        return r