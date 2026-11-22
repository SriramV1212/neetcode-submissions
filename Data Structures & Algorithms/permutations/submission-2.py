class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        res = []

        path = []
        added = set()

        def backtrack():
            if len(path) == len(nums):
                res.append(path.copy())
                return

            
            for j in range(len(nums)):
                if nums[j] not in added:
                    added.add(nums[j])
                    path.append(nums[j])
                    backtrack()
                    path.pop()
                    added.remove(nums[j])


        backtrack()

        return res
        