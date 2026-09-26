class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True

        if nums[0] == 0:
            return False
        
        furthest = 0 + nums[0]

        for i in range(len(nums)):

            if furthest >= len(nums)-1:
                return True

            j = i+1
            new_reachable = 0

            while j<=furthest:
                candidate_furthest = j + nums[j]

                if candidate_furthest >= len(nums)-1:
                    return True

                if candidate_furthest > furthest:
                    new_reachable = candidate_furthest

                j+=1

            if new_reachable <= furthest:
                return False

            if new_reachable > furthest:
                furthest = new_reachable

            


        