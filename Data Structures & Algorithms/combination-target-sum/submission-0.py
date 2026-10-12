class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        result = []

        def dfs(i, path, current_sum):
            if current_sum == target:
                result.append(path.copy())
                return

            if i >= len(nums) or current_sum > target:
                return

            path.append(nums[i])

            dfs(i, path, current_sum + nums[i])

            path.pop()

            dfs(i+1, path, current_sum)

        dfs(0, [], 0)

        return result


