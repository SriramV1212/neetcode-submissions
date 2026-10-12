class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        result = []

        nums.sort()

        def dfs(i, path, current_sum):
            if current_sum == target:
                result.append(path.copy())
                return

            
            for j in range(i, len(nums)):
                if current_sum + nums[j] > target:
                    return

                path.append(nums[j])

                dfs(j, path, current_sum + nums[j])

                path.pop()

        dfs(0, [], 0)

        return result
        