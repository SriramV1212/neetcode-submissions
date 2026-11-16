class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        heap = []
        res = []

        for n in nums:

            if len(heap) < k:
                heapq.heappush(heap,-n)
            
            if len(heap)==k and n > -heap[0]:
                heapq.heappop(heap)
                heapq.heappush(heap,-n)
                res.append(n)
            elif len(heap)==k and n <= -heap[0]:
                res.append(-heap[0])

        return res


        # heap = [-6,-1,-1], res = [2,2,4,4,6]

        # 6 > 4



        



            
        