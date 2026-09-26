class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        furthest = 0

        for i in range(len(nums)):
            if i > furthest:
                return False

            candidate_furthest = i + nums[i]

            furthest = max(furthest, candidate_furthest)

            if furthest >= len(nums)-1:
                return True

            


        