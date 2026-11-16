class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        heap = []

        res = []

        l , r = 0, 0

        while r < len(nums):

            heapq.heappush(heap,(-nums[r],r))

            if heap[0][1] < l:
                heapq.heappop(heap)
            
            if (r+1) >= k:
                res.append(-heap[0][0])
                l+=1

            r+=1

        return res
            

            


        